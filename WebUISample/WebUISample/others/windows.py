from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()

search_windows=driver.current_window_handle

driver.find_element_by_link_text('登录').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="passport-login-pop-dialog"]/div/div/div/div[3]/a').click()

all_handles=driver.window_handles

for handle in all_handles:
    if handle!=search_windows:
        driver.switch_to.window(handle)
        print('now register window!')
        driver.find_element_by_name('userName').send_keys('ranran')
        driver.find_element_by_name('phone').send_keys('1234')
        time.sleep(1)
for handle in all_handles:
    if handle==search_windows:
        driver.switch_to.window(handle)
        print('now search window!')
        driver.find_element_by_id('TANGRAM__PSP_4__closeBtn').click()
        driver.find_element_by_id('kw').send_keys('ranran')
        driver.find_element_by_id('su').click()
        time.sleep(1)
driver.quit()