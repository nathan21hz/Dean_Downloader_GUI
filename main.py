# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox
from Ui_main_ui import Ui_MainWindow
from Ui_edit import Ui_Dialog
import urllib
import urllib.request
import http.cookiejar
from lxml import etree
import os
import json

total = 0
count = 0
loggedin = False
appdir = os.getcwd()
version = '2.2.5'
updateinfo = {}
print(appdir)

loginurl = "http://jiaowu.swjtu.edu.cn/servlet/UserLoginSQLAction"
headers = { "Referer" : "http://jiaowu.swjtu.edu.cn/service/login.jsp?user_type=student"}
imgurl = "http://jiaowu.swjtu.edu.cn/servlet/GetRandomNumberToJPEG"

coursepage_url = "http://jiaowu.swjtu.edu.cn/servlet/StudentCourseAction?Action=resourceView&course_code="

cookie = http.cookiejar.MozillaCookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
urllib.request.install_opener(opener)


#重写主界面类
class mywindow(Ui_MainWindow):
    def refresh(self):
        img_req = urllib.request.Request(imgurl)
        img_response = opener.open(img_req)
        out=open('code.jpg','wb')
        out.write(img_response.read())
        out.flush()
        out.close()
        codep = QPixmap('code.jpg')
        self.pic_label.setPixmap(codep)
        return
        
    def login(self):
        global loggedin
        data = urllib.parse.urlencode({
            "user_id": self.no_edit.text(),
            "password":self.pw_edit.text(),
            "setlanguage": "cn",
            "user_type":"student",
            "ranstring":self.check_edit.text(),
            "btn1":""}).encode(encoding='UTF8')

        request = urllib.request.Request(loginurl,data,headers)
        result = opener.open(request)
        print (result.read)
        if "url=".encode(encoding='UTF8') in result.read():
            self.textBrowser.append("登陆成功！")
            self.textBrowser.moveCursor(QtGui.QTextCursor.End)
        else :
            self.textBrowser.append("登陆失败，请检查密码/验证码并再次尝试。")
            self.textBrowser.moveCursor(QtGui.QTextCursor.End)
            return
#        读取课程列表
        self.textBrowser.append ("正在获取课程信息...")
        self.textBrowser.moveCursor(QtGui.QTextCursor.End)
        dean_url = "http://jiaowu.swjtu.edu.cn/student/course/MyCourseThisTerm.jsp"
        request = opener.open(dean_url)
        content = request.read().decode("utf-8")
        code_items = etree.HTML(content).xpath('//*[@id="table6"]/tr/td[3]/text()')
        teacher_items = etree.HTML(content).xpath('//*[@id="table6"]/tr/td[8]/a/u/text()|//*[@id="table6"]/tr/td[8]/text()')
        for t in teacher_items:print(t)
        for t in code_items:print(t)
        #重置课程文件
        coursedata = open("course.json","w", encoding="utf-8")
        coursedata.write("{}")
        coursedata.close()
        #写入课程文件
        coursedata = open("course.json","r", encoding="utf-8")
        f=coursedata.read()
        coursedata.close()
        data=json.loads(f)
        coursedata = open("course.json","w", encoding="utf-8")
        for i in range(len(code_items)-1):
            data.update({code_items[i+1].strip():teacher_items[i+1].strip()})
        f=json.dumps(data)
        coursedata.write(f)
        coursedata.close()
        ref_list()
        self.textBrowser.append ("完成！")
        self.textBrowser.moveCursor(QtGui.QTextCursor.End)
        loggedin = True
        QMessageBox.information(MainWindow,"提示", "推荐使用教育网进行下载\n使用其他网络可能使下载极其缓慢\n（直接连接墙上网线插座不拨号亦可）",QMessageBox.Yes)
        
    def sel_route(self):
        self.route_edit.setText(QtWidgets.QFileDialog.getExistingDirectory(MainWindow, '选择路径', '/home'))
        return
        
    def start_down(self):
        global loggedin
        if(loggedin == False):
            QMessageBox.information(MainWindow,"提示", "请先登陆！",QMessageBox.Yes)
            return
        if(self.route_edit.text() == ''):
            QMessageBox.information(MainWindow,"提示", "请先选择下载路径！",QMessageBox.Yes)
            return
        global total
        global count
        total = 0
        count = 0
        ui.textBrowser.append("正在获取课件数...")
        ui.textBrowser.moveCursor(QtGui.QTextCursor.End)
        CountFile()
        ui.textBrowser.append("课件共计 "+str(total)+" 个")
        ui.textBrowser.moveCursor(QtGui.QTextCursor.End)
        workthread.start()
        workthread.trigger.connect(ReBar)
        return
        
    def list_edit(self):
        row = self.list.currentItem()
        if(row):
            course_code , T_name =row.text().split(' ')
            dialog.code_edit.setText(course_code)
            dialog.teacher_edit.setText(T_name)
            Dialog.exec_()
            ref_list()
        return
        
    def list_add(self):
        Dialog.exec_()
        ref_list()
        return
        
    def list_del(self):
        row = self.list.currentItem()
        if(row):
            coursedata = open("course.json","r", encoding="utf-8")
            f=coursedata.read()
            coursedata.close()
            data=json.loads(f)
            coursedata = open("course.json","w", encoding="utf-8")
            course_code , T_name =row.text().split(' ')
            del data[course_code]
            f=json.dumps(data)
            coursedata.write(f)
            coursedata.close()
            Dialog.close()
            ref_list()
        return
        
    def refilelist(self):
        files = open("filelist.json","w", encoding="utf-8")
        f='[]'
        files.write(f)
        files.close()
        return

#重写修改对话框类
class mydialog(Ui_Dialog):
    def doEdit(self):
        coursedata = open("course.json","r", encoding="utf-8")
        f=coursedata.read()
        if(f == ''):
            f="{}"
        coursedata.close()
        data=json.loads(f)
        coursedata = open("course.json","w", encoding="utf-8")
        data.update({self.code_edit.text():self.teacher_edit.text()})
        f=json.dumps(data)
        coursedata.write(f)
        coursedata.close()
        Dialog.close()
        return

class WorkThread(QtCore.QThread):
    trigger = QtCore.pyqtSignal()
    def __int__(self):  
        super(WorkThread,self).__init__()  
  
    def run(self):
        global count
        course = GetCourseInfo()
        disk = ui.route_edit.text()
        ui.textBrowser.append("文件将会被保存在 "+disk+"/Courseware")
        ui.textBrowser.moveCursor(QtGui.QTextCursor.End)
        #读取文件列表
        files = open("filelist.json","r", encoding="utf-8")
        f=files.read()
        files.close()
        filelist=json.loads(f)
        for c in course:
            try:
                course_code = c
                T_name = course[c]
                dirname = CodeToName(c)+'-'+T_name
                ui.textBrowser.append('正在下载 '+dirname)
                ui.textBrowser.moveCursor(QtGui.QTextCursor.End)
                request = opener.open(coursepage_url + course_code)
                content = request.read().decode("utf-8")
                fileurl_list = etree.HTML(content).xpath('//*[@id="pageBodyRight"]/table/tr/td/div/table/tr[1]/td/table/tr[3]/td/table/tr/td[2]/a/@href')
                fileteacher_list = etree.HTML(content).xpath('//*[@id="pageBodyRight"]/table/tr/td/div/table/tr[1]/td/table/tr[3]/td/table/tr/td[3]/a/u/text()')
                try:
                    os.makedirs(os.path.join(disk +"/Courseware", dirname))
                    ui.textBrowser.append("Created a new folder named " + T_name)
                    ui.textBrowser.moveCursor(QtGui.QTextCursor.End)
                except:
                    ui.textBrowser.append("Folder "+ dirname +" already exist")
                    ui.textBrowser.moveCursor(QtGui.QTextCursor.End)
                os.chdir(os.path.join(disk + "/Courseware", dirname))
                for i in range(len(fileurl_list)):
                    if fileteacher_list[i].strip() == T_name:
                        fileid = fileurl_list[i].strip().replace("../../servlet/ResourceAction?SetAction=view&resource_id=","")
                        #ToDo:
                        print(fileid)
                        filepage_url = fileurl_list[i].strip().replace("../..","http://jiaowu.swjtu.edu.cn")
                        #print (filepage_url +"\t")
                        req_file = opener.open(filepage_url)
                        filepage =  req_file.read().decode("utf-8")
                        filehtml = etree.HTML(filepage)
                        filename = filehtml.xpath('//*[@id="table1"]/tr[2]/td[2]/font/b/text()')[0].strip()
                        downloadurl = filehtml.xpath('//*[@id="table1"]/tr[2]/td[4]/a/@href')[0].strip()
                        print (filename.encode("utf-8") , downloadurl)
                        try:
                            if(fileid not in filelist):
                                filelist.append(fileid)
                                download(filename,downloadurl)
                            count = count + 1
                            self.trigger.emit()
                        except:
                            ui.textBrowser.append("Download error!")
                            ui.textBrowser.moveCursor(QtGui.QTextCursor.End)
            except:
                ui.textBrowser.append("Course data error!")
                ui.textBrowser.moveCursor(QtGui.QTextCursor.End)
        global appdir
        os.chdir(appdir)
        #写入文件列表
        files = open("filelist.json","w", encoding="utf-8")
        f=json.dumps(filelist)
        files.write(f)
        files.close()
        ui.textBrowser.append("下载完成。")
        ui.textBrowser.moveCursor(QtGui.QTextCursor.End)

#读取课程文件
def GetCourseInfo():
    coursedata = open('course.json','r',encoding='utf-8')
    f=coursedata.read()
    data=json.loads(f)
    coursedata.close()
    return data

#统计课件数目
def CountFile():
    global total
    course = GetCourseInfo()
    for c in course:
        try:
            course_code = c
            T_name = course[c]
            print (course_code , T_name)
            request = opener.open(coursepage_url + course_code)
            content = request.read().decode("utf-8")
            fileteacher_list = etree.HTML(content).xpath('//*[@id="pageBodyRight"]/table/tr/td/div/table/tr[1]/td/table/tr[3]/td/table/tr/td[3]/a/u/text()')
            for i in fileteacher_list:
                if i == T_name:
                    try:
                        total = total + 1
                    except:
                        ui.textBrowser.append("Count error!")
                        ui.textBrowser.moveCursor(QtGui.QTextCursor.End)
        except:
            ui.textBrowser.append("Course data error!")
            ui.textBrowser.moveCursor(QtGui.QTextCursor.End)

#刷新进度条
def ReBar():
    ui.progressBar.setValue(int(count/total*100))

#下载
def download(filename,downloadurl):
    if(filename.split('.')[0] == ''):
        filename = '未命名文件No_'+str(count)+filename
    print(filename)
    f = urllib.request.urlopen(downloadurl)
    with open(filename, "wb") as code:
        code.write(f.read())
        
#刷新列表
def ref_list():
    ui.list.clear()
    course = GetCourseInfo()
    for c in course:
        ui.list.addItem(c+' '+course[c])
    return

#通过课程代码读课程名
def CodeToName(code):
    try:
        url = "http://jwc.swjtu.edu.cn//servlet/CourseInfoMapAction?SelectTableType=ThisTerm&MapID=101&PageUrl=..%2Fother%2FCourseList.jsp&SelectAction=CourseCode&KeyWord1="+str(code)
        response = urllib.request.urlopen(url)
        page = response.read().decode("utf-8")
        name = etree.HTML(page).xpath('//*[@id="table6"]/tr[2]/td[4]/text()')
        return name[0]
    except:
        return False

def CheckUpdate():
    global version
    global updateinfo
    try:
        url = "http://www.21hz.top/courseware/version.json"
        response = urllib.request.urlopen(url=url,timeout=2)
        vdpage = response.read().decode("utf-8")
        versiondata = json.loads(vdpage)
        print(versiondata['version'])
        if(versiondata['version'] != version):
            updateinfo = versiondata
            ans = QMessageBox.information(MainWindow,"提示", "检测到新版本，是否前往下载？\nV"+versiondata['version']+'\n'+versiondata['notice']+'\n(下载后执行覆盖安装即可)',QMessageBox.Yes|QMessageBox.No)
            if(ans == QMessageBox.Yes):
                ui.textBrowser.append('正在下载新版本安装包，请稍候……')
                ui.textBrowser.moveCursor(QtGui.QTextCursor.End)
                updatethread.start()
            else:
                return
        else:
            return
    except:
        QMessageBox.information(MainWindow,"提示", "检查更新时出错",QMessageBox.Yes)
        return

class UpdateThread(QtCore.QThread):
    def __int__(self):  
        super(UpdateThread,self).__init__()  
  
    def run(self):
        global updateinfo
        work_path = os.path.abspath('.')+'\V'+updateinfo['version']+'.exe'
        print(work_path)
        urllib.request.urlretrieve(updateinfo['url'],work_path,self.UpdateCbk)
        try:
            os.startfile(work_path)
        except:
            ui.textBrowser.append('安装失败')
            ui.textBrowser.moveCursor(QtGui.QTextCursor.End)
        QtCore.QCoreApplication.instance().quit()

    def UpdateCbk(self,a,b,c):
        per=100.0*a*b/c  
        if(per<100):
            print('正在下载新版本安装包：'+'%.2f'%per+'%')
        else:  
            ui.textBrowser.append('下载完成，安装稍后开始。')
            ui.textBrowser.moveCursor(QtGui.QTextCursor.End)  

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    Dialog = QtWidgets.QDialog()
    ui = mywindow()
    dialog = mydialog()
    ui.setupUi(MainWindow)
    dialog.setupUi(Dialog)
    workthread = WorkThread()
    updatethread = UpdateThread()
    ui.refresh()
    _translate = QtCore.QCoreApplication.translate
    MainWindow.setWindowTitle(_translate("MainWindow", "自动课件下载器 V"+version+" By Nathan_21hz"))
    MainWindow.show()
    CheckUpdate()
    sys.exit(app.exec_())
