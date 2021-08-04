from selenium import webdriver
from public import Login

driver = webdriver.Chrome()
driver.get('http://localhost:8080/jforum-2.1.9/user/login.page')

driver.implicitly_wait(2)
Login().user_login(driver)
driver.implicitly_wait(2)
Login().user_logout(driver)
