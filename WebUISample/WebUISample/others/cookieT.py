from selenium import webdriver

driver=webdriver.Chrome()
driver.get('http://www.youdao.com')
cookie=driver.get_cookies()
print(cookie)
driver.add_cookie({'name':'key-aaaaa','value':'value-bbbbb'})
for cookie in  driver.get_cookies():
    print("%s -> %s" %(cookie['name'],cookie['value']))
driver.quit()