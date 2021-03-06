
from typing import List

class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        '''生成合法括号组合的数量
            回溯算法实现
        '''
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

if __name__ == '__main__':
    solution = Solution()
    print(solution.generateParenthesis(3))