"""
Implement a queue with two stacks
"""

class QueuewithStacks:
    def __init__(self):
        self.inbox = []
        self.outbox = []

    def enqueue(self, val):
        if not len(self.outbox) == 0:
            for i in range(len(self.outbox)):
                self.inbox.append(self.outbox.pop())
        if len(self.outbox) == 0:
            return self.inbox.append(val)


    def dequeue(self):
        if not len(self.inbox) == 0:
            for j in range(len(self.inbox)):
                self.outbox.append(self.inbox.pop())
        if len(self.inbox) == 0:
            if not len(self.outbox) == 0:
                return self.outbox.pop()
            else:
                return None


    def print_queue(self):
        if not len(self.inbox) == 0:
            print(self.inbox)
        if not len(self.outbox) == 0:
            self.outbox.reverse()
            print(self.outbox)
            self.outbox.reverse()
        if len(self.inbox) == 0  and  len(self.outbox) == 0:
            print("Queue empty")



q = QueuewithStacks()

q.print_queue()
q.dequeue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.enqueue("D")
q.print_queue()
q.dequeue()
q.print_queue()
q.dequeue()
q.print_queue()
q.enqueue("E")
q.print_queue()

