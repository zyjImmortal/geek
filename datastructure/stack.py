class ArrayStack:

    def __init__(self):
        self.items = []
        self.count = 0

    def push(self, item):
        self.items.insert(0, item)
        self.count += 1

    def pop(self):
        if self.count == 0:
            return None
        return self.items.pop(0)
