from selenium.webdriver import Remote


def browser():
    driver = Remote(command_executor='http://127.0.0.1:4444/wd/hub',
                    desired_capabilities={'platform': 'ANY',
                                          'browserName': 'chrome',
                                          'version': '',
                                          'javascriptEnabled': True})
    return driver


if __name__ == '__main__':
    dr = browser()
    dr.get("http://www.baidu.com")
    dr.quit()
