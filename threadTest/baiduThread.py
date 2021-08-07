from threading import Thread
from time import ctime, sleep

from selenium import webdriver

from threadTest.threadsone import threads


def test_baidu(browser, search):
    print('start:%s' % ctime())
    print('browser:%s,' % browser)
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        print("browser 参数有误,只能是Chrome,ff")
    driver.get('http://www.baidu.com')
    driver.find_element_by_id('kw').send_keys(search)
    driver.find_element_by_id('su').click()
    sleep(2)
    driver.quit()


if __name__ == '__main__':
    lists = {'chrome': 'ranran', 'firefox': 'loveranran'}
    threads = []
    files = range(len(lists))

    for browser, search in lists.items():
        t = Thread(target=test_baidu, args=(browser, search))
        threads.append(t)

if __name__ == '__main__':
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print('all end:', ctime())
