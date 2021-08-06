
import threading
from time import ctime, sleep
def super_player(file_,time):
    for i in range(3):
        print('start playing:%s! %s' %(file_,ctime()))
        sleep(time)
lists={'骁':3,'三傻大闹宝莱坞':5}
threads=[]
files=range(len(lists))

for file_,time in lists.items():
    t=threading.Thread(target=super_player,args=(file_,time))
    threads.append(t)




if __name__=='__main__':
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print('all end:',ctime())