from threading import Thread
from time import ctime, sleep

from selenium import webdriver

from threadTest.threadsone import threads
from selenium.webdriver import Remote


def test_baidu(host, browser):
    print('start:%s' % ctime())
    print(host, browser)
    dc = {'browserName': browser}

    driver = webdriver.Remote(command_executor=host, desired_capabilities=dc)
    driver.get('http://www.baidu.com')
    driver.find_element_by_id('kw').send_keys(browser)
    driver.find_element_by_id('su').click()
    sleep(2)
    driver.close()


if __name__ == '__main__':
    lists = {'http://127.0.0.1:4444/wd/hub': 'chrome',
             'http://127.0.0.1:4445/wd/hub': 'firefox' }
    threads = []
    files = range(len(lists))

    for host, browser in lists.items():
        t = Thread(target=test_baidu, args=(host,browser))
        #注意不要将host,browser顺序填写错误
        threads.append(t)

if __name__ == '__main__':
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print('all end:', ctime())
