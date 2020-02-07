class Solution:

    def isValid(self, s):
        stack = []
        # 右括号放到前面
        paren_map = {')': '(', '}': '{', ']': '['}
        for c in s:
            # 如果不是右括号就入栈
            if c not in paren_map:
                stack.append(c)
            # 如果栈为空或者，发生不匹配的情况，就直接返回false
            elif not stack or paren_map[c] != stack.pop():
                return False
        # 栈为空说明s是否要去的字符串
        return not stack

    def maxSlidingWindowV1(self, nums, k):
        '''暴力求解法，每次窗口滑动后都扫描一遍窗口的最大值'''
        if not nums: return []

        window, res = [], []
        for i in nums:
            # 当窗口的元素小于k的时候，先不求最大值，当元素个数等于k的时候再求
            if len(window) < k:
                window.append(i)
            else:
                # 求当前窗口的最大值
                res.append(max(window))
                # 滑动，删除窗口第一个元素，并在窗后最后添加新元素
                window.pop(0)
                window.append(i)
        # 最后一次滑动后，在循环中不会再求最大值，所以要单独对最后一次滑动后的窗口求最大值
        res.append(max(window))
        return res

    def maxSlidingWindowV2(self, nums, k):
        if not nums: return []
        res = []
        for i in range(len(nums) - k + 1):
            res.append(max(nums[i:i + k]))
        return res

    def maxSlidingWindowV3(self, nums, k):
        pass

    def maxSlidingWindow(self, nums, k):
        '''
        思路：为什么是双端队列，
        双端队列的特点是从两端操作时间复杂度都是O(1)
        目的是通过维护一个队列，这个队列作为窗口，使得窗口(双端队列)的最左端始终是窗口内所有元素的最大值，
        取最大值的时候，直接从队列的开始位置取就可以。
        新进来的元素如果比最大值大，那么就把前面打的元素全部删除掉
        :param nums:
        :param k:
        :return:
        '''
        if not nums: return []
        # window 存储的是下标
        window, res = [], []
        for i, x in enumerate(nums):
            # i-k是窗口滑动后的左边的索引，如果实际存储的索引小于滑动后的索引，就要将开头对的元素删除掉了
            # 要维持窗口中只有k个元素
            if i >= k and window[0] <= i - k:
                window.pop(0)
            # 窗口中小于新元素x的都删除掉
            while window and nums[window[-1]] < x:
                window.pop()
            window.append(i)
            # 获取当前窗口最大值
            if i >= k - 1:
                res.append(nums[window[0]])
        return res


class MyQueue:

    def __init__(self):
        self._in_stack = []
        self._out_stack = []

    def push(self, x: int) -> None:
        self._in_stack.append(x)

    def _move(self):
        # if len(self._out_stack) == 0:
        #     if len(self._in_stack) == 0:
        #         return -1
        #     else:
        #         while len(self._in_stack) != 0:
        #             x = self._in_stack.pop()
        #             self._out_stack.append(x)
        if not self._out_stack:
            while self._in_stack:
                self._out_stack.append(self._in_stack.pop())

    def pop(self) -> int:
        self._move()
        return self._out_stack.pop()

    def peek(self) -> int:
        self._move()
        # return self._out_stack[len(self._out_stack) - 1]
        return self._out_stack[-1]

    def empty(self):
        return not self._in_stack and not self._out_stack


obj = MyQueue()
obj.push(1)
obj.push(2)
print(obj.peek())
obj.pop()
obj.pop()
print(len(obj._in_stack))
print(len(obj._out_stack))
print(obj.empty())
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
#
# print(param_2,param_3,param_4)
