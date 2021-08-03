# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
time.sleep(5)
#driver.set_window_size(960,800)
#设置浏览器大小 宽960 高800
#time.sleep(5)

#右击操作
right_click=driver.find_element_by_link_text('地图')
ActionChains(driver).context_click(right_click).perform()
time.sleep(2)

#鼠标悬停操作
above=driver.find_element_by_link_text('直播')
ActionChains(driver).move_to_element(above).perform()
time.sleep(2)

#获得输入框的尺寸
size=driver.find_element_by_id('kw').size
print(size)


driver.find_element_by_id("kw").send_keys("ranran")
driver.maximize_window()
time.sleep(5)
driver.find_element_by_id("su").click()

#鼠标双击操作
double_click=driver.find_element_by_link_text('百度首页')
ActionChains(driver).double_click(double_click).perform()
time.sleep(2)

driver.refresh()#刷新当前页面
driver.quit()