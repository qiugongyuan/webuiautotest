
from selenium import webdriver


def insert_img(driver, file_name):
    file_path = "D:\\qgy work\\python project\\selenium\\jforumTest\\bbs\\report\\image\\" + file_name

    print(file_path)
    driver.get_screenshot_as_file(file_path)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')
    insert_img(driver, 'baidu.png')
    driver.quit()
