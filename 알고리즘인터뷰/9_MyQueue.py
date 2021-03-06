

class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        self.input.append(x)

    def pop(self):
        self.peek()
        return self.output.pop()

    def peek(self): #리스트 순서 재배열
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())

        return self.output[-1]


    def empty(self):
        return self.input == [] and self.output == []


queue = MyQueue()
queue.push(1)
queue.push(2)
print(queue.peek())
print(queue.pop())
print(queue.empty())