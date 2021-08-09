import  unittest

from jforumTest.bbs.testcase.models import myunit, function
from jforumTest.bbs.testcase.page_obj.loginPage import login


class testlogin(myunit.MyTest):

    def user_login_verify(self, username='', password=''):
        login(self.driver).user_login(username, password)

    def test_login1(self):
        self.user_login_verify()
        po = login(self.driver)
        self.assertEqual(po.user_error_hint(), '您输入了无效的用户名或错误的密码')
        self.assertEqual(po.pawd_error_hint(), '您输入了无效的用户名或错误的密码')
        function.insert_img(self.driver, 'user_pawd_empty.jpg')

    def test_login2(self):
        self.user_login_verify(username='test8')
        po = login(self.driver)
        self.assertEqual(po.pawd_error_hint(), '您输入了无效的用户名或错误的密码')
        function.insert_img(self.driver, 'user_pawd_error.jpg')

    def test_login4(self):
        self.user_login_verify(username='test6', password='1234')
        po = login(self.driver)
        self.assertEqual(po.user_login_success(), '注销 [test6]')
        function.insert_img(self.driver, 'success.jpg')


if __name__ == "__main__":
    unittest.main()
