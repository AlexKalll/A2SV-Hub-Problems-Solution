# Problem: Implement Stack using Queues - https://leetcode.com/problems/implement-stack-using-queues/

class MyStack:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        if self.queue1:
            self.queue1.append(x)
        elif self.queue2:
            self.queue2.append(x)
        else:
            self.queue1.append(x)

    def pop(self) -> int:
        while self.queue1:
            if len(self.queue1) == 1:
                return self.queue1.pop(0)
            else:
                self.queue2.append(self.queue1.pop(0))
        while self.queue2:
            if len(self.queue2) == 1:
                return self.queue2.pop(0)
            else:
                self.queue1.append(self.queue2.pop(0))


    def top(self) -> int:
        while self.queue1:
            if len(self.queue1) == 1:
                self.queue2.append(self.queue1[0])
                return self.queue1.pop(0)
            else:
                self.queue2.append(self.queue1.pop(0))
        while self.queue2:
            if len(self.queue2) == 1:
                self.queue1.append(self.queue2[0])
                return self.queue2.pop(0)
            else:
                self.queue1.append(self.queue2.pop(0))

    def empty(self) -> bool:
        if not self.queue1 and not self.queue2:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()