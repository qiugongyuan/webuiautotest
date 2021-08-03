from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
time.sleep(5)
driver.find_element_by_id("kw").send_keys("ranran")
time.sleep(5)
driver.find_element_by_id("su").click()
driver.quit()