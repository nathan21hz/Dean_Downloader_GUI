# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from Ui_main_ui import Ui_MainWindow
from Ui_edit import Ui_Dialog
import urllib
import http.cookiejar
import re
from lxml import etree
import os
import json

total = 0
count = 0

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
            self.textBrowser.append("登陆失败，请再次尝试。")
            self.textBrowser.moveCursor(QtGui.QTextCursor.End)
#        读取课程列表
        self.textBrowser.append ("正在获取课程信息...")
        self.textBrowser.moveCursor(QtGui.QTextCursor.End)
        dean_url = "http://jiaowu.swjtu.edu.cn/student/course/MyCourseThisTerm.jsp"
        request = opener.open(dean_url)
        content = request.read().decode("utf-8")
        listcom = re.compile( r'<tr>\s*?<td.*?>(.*?)</td>.*?<td.*?<td.*?>.*?(\d*)</td>.*?<td.*?<font color="#000080">(.*?)<br>.*?</td>.*?<td.*?<td.*?<td.*?<td.*?<u>(.*?)</u>.*?</td>.*?<td.*?<td.*?style="line-height: 150%">.*?</td>.*?</tr>',re.S)
        items = re.findall(listcom,content)
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
        for item in items:
            data.update({item[1]:item[3]})
        f=json.dumps(data)
        coursedata.write(f)
        coursedata.close()
        ref_list()
        self.textBrowser.append ("完成！")
        self.textBrowser.moveCursor(QtGui.QTextCursor.End)
        
    def sel_route(self):
        self.route_edit.setText(QtWidgets.QFileDialog.getExistingDirectory(MainWindow, '选择路径', '/home'))
        return
        
    def start_down(self):
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
        coursedata = open("course.json","r", encoding="utf-8")
        f=coursedata.read()
        coursedata.close()
        data=json.loads(f)
        coursedata = open("course.json","w", encoding="utf-8")
        row = self.list.currentItem()
        if(row):
            course_code , T_name =row.text().split(' ')
            del data[course_code]
            f=json.dumps(data)
            coursedata.write(f)
            coursedata.close()
            Dialog.close()
            ref_list()
        return

#重写修改对话框类
class mydialog(Ui_Dialog):
    def doEdit(self):
        coursedata = open("course.json","r", encoding="utf-8")
        f=coursedata.read()
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
        ui.textBrowser.append("Files will be saved in "+disk+"/coursefile")
        ui.textBrowser.moveCursor(QtGui.QTextCursor.End)
        for c in course:
            try:
                course_code = c
                T_name = course[c]
                ui.textBrowser.append(course_code+T_name)
                ui.textBrowser.moveCursor(QtGui.QTextCursor.End)
                request = opener.open(coursepage_url + course_code)
                content = request.read().decode("utf-8")
                listcom = re.compile(r'<tr>\s*?<td.*?>.*?<td.*?><a href="(.*?)" target="_blank">.*?<td.*?><a.*?><u>(.*?)</u></a></td>.*?<td.*?<td.*?<td.*?</tr>',re.S)
                items = re.findall(listcom, content)
                try:
                    os.makedirs(os.path.join(disk +"/coursefile", T_name))
                    ui.textBrowser.append("Created a new folder named " + T_name)
                    ui.textBrowser.moveCursor(QtGui.QTextCursor.End)
                except:
                    ui.textBrowser.append("Folder "+ T_name +" already exist")
                    ui.textBrowser.moveCursor(QtGui.QTextCursor.End)
                os.chdir(os.path.join(disk + "/coursefile", T_name))
                for i in items:
                    if i[1] == T_name:
                        filepage_url = i[0].replace("../..","http://jiaowu.swjtu.edu.cn")
                        print (filepage_url +"\t")
                        req_file = opener.open(filepage_url)
                        filepage =  req_file.read().decode("utf-8")
                        filehtml = etree.HTML(filepage)
                        filename = filehtml.xpath('//*[@id="table1"]/tr[2]/td[2]/font/b/text()')[0]
                        downloadurl = filehtml.xpath('//*[@id="table1"]/tr[2]/td[4]/a/@href')[0]
                        print (filename.encode("utf-8") , downloadurl)
                        try:
                            download(filename,downloadurl)
                            count = count + 1
                            self.trigger.emit()
                        except:
                            ui.textBrowser.append("Download error!")
                            ui.textBrowser.moveCursor(QtGui.QTextCursor.End)
            except:
                ui.textBrowser.append("Course data error!")
                ui.textBrowser.moveCursor(QtGui.QTextCursor.End)
        ui.textBrowser.append("下载完成。")
        ui.textBrowser.moveCursor(QtGui.QTextCursor.End)

#读取课程文件
def GetCourseInfo():
    coursedata = open('course.json','r',encoding='utf-8')
    f=coursedata.read()
    data=json.loads(f)
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
            listcom = re.compile(r'<tr>\s*?<td.*?>.*?<td.*?><a href="(.*?)" target="_blank">.*?<td.*?><a.*?><u>(.*?)</u></a></td>.*?<td.*?<td.*?<td.*?</tr>',re.S)
            items = re.findall(listcom, content)
            for i in items:
                if i[1] == T_name:
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
    ui.refresh()
    MainWindow.show()
    sys.exit(app.exec_())

