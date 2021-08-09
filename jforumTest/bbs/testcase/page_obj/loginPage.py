from time import sleep

from selenium.webdriver.common.by import By

from jforumTest.bbs.testcase.page_obj.base import Page


class login(Page):
    url = ''
    bbs_login_user_loc = (By.NAME, 'username')
    bbs_login_button_loc = (By.ID, 'login')

    def bbs_login(self):
        self.find_element(*self.bbs_login_user_loc).click()
        sleep(1)
        self.find_element(*self.bbs_login_button_loc).click()

    login_username_loc = (By.NAME, 'username')
    login_password_loc = (By.NAME, 'password')
    login_button_loc = (By.NAME, 'login')

    def login_username(self, username):
        self.find_element(*self.login_username_loc).send_keys(username)

    def login_password(self, password):
        self.find_element(*self.login_password_loc).send_keys(password)

    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    def user_login(self, username='test6', password='1234'):
        self.open()
        self.bbs_login()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        sleep(2)

    user_error_hint_loc = (By.XPATH, '//*[@id="invalidlogin"]/font')
    pawd_error_hint_loc = (By.XPATH, '//*[@id="invalidlogin"]/font')
    user_login_success_loc = (By.ID, 'logout')

    def user_error_hint(self):
        return self.find_element(*self.user_error_hint_loc).text

    def pawd_error_hint(self):
        return self.find_element(*self.pawd_error_hint_loc).text

    def user_login_success(self):
        return self.find_element(*self.user_login_success_loc).text
