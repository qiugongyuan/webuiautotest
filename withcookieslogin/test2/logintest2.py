import json
import time

from selenium import webdriver

url = 'https://account.cnblogs.com/signin'
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(2)
driver.delete_all_cookies()
with open("cookies.txt", "r") as f:
    cookies = json.load(f)
    for cookie in cookies:
        driver.add_cookie(cookie)
driver.get(url)
driver.get('https://www.cnblogs.com/')
time.sleep(3)
driver.quit()