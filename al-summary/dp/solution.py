class Solution:

    def uniquePaths(self, m: int, n: int) -> int:

        res = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(m):
            res[0][i] = 1
        for j in range(n):
            res[j][0] = 1
        self.helper(m, n, res)
        return res[n-1][m-1]

    def helper(self, m, n, res):
        for i in range(1, m):
            for j in range(1, n):
                res[j][i] = res[j-1][i] + res[j][i-1]  # 状态迁移方程




if __name__ == '__main__':
    solution = Solution()
    print(solution.uniquePaths(3, 2))
