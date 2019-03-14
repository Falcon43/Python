import threading
import time
import random



# Custom thread object
class custThread(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        getTime(self.name)
        print("Thread ",self.name," Execution Ends ")




def getTime(name):
    print("Thread {} sleeps at {}".format(name, time.strftime("%H:%M:%S", time.gmtime())))
    randSleepTime = random.randint(1, 5)
    time.sleep(randSleepTime)
    print("Thread {} wakes at {}".format(name, time.strftime("%H:%M:%S", time.gmtime())))



thread1 = custThread("1")
thread2 = custThread("2")
thread3 = custThread("3")

thread1.start()
thread2.start()
thread3.start()

print("Thread 1 alive: : ", thread1.isAlive())
print("Thread 2 alive: : ", thread2.isAlive())
print("Thread 3 alive: : ", thread3.isAlive())

print("Thread 1 name : ", thread1.getName())


thread1.join()      # waits untill thread1 completes and then only starts main thread

#time.sleep(10)
print("Thread 1 alive: : ", thread1.isAlive())
print("Thread 2 alive: : ", thread2.isAlive())
print("Thread 3 alive: : ", thread3.isAlive())

"""
# non-custom thread object



def executeThread(i):
    print("Thread {} sleeps at {}".format(i,time.strftime("%H:%M:%S" ,time.gmtime())))
    randSleepTime = random.randint(1,5)
    time.sleep(randSleepTime)
    print("Thread {} wakes at {}".format(i, time.strftime("%H:%M:%S", time.gmtime())))




for i in range(10):
    t = threading.Thread(target=executeThread, args=(i,))       # thread object
    t.start()
    print("Active threads: ",threading.active_count())
    print("Thread objects: ",threading.enumerate())
"""
