class Stack:
    def __init__(self):
        self.stack = []


    def push(self,val):
        self.stack.append(val)

    def pop(self):
        if self.isempty():
            return None
        else:
            self.stack.pop()

    def print_stack(self):
        print(self.stack)

    def size(self):
        return len(self.stack)

    def isempty(self):
        return self.size() == 0

    def peak(self):
        if self.isempty():
            return None
        else:
           print(self.stack[-1])



bucket_stack = Stack()

bucket_stack.print_stack()
print("Your bucket stack is Empty? "+str(bucket_stack.isempty()))
bucket_stack.push("Victoria Falls")
bucket_stack.print_stack()
print("Your bucket stack is Empty? "+str(bucket_stack.isempty()))
bucket_stack.pop()
bucket_stack.pop()
bucket_stack.print_stack()
bucket_stack.push("Bora Bora")
bucket_stack.push("Kauai, Hawaii")
bucket_stack.push("Longsheng")
bucket_stack.push("Amazon River")
bucket_stack.push("Rainbow Mountains of Zhangye Danxia, China")
bucket_stack.push("Railay, Thailand ")
bucket_stack.push("Neuschwanstein")
bucket_stack.push("Aurora - Iceland")
bucket_stack.push("Antarctica")
bucket_stack.push("Yellowstone National Park")
bucket_stack.push("Petra, Jordan")

bucket_stack.print_stack()
bucket_stack.peak()