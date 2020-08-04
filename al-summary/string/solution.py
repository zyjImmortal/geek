from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。'''
        if len(s) < 2:
            return len(s)

        res = 0
        record = {}  # 记录每个字符的索引
        i = 0  # 无重复子串头部指针位置
        for j in range(len(s)):
            if record.get(s[j]):
                # 如果存在重复字符，更新头部指针位置，这个要取最大值，防止发生左移的情况
                i = max(record.get(s[j]), i)
            res = max(res, j - i + 1)
            record[s[j]] = j + 1
        return res

    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        '''给定一个字符串 s ，找出 至多 包含两个不同字符的最长子串 t '''
        if len(s) < 2:
            return len(s)
        res = 0
        record = set()
        i = 0
        for j in range(len(s)):
            record.add(s[j])
            if len(record) > 2:
                i = j
            res = max(res, j - i + 1)

        return res

    def isPalindrome(self, s: str) -> bool:
        '''给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写'''
        length = len(s)
        for i in range(length // 2):
            if s[i] != s[length - i - 1]:
                return False
        return True

    def dplongestPalindrome(self, s):
        '''动态规划实现'''
        size = len(s)
        if size < 2:
            return s

        dp = [[False for _ in range(size)] for _ in range(size)]
        max_length = 1
        start = 0
        for j in range(1, size):
            for i in range(j):  # 内层循环控制start指针
                if s[i] == s[j]:
                    if j - i < 3:  # i + 1 - (j - 1) < 2
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]  # 状态转移方程
                else:
                    dp[i][j] = False

                if dp[i][j]:
                    if j - i + 1 > max_length:
                        start = i
                        max_length = max(max_length, j - i + 1)
        return s[start:start + max_length]

    def longestPalindrome(self, s: str) -> str:
        '''给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000'''
        ans = ''
        length = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if self.isPalindrome(s[i:j]) and len(s[i:j]) > length:
                    ans = s[i:j]
                    length = max(len(ans), length)
        return ans

    def minWindow(self, s: str, t: str) -> str:
        '''给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串'''
        window, needs = {}, Counter(t)
        start = left = right = match = 0

        min_len = size = len(s)
        if size < len(t):
            return ''

        while right < size:
            tmp = s[right]
            if tmp in needs:
                window[tmp] = window.get(tmp, 0) + 1
                if needs[tmp] == window[tmp]:
                    match += 1
            right += 1

            while match == len(needs):

                if right - left < min_len:
                    start = left
                    min_len = right - left

                char = s[left]
                if char in needs:
                    window[char] -= 1
                    if needs[char] > window[char]:
                        match -= 1
                left += 1

        return s[start:start + min_len]

    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
           换句话说，第一个字符串的排列之一是第二个字符串的子串
        '''
        if len(s2) < len(s1):
            return False
        window, record = {}, Counter(s1)
        left = right = 0
        size = len(s2)
        while right < size:
            char = s2[right]
            if record.get(char, 0) > window.get(char, 0):
                window[char] = window.get(char, 0) + 1
                right += 1
            else:
                window.clear()
                right  = left + 1
                left = right
            if window == record:
                return True
        return False

    def is_valid(self, str):
        table = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        tuple


if __name__ == '__main__':
    solution = Solution()
    s = 'adb'
    t = 'dbda'
    print(solution.checkInclusion(s,t))
