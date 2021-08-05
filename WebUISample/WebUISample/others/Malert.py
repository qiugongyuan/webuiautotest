from selenium import webdriver
import time

from selenium.webdriver import ActionChains

driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()

link=driver.find_element_by_id('s-usersetting-top').click()
time.sleep(1)
#ActionChains(driver).move_to_element(link).perform()

driver.find_element_by_link_text('搜索设置').click()
driver.find_element_by_link_text('保存设置').click()
time.sleep(2)
driver.switch_to.alert.accept()

driver.quit()