import json
import time,os

import yaml
from selenium import webdriver
url = 'https://account.cnblogs.com/signin'
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="mat-input-0"]').clear()
driver.find_element_by_xpath('//*[@id="mat-input-0"]').send_keys("360960443@qq.com")
driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@id="mat-input-1"]').clear()
driver.find_element_by_xpath('//*[@id="mat-input-1"]').send_keys("QGYLZLXNZ114")
print("请输入验证码：")
# 手动输入验证码
security_code = input()
time.sleep(1)
#driver.find_element_by_id("security_code").send_keys(security_code)
time.sleep(1)
driver.find_element_by_xpath('/html/body/app-root/mat-sidenav-container/mat-sidenav-content/div/div/app-sign-in/app-content-container/div/div/div/form/div/button').click()
driver.implicitly_wait(5)
# 加一个休眠，这样得到的cookie 才是登录后的cookie,否则可能打印的还是登录前的cookie
time.sleep(5)
cookiesAfter = driver.get_cookies()
print(cookiesAfter)
with open("cookies.txt", "w")  as f:
    json.dump(cookiesAfter, f)
driver.quit()

