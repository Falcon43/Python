class Queue:
    def __init__(self):
        self.queue = []

    def size(self):
        return len(self.queue)

    def isempty(self):
        return self.size() == 0



    def enqueue(self,val):
        self.queue.insert(0,val)


    def dequeue(self):
        if self.isempty():
            return None
        else:
           return self.queue.pop()

    def print_Queue(self):
        print("Queue :  "+str(self.queue))

    def peak(self):
        print("Peak :  "+self.queue[0])




bucket_queue = Queue()

bucket_queue.print_Queue()
print("Your bucket stack is Empty? "+str(bucket_queue.isempty()))
bucket_queue.enqueue("Victoria Falls")
print("Size:  "+str(bucket_queue.size()))
bucket_queue.print_Queue()
print("Your bucket stack is Empty? "+str(bucket_queue.isempty()))
bucket_queue.dequeue()
bucket_queue.dequeue()
print("Size:  "+str(bucket_queue.size()))
bucket_queue.print_Queue()
bucket_queue.enqueue("Bora Bora")
bucket_queue.enqueue("Kauai, Hawaii")
bucket_queue.enqueue("Longsheng")
bucket_queue.enqueue("Amazon River")
bucket_queue.enqueue("Rainbow Mountains of Zhangye Danxia, China")
bucket_queue.enqueue("Railay, Thailand ")
bucket_queue.enqueue("Neuschwanstein")
bucket_queue.enqueue("Aurora - Iceland")
bucket_queue.enqueue("Antarctica")
bucket_queue.enqueue("Yellowstone National Park")
bucket_queue.enqueue("Petra, Jordan")
print("Size:  "+str(bucket_queue.size()))
bucket_queue.print_Queue()
bucket_queue.peak()
bucket_queue.dequeue()
bucket_queue.dequeue()
bucket_queue.dequeue()
print("Size:  " + str(bucket_queue.size()))
bucket_queue.print_Queue()
bucket_queue.peak()
bucket_queue.dequeue()
bucket_queue.dequeue()
bucket_queue.dequeue()
print("Size:  " + str(bucket_queue.size()))
bucket_queue.print_Queue()
bucket_queue.peak()



"""

Output:



Queue :  []
Your bucket stack is Empty? True
Size:  1
Queue :  ['Victoria Falls']
Your bucket stack is Empty? False
Size:  0
Queue :  []
Size:  11
Queue :  ['Petra, Jordan', 'Yellowstone National Park', 'Antarctica', 'Aurora - Iceland', 'Neuschwanstein', 'Railay, Thailand ', 'Rainbow Mountains of Zhangye Danxia, China', 'Amazon River', 'Longsheng', 'Kauai, Hawaii', 'Bora Bora']
Peak :  Petra, Jordan
Size:  8
Queue :  ['Petra, Jordan', 'Yellowstone National Park', 'Antarctica', 'Aurora - Iceland', 'Neuschwanstein', 'Railay, Thailand ', 'Rainbow Mountains of Zhangye Danxia, China', 'Amazon River']
Peak :  Petra, Jordan
Size:  5
Queue :  ['Petra, Jordan', 'Yellowstone National Park', 'Antarctica', 'Aurora - Iceland', 'Neuschwanstein']
Peak :  Petra, Jordan



"""