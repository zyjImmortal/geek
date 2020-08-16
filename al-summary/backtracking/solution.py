from typing import List


class Solution:

    def __init__(self):
        self.res = []

    def generateParenthesisV2(self, n: int) -> List[str]:
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
        """
        回溯算法的框架：
        result = []
        def backtrack(路径, 选择列表):
            if 满足结束条件:
                result.add(路径)
                return

            for 选择 in 选择列表:
                做选择
                backtrack(路径, 选择列表)
                撤销选择
        :param nums:
        :param track:
        :param res:
        :return:
        """
        if len(track) == len(nums):
            res.append(track[:])
            return

        for i in nums:
            # if i in track:
            #     continue
            track.append(i)
            self.back(nums, track, res)
            track.pop()

    def solveNQueens(self, n: int):
        """
        给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
        每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位

        :param n:
        :return:
        """
        board = [['.'] * n for _ in range(n)]
        print(board)
        self.queen_back_tack(board, 0)
        return self.res

    def queen_back_tack(self, board, row):
        """"""
        if row == len(board):
            tmp_list = []  # 二维变一维添加到res中
            for e_row in board:
                tmp = ''.join(e_row)
                tmp_list.append(tmp)
            # res.append(tmp_list)
            self.res.append(tmp_list)
            return
        n = len(board[row])
        for col in range(n):
            if not self.queen_is_valid(board, row, col):
                continue
            board[row][col] = 'Q'
            self.queen_back_tack(board, row + 1)
            board[row][col] = '.'

    def queen_is_valid(self, board, row, col):
        """
        校验要插入的位置是否满足要求
        未遍历到的不用考虑
        :return:
        """
        n = len(board)
        # 列
        for i in range(n):
            if board[i][col] == 'Q':
                return False
        # 右上方
        # for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
        #     if board[i][j] == 'Q':
        #         return False
        # 左上方
        # for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        #     if board[i][j] == 'Q':
        #         return False
        r_row, r_col = row, col
        while r_row > 0 and r_col < n - 1:
            r_row -= 1
            r_col += 1
            if board[r_row][r_col] == 'Q':
                return False
        # 检查左上方是否有皇后互相冲突
        l_row, l_col = row, col
        while l_row > 0 and l_col > 0:
            l_row -= 1
            l_col -= 1
            if board[l_row][l_col] == 'Q':
                return False
        return True

    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）
        说明：解集不能包含重复的子集
        :param nums:
        :return:
        """
        res = []
        track = []

        def backtrack(track, start, nums):
            # from copy import deepcopy
            res.append(track[:])
            for i in range(start, len(nums)):
                track.append(nums[i])
                backtrack(track, i + 1, nums)
                track.pop()

        backtrack(track, 0, nums)
        return res

    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []
        track = []

        def backtrack(start, track):
            if len(track) == k:
                res.append(track[:])
                return
            for i in range(start, n + 1):
                if i in track:
                    continue
                track.append(i)
                # 做完选择穷举下一个位置，通过递归不断地穷举所有的可能性，然后在通过一些条件判断，到达某种状况下，是否符合要求，如果符合就添加到结果当中
                # 选择列表。，选择--是否需要满足条件才能做选择，不满足就跳过，进行下一轮选择，，选择完了递归
                backtrack(i + 1, track)
                track.pop()

        backtrack(1, track)
        return res

    def generateParenthesis(self, n: int) -> List[str]:
        """
        数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合
        https://leetcode-cn.com/problems/generate-parentheses/

        可以先找出特点，有效的括号组合具备什么样的条件：

        1、一个合法括号组合一定是左括号的数量等于右括号的数量
        2、对于一个合法的括号字符串组合p，必然对于任何0 <= i < len(p)都有：子串p[0..i]中左括号的数量都大于或等于右括号的数量
        因为从左往右算的话，肯定是左括号多嘛，到最后左右括号数量相等，说明这个括号组合是合法的
        :param n:
        :return:
        """

        track = []
        res = []

        # def backtrackV2(n, i, track):
        #     if i == 2 * n:
        #         res.append(track)
        #         return
        #
        #     for chioc in ['(', ')']:
        #         track.append(chioc)
        #         backtrack(n, i+1, track)
        #         track.pop()
        track = []
        res = []

        def backtrack(left, right, track, res):
            if right < left:
                return
            if left < 0 or right < 0:
                return
            if left == 0 and right == 0:
                res.append(''.join(track[:]))
                return

            track.append('(')
            backtrack(left - 1, right, track, res)
            track.pop()

            track.append(')')
            backtrack(left, right - 1, track, res)
            track.pop()

        backtrack(n, n, track, res)
        return res

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        给定一个数组 candidates 和一个目标数 target ，
        找出 candidates 中所有可以使数字和为 target 的组合。
        candidates 中的每个数字在每个组合中只能使用一次。
        说明：
        所有数字（包括目标数）都是正整数。
        解集不能包含重复的组合
        :param candidates:
        :param target:
        :return:
        candidates = [10,1,2,7,6,1,5], target = 8,

        在做不同选择的时候，同层之间可能会出现相同的数字
        """

        def backtrack(residue, track, start):
            if residue == 0:
                res.append(track[:])
                return
            for i in range(start, len(candidates)):  # 遍历选择列表，每个选择都代表一个分支
                if candidates[i] > residue:
                    break
                # i 大于start就代表的是不同的分支，candidates[i] == candidates[i - 1]不同分支的根元素
                # 就是剪掉以candidates[i]为根元素的分支
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                track.append(candidates[i])
                backtrack(residue - candidates[i], track, i + 1)
                track.pop()

        track = []
        res = []
        candidates.sort()
        backtrack(target, track, 0)
        return res

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        pass


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3]
    print(solution.generateParenthesis(3))
