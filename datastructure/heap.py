class Heap:
    def __init__(self):
        self.data = [0]
        self.count = 0

    @classmethod
    def swap(nums, x, y):
        nums[x], nums[y] = nums[y], nums[x]

    def insert(self, value):
        self.count += 1
        self.data.insert(self.count,value)
        i = self.count
        while i / 2 > 0 and self.data[i // 2] < self.data[i]:
            self.data[i], self.data[i // 2] = self.data[i // 2], self.data[i]
            i = i // 2

    def heapify(self,nums,):
        pass

    def printHeap(self):
        for i in self.data:
            print(i)

if __name__ == '__main__':
    heap = Heap()
    heap.insert(4)
    heap.insert(5)
    heap.insert(6)
    heap.printHeap()
