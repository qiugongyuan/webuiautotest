

class Login():
    def user_login(self, driver):
     driver.find_element_by_name('username').clear()
     driver.find_element_by_name('username').send_keys('test9')
     driver.find_element_by_name('password').send_keys('1234')
     driver.find_element_by_name('login').click()

    def user_logout(self, driver):
        driver.find_element_by_id('logout').click()
        driver.quit()
