class MaxStack:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        if len(self.stack2) == 0 or self.stack2[len(self.stack2) - 1] < x:
            self.stack2.append(x)
        self.stack1.append(x)

    def pop(self) -> int:
        if self.stack1[len(self.stack1) - 1] == self.stack2[len(self.stack2) - 1]:
            self.stack2.pop()
        return self.stack1.pop()

    def top(self) -> int:
        return self.stack1[len(self.stack1) - 1]

    def peekMax(self) -> int:
        size = len(self.stack2)
        if size == 0:
            return -1
        return self.stack2[size - 1]

    def popMax(self) -> int:
        max_ele = self.stack2.pop()
        for i in range(len(self.stack1) - 1, -1):
            if self.stack1[i] == max_ele:
                return self.stack1.pop(i)
