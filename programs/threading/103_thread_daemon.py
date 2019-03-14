import threading
import time

def queue1():
    while True:
        print("Heartbeat   -%s Thread" %threading.current_thread().getName())
        time.sleep(1)


def queue2():
    print("Starting  "+threading.current_thread().getName())
    time.sleep(5)
    print("Ending  "+threading.current_thread().getName())


q1 = threading.Thread(name='daemon', target=queue1)
q1.setDaemon(True)
q2 = threading.Thread(name='non-daemon', target=queue2)



q1.start()
q2.start()

