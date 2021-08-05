from selenium import webdriver
import os,time

driver=webdriver.Chrome()

filepath=''+os.path.abspath('../HT/checkbox.html')
print (filepath)
#方法一
driver.get(filepath)
#方法一
# inputs=driver.find_elements_by_tag_name('input')
# for i in inputs:
#     if i.get_attribute('type')=='checkbox':
#         i.click()
#         time.sleep(1)

checkboxes=driver.find_elements_by_css_selector('input[type=checkbox]')
print (len(checkboxes))
for checkbox in checkboxes:
    checkbox.click()
    time.sleep(1)
driver.find_elements_by_css_selector('input[type=checkbox]').pop().click()
#pop()方法用于获取列表中的一个元素,默认为最后一个元素
driver.quit()