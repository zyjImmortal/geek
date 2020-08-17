from typing import List


class Solution:
    """

    暴力的递归解法->带备忘录的递归解法->非递归的动态规划解法
    """

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
            dp[i] = max(nums[i], dp[i - 1] + nums[i])

        max_sum = 0
        for sum1 in dp:
            max_sum = max(sum1, max_sum)
        print(dp)
        return max_sum

    def maxProfit(self, prices: List[int]) -> int:
        """
        给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
        如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
        注意：你不能在买入股票前卖出股票
        https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/

        使用穷举：
        伪代码： 所有的可能 = {第x天买，第y天卖}
        0<= x < len(prices)
        x<y<len(prices)
        result = max(所有可能)

        主题思想就是：确定买入，后然后穷举找出最大卖出的价格
        """
        res = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                res = max(res, prices[j] - prices[i])
        return res

    def maxProfitV2(self, prices: List[int]) -> int:
        """穷举买入，寻找买入价格最小的那天
        https://mp.weixin.qq.com/s?__biz=MzAxODQxMDM0Mw==&mid=2247484509&amp;idx=1&amp;
        sn=21ace57f19d996d46e82bd7d806a2e3c&source=41#wechat_redirect
        """
        res = 0
        if len(prices) == 0:
            return 0
        curMin = prices[0]
        for i in range(1, len(prices)):
            curMin = min(curMin, prices[i])
            res = max(res, prices[i] - curMin)
        return res

    def maxProfitV3(self, prices: List[int]) -> int:
        """
        给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
        设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
        注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）
        https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/
        """
        res = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                res = max(res, self.maxProfitV3(prices[j + 1:]) + prices[j] - prices[i])
        return res

    def maxProfitV4(self):
        """
        状态都有哪些
        选择都有那些
        状态如何迁移-->不同的选择
        :return:
        """

if __name__ == '__main__':
    solution = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(solution.maxSubArray(nums))
