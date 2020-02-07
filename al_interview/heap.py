from typing import *
import heapq


class Solution:

    def kLargest(self):
        '''返回数据流中第k大元素'''
        pass


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = heapq.nlargest(k, nums)
        heapq.heapify(self.nums)

    def add(self, val: int) -> int:
        heapq.heappushpop(self.nums, val)
        return self.nums[0]


largest = KthLargest(3, [4,5,8,2])
print(largest.add(3))
print(largest.add(5))
print(largest.add(10))
print(largest.add(9))
print(largest.add(4))