import collections


class Mystack:
    def __init__(self):
        self.q = collections.deque()

    def push(self, num: int):
        self.q.append(num)
        print(self.q)
        for _ in range(len(self.q) -1):
            self.q.append(self.q.popleft())
    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0

stack = Mystack()
print(stack.push(2))
print(stack.push(3))
print(stack.push(1))

print(stack.top())
print(stack.pop())
print(stack.empty())