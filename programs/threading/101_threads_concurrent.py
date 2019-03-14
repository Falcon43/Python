import threading

def worker(num):
    for j in range(100):
        print("worker "+str(num) +"  :  "+str(j))
    return


threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()
