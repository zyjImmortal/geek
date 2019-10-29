import re


class Solution:

    def isPalindrome(self, s: str) -> bool:
        '''
        判断是否是回文字符串

        str.isalnum判断一个字符是不是数字或者字符串，如果不是返回false
        '''
        filter_str = filter(str.isalnum, s)
        new_str = ''.join(filter_str)
        reverse_string = new_str.lower()[::-1]
        if s == reverse_string:
            return True
        else:
            return False

    def mostCommonWord(self, paragraph: str, banned) -> str:
        import re
        record = {}
        strs = re.split('\W', paragraph.lower())
        for key in strs:
            if key not in banned and key != '':
                if key in record:
                    record[key] += 1
                else:
                    record[key] = 0
        return sorted(record.items(), key=lambda x: x[1], reverse=True)[0][0]

    def isValid(self, s: str) -> bool:
        table = {')': '(', ']': '[', '}': '{'}
        stack = []
        for i in s:
            if i in table:
                stack.append(i)
        return len(stack) == 0

    def queue(self):
        # from queue import
        pass

    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == None or s == '':
            return 0
        words = s.split(' ')
        end = len(words) - 1
        while (end >= 0):
            if words[end] != '':
                return len(words[end])
            end -= 1
        return 0

    def lengthOfLastWordV2(self, s):
        import re
        words = re.search(r'\w*', s)
        print(words.groups(0))

    def longestPalindrome(self, s):
        """
        给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000
        :type s: str
        :rtype: str
        """
        pass

    def countSegments(self, s):
        """
        统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。
        请注意，你可以假定字符串里不包括任何不可打印的字符
        :type s: str
        :rtype: int
        """
        # return len(re.search(r'[a-z]+',s).groups())
        return len(s.split())
        # 需要自己过滤一下为空的情况，直接使用s.split()不指定分隔符，会自动把空的移除
        # return len(filter(lambda x: x != '', s.split(' ')))

    def numKLenSubstrNoRepeats(self, S, K):
        """
        给你一个字符串 S，找出所有长度为 K 且不含重复字符的子串，请你返回全部满足要求的子串的 数目
        :type S: str
        :type K: int
        :rtype: int
        """
        length = len(S)
        if length < K:
            return 0
        pre, cur = 0, 1
        pass

    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        
        pass


if __name__ == "__main__":
    soluton = Solution()
    # paragraph = "Bob. hIt, baLl"
    # banned = ["bob", "hit"]
    # print(soluton.mostCommonWord(paragraph, banned))
    s = "ass Adsf "
    print(soluton.countSegments(s))
