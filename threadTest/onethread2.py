from time import ctime, sleep


def music(func,loop):
    for i in range(loop):
        print('I was listening to %s! %s' %(func,ctime()))
        sleep(2)
def movie(func,loop):
    for i in range(loop):
        print('I was at the %s! %s' %(func,ctime()))
        sleep(5)
if __name__=='__main__':
    music('骁',2)
    movie('三傻大闹宝莱坞',2)
    print('all end:',ctime())