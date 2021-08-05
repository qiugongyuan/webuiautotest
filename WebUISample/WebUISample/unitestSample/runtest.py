import os
import smtplib
import time
import  unittest
#方法一
# import testadd
# import testsub
# suit=unittest.TestSuite()
# suit.addTest(testadd.TestAdd('test_add1'))
# suit.addTest(testadd.TestAdd('test_add2'))
# suit.addTest(testsub.TestAdd('test_sub1'))
# suit.addTest(testsub.TestAdd('test_sub2'))
# if __name__=='__main__':
#     runner=unittest.TextTestRunner()
#     runner.run(suit)
#方法二

import unittest
from HTMLTestRunner import HTMLTestRunner




#定义发送邮件
from email.header import Header
from email.mime.text import MIMEText


def send_mail(file_new):
    f=open(file_new,'rb')
    mail_body=f.read()
    f.close()

    msg=MIMEText(mail_body,'html','utf-8')
    msg['Subject']=Header('自动化测试报告','utf-8')
    smtpserver = 'smtp.qq.com'
    sender = "360960443@qq.com"
    receive = "360960443@qq.com"
    user = "360960443"
    password = "mebjtiodnnlwbicg"
    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    smtp.login(user,password)
    smtp.sendmail(sender,receive,msg.as_string())
    smtp.quit()
    print('email has send out!')

#查找最新测试报告

def new_report(testreport):
    lists=os.listdir(testreport)
    lists.sort(key=lambda fn:os.path.getmtime(testreport+"\\"+fn))
    file_new=os.path.join(testreport,lists[-1])
    print(file_new)
    return file_new

test_dir= 'testsequ/'
discover=unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

if __name__=='__main__':
    runner=unittest.TextTestRunner()
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    test_report='D:\\qgy work\\python project\\selenium\\WebUISample\\WebUISample\\report'
    dir_path = test_report +"\\"+ now + 'result.html'
    fp = open(dir_path, 'wb')
    runner = HTMLTestRunner(stream=fp, title='练习测试报告', description='用例测试情况:')
    runner.run(discover, 0, False)

    new_report=new_report(test_report)
    send_mail(new_report)