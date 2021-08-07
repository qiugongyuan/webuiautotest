from selenium import webdriver
import time,yaml,os
url = 'https://account.cnblogs.com/signin'
driver = webdriver.Chrome()
driver.maximize_window()
driver.delete_all_cookies()
time.sleep(3)
driver.get(url)

fileNamePath = os.path.split(os.path.realpath(__file__))[0]
yamlPath = os.path.join(fileNamePath, 'config2.yaml')
# 读取yaml 文件
f = open(yamlPath,'r',encoding='utf-8')
cont = f.read()
conf = yaml.load(cont)
# 读取cookie值
cookie1 = conf.get("cookie1")
# 添加cookie
driver.add_cookie(cookie1)
print(cookie1)
print("cookies")
print(driver.get_cookies())
time.sleep(5)
# 这里重新获取地址，因为有些系统，未登录状态，链接会跳转，这里就是，登录状态后，才能正确打开指定网址，所以这里要再次指定网址。
driver.get(url)
# 刷新查看登录状态
driver.refresh()
time.sleep(5)
driver.quit()