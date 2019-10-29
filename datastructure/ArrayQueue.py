class ArrayQueue:
    """
    顺序队列，队尾插入元素，对头取出元素
    """

    def __init__(self):
        self.items = []
        self.head = 0
        self.tail = 0

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        """
        入队
        :param item:
        :return:
        """
        self.items.append(item)
        self.tail += 1
        return True

    def dequeue(self):
        """
        出队
        :return:
        """
        if self.head == self.tail:
            return False
        self.tail += 1
        return self.items.pop(self.head)

    def __str__(self):
        return '[' + ','.join(self.items) + ']'

if __name__ == '__main__':
    queue = ArrayQueue()
    queue.enqueue(4)
    queue.enqueue(3)
    queue.enqueue(8)
    queue.enqueue(1)
    print(queue)