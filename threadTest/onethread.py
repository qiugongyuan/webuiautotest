from time import sleep, ctime


def music():
    print('I was listening to music1 %s' % ctime())
    sleep(2)


def movie():
    print('I was at the movies! %s' % ctime())
    sleep(5)


if __name__ == '__main__':
    music()
    movie()
    print('all end:', ctime())
