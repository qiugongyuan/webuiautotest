from time import sleep

from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://videojs.com")
driver.maximize_window()
driver.find_element_by_id('vjs_video_3').click()
sleep(10)
driver.quit()
