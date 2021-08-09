import json

import requests as requests
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication

#创建程序对象
app=QApplication([])
#创建ui文件
file=QFile('requestTool.ui')
#以只读的形式打开UI文件
file.open(QFile.ReadOnly)
#加载UI文件内的组件
ui=QUiLoader().load(file)
#关闭ui文件对象
file.close()

#程序逻辑处理
#初始化下拉框的下拉选项值
ui.select_comboxBox.addItems(['请选择','GET','POST','PUT','DELETE'])
#获取接口相关数据
def send_request():
    method=ui.select_comboxBox.currentText()#获取当前选中文本
    url=ui.url_lineEdit.text()
    data_body=ui.body.toPlainText()
    data_header=ui.header.toPlainText()
    #获取到的请求头和请求体是str格式,需要转为json格式
    body=json.loads(data_body)
    header=json.loads(data_header)
    #发送接口请求
    resp=requests.request(method=method, url=url, params=body, headers=header)
    #展示响应数据
    #响应数据要添加到文本浏览器内时,需要先转为字符串格式
    msg_header=str(resp.headers)
    msg_body=str(resp.text)
    ui.resp_h_textBrowser.append(msg_header)
    ui.resp_b_textBrowser.append(msg_body)

    #清空数据函数
def clear():
    ui.resp_h_textBrowser.clear()
    ui.resp_b_textBrowser.clear()
    ui.select_comboxBox.setCurrentText('请选择')#清空时,恢复默认选项'请选择'

ui.send_pushButton.clicked.connect(send_request)
ui.clear_pushButtion.clicked.connect(clear)

#展示ui图形界面
ui.show()

#运行程序
app.exec_()