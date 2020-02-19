from typing import *


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
        如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
        注意你不能在买入股票前卖出股票
        :param prices:
        :return:
        '''
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                diff = prices[j] - prices[i]
                if diff > max_profit:
                    max_profit = diff
        return max_profit

    def maxProfitV2(self, prices: List[int]) -> int:
        '''
        动态规划 前i天的最大收益 = max{前i-1天的最大收益，第i天的价格-前i-1天中的最小价格}
        :param prices:
        :return:
        '''
        if len(prices) < 2:
            return 0
        max_profit = 0
        min_value = prices[0]
        for i in range(len(prices)):
            min_value = min(min_value, prices[i])
            max_profit = max(max_profit, prices[i] - min_value)
            # if prices[i] < min_value:
            #     min_value = prices[i]
            # elif (prices[i] - min_value) > max_profit:
            #     max_profit = prices[i] - min_value
        return max_profit

    def maxProfitV3(self, prices: List[int]) -> int:
        """贪心算法"""
        if len(prices) < 2:
            return 0
        sum = 0
        for i in range(1, len(prices)):
            j = i - 1
            if prices[i] > prices[j]:
                sum += prices[i] - prices[j]
        return sum

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """给定两个数组，编写一个函数来计算它们的交集
            说明:
            输出结果中的每个元素一定是唯一的。
            我们可以不考虑输出结果的顺序
        """
        l1, l2 = len(nums1), len(nums2)
        if l1 == 0 or l2 == 0:
            return []
        result = []
        if l1 >= l2:
            for i in range(l2):
                if nums2[i] in nums1:
                    result.add(nums2[i])
        if l1 < l2:
            for i in range(l1):
                if nums1[i] in nums2:
                    result.add(nums1[i])
        return result

    def intersectionV2(self, nums1: List[int], nums2: List[int]) -> List[int]:

        return list(set(nums1) & set(nums2))

    def intersectionV3(self, nums1: List[int], nums2: List[int]) -> List[int]:
        tab = {}
        rs = []
        for num in nums1:
            tab[num] = 1
        for num in nums2:
            if num in tab:
                rs.append(num)
        return rs

    """
    给定两个数组，编写一个函数来计算它们的交集。
    示例 1:
    输入: nums1 = [1,2,2,1], nums2 = [2,2]
    输出: [2,2]
    示例 2:
    输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    输出: [4,9]
    说明： 
    输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
    我们可以不考虑输出结果的顺序。
    进阶: 
    如果给定的数组已经排好序呢？你将如何优化你的算法？
    如果 nums1 的大小比 nums2 小很多，哪种方法更优？
    如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
    """
if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    solution = Solution()
    print(solution.maxProfitV3(prices))
