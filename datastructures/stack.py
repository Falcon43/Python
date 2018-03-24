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
           return self.stack[-1]

