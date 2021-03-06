
class MyCircleQueue:
    def __init__(self, size):
        self.q = [None] * size
        self.max_len = size
        self.p1 = 0
        self.p2 = 0

    def enQueue(self, num)-> bool:
        if self.q[self.p2] is None:
            self.q[self.p2] = num
            self.p2 = (self.p2 + 1 ) % self.max_len
            return True
        else:
            return False

    def deQueue(self) -> bool:

        if self.q[self.p1] is None:
            return False
        else:
            self.q[self.p1] = None
            self.p1 = (self.p1 +1) %self.max_len
            return True

    def Front(self)-> int:
        return -1 if self.q[self.p1] is None else self.q[self.p1]

    def Rear(self)-> int:
        return -1 if self.q[self.p2-1] is None else self.q[self.p2-1]

    def isEmpty(self) ->bool:
        return self.p1 == self.p2 and self.q[self.p1] is None

    def isFull(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is not None


circleQueue = MyCircleQueue(5)
circleQueue.enQueue(10)
circleQueue.enQueue(20)
print(circleQueue.Rear())
print(circleQueue.Front())