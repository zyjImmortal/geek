from typing import List


class Solution:

    def uniquePaths(self, m: int, n: int) -> int:

        res = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(m):
            res[0][i] = 1
        for j in range(n):
            res[j][0] = 1
        self.helper(m, n, res)
        return res[n - 1][m - 1]

    def helper(self, m, n, res):
        for i in range(1, m):
            for j in range(1, n):
                res[j][i] = res[j - 1][i] + res[j][i - 1]  # 状态迁移方程

    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        给定一个无序的整数数组，找到其中最长上升子序列的长度
        示例:
        输入: [10,9,2,5,3,7,101,18]
        输出: 4
        解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
        说明:

        可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
        你算法的时间复杂度应该为 O(n2)

        状态：子序列长度

        """
        if len(nums) == 0:
            return 0
        dp = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])

        max_value = 1
        for value in dp:
            max_value = max(max_value, value)
        return max_value

    def maxSubArray(self, nums: List[int]) -> int:
        """
        给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和
        :param nums:
        :return:
        """
        if len(nums) == 0:
            return 0

        dp = []

        for i in range(len(nums)):
            dp[i] = max(nums[i], dp[i-1] + nums[i])


        max_sum = 0
        for sum1 in dp:
            max_sum = max(sum1, max_sum)
        print(dp)
        return max_sum

if __name__ == '__main__':
    solution = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(solution.maxSubArray(nums))
