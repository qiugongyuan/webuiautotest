from selenium import webdriver
import os,time

driver=webdriver.Chrome()
file_path=''+os.path.abspath('../HT/frame.html')
driver.get(file_path)
driver.maximize_window()
time.sleep(1)
driver.switch_to.frame('if')
driver.find_element_by_link_text('注册/登录').click()
time.sleep(1)
driver.quit()