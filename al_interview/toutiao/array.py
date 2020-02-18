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


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    solution = Solution()
    print(solution.maxProfit(prices))
