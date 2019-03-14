import threading
import time

def queue1():
    print("Starting  "+threading.current_thread().getName())
    time.sleep(10)
    print("Ending  "+threading.current_thread().getName())


def queue2():
    print("Starting  "+threading.current_thread().getName())
    time.sleep(2)
    print("Ending  "+threading.current_thread().getName())


q1 = threading.Thread(name='Long Queue', target=queue1)
q2 = threading.Thread(name='Short Queue', target=queue2)
q3 = threading.Thread(target=queue1)    # use default name


q1.start()
q2.start()
q3.start()
