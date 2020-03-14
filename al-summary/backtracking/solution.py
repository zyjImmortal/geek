
from typing import List

class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        '''生成有效括号'''
        ans = []

        def backtrack(S='', left=0, right=0):
            # 结束条件
            if len(S) == 2 * n:
                ans.append(S)
                return

            if left < n:
                backtrack(S + '(', left + 1, right)
            if right < left:
                backtrack(S + ')', left, right + 1)

        backtrack()
        return ans

    def permute(self, nums: List[int]) -> List[List[int]]:
        '''给定一个没有重复数字的序列，返回其所有可能的全排列'''
        res = []
        self.back(nums, [], res)
        return res

    def back(self, nums, track, res):
        if len(track) == len(nums):
            res.append(track[:])
            return

        for i in nums:
            # if i in track:
            #     continue
            track.append(i)
            self.back(nums, track, res)
            track.pop()



if __name__ == '__main__':
    solution = Solution()
    print(solution.permute([1,1,2]))