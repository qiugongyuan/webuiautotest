import os
import time
import unittest
from HTMLTestRunner import HTMLTestRunner


# 测试顺序,数字与字母的顺序为:0-9,A-Z,a-z

class TestBdd(unittest.TestCase):

    def setUp(self):
        print('test TestBdd ')

    def tearDown(self):
        print('test TestBdd end')

    def test_ccc(self):
        print('test ccc')

    def test_aaa(self):
        print('test aaa')


class TestAdd(unittest.TestCase):
    def setUp(self):
        print('test TestAdd ')

    def tearDown(self):
        print('test TestAdd end')

    def test_bbb(self):
        print('test bbb')


if __name__ == '__main__':
    testsuit = unittest.TestSuite()
    testsuit.addTest(TestBdd('test_ccc'))
    testsuit.addTest(TestBdd('test_aaa'))
    testsuit.addTest(TestAdd('test_bbb'))
    #current_path = os.getcwd()
    #result_path = os.path.join(current_path, 'report.html')
    now=time.strftime("%Y-%m-%d %H-%M-%S")
    dir_path='D:\\qgy work\\python project\\selenium\\WebUISample\\WebUISample\\report\\'+now+'result.html'
    # with open(dir_path, 'wb') as report:
    #     runner = HTMLTestRunner(
    #         stream=report,
    #         title='测试报告',
    #         description='用例执行情况:',
    #         )
    fp=open(dir_path,'wb')
    runner=HTMLTestRunner(stream=fp,title='练习测试报告',description='用例测试情况:')
    runner.run(testsuit,0,False)
    fp.close()
