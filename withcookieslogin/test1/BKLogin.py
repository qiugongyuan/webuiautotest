import time,os

import yaml
from selenium import webdriver
url = 'https://account.cnblogs.com/signin'
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
cookiebefore=driver.get_cookies()
fileNamePath = os.path.split(os.path.realpath(__file__))[0]
yamlPath1 = os.path.join(fileNamePath, 'config3.yaml')
# 以覆盖写入打开文件
fw = open(yamlPath1,'w',encoding='utf-8')
data3={"cookiesbefore":cookiebefore}
yaml.dump(data3,fw)

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
len1 = len(cookiesAfter)
# 已经知道需要第几个cookie，这里需要第3个cookie，所以选择cookie下标为2
cookie1 = cookiesAfter[2]
# 获取当前文件所在路径
fileNamePath = os.path.split(os.path.realpath(__file__))[0]
# 拼接config.yaml文件绝对路径
yamlPath1 = os.path.join(fileNamePath, 'config1.yaml')
# 以覆盖写入打开文件
fw = open(yamlPath1,'w',encoding='utf-8')
data1={"cookiesAfter":cookiesAfter}
yaml.dump(data1,fw)

yamlPath2=os.path.join(fileNamePath, 'config2.yaml')
fw=open(yamlPath2,'w',encoding='utf-8')
# 构建数据
data2= {"cookie1":cookie1}
# 装载写入yaml文件。
yaml.dump(data2,fw)

driver.quit()