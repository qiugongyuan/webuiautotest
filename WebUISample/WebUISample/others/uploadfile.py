from selenium import webdriver
import os,time

driver=webdriver.Chrome()
file_path=''+os.path.abspath('../HT/Upfile.html')
driver.get(file_path)
driver.maximize_window()
time.sleep(1)

driver.find_element_by_name('file').send_keys('D:\\qgy work\\jmeter learning\\users.txt')
time.sleep(2)
text='ranran lovely'
js="var sum=document.getElementById('text id');sum.value='"+text+"';"
driver.execute_script(js)
time.sleep(3)
driver.quit()