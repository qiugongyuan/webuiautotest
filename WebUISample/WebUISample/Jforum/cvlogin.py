import codecs
import time

from selenium import webdriver

source = codecs.open("D:\qgy work\jmeter learning\\users.txt", "r", "gb18030")
values = source.readlines()
users = []
pwds = []

for val in values:
    user, pwd = val.split(',')
    user = user.strip('\t\r\n')
    pwd = pwd.strip('\t\r\n')
    users.append(user)
    pwds.append(pwd)
print(users)
print(pwds)

for user in users:
    driver = webdriver.Chrome()
    driver.get('http://localhost:8080/jforum-2.1.9/user/login.page')
    driver.find_element_by_name('username').clear()
    driver.find_element_by_name('username').send_keys(user)
    time.sleep(2)
    driver.find_element_by_name('password').send_keys(pwd)
    driver.find_element_by_name('login').click()
    time.sleep(3)
    driver.find_element_by_id('logout').click()
    driver.quit()
