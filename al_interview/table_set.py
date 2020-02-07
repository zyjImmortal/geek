from typing import *


class Solution:
    '''
    给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
    示例 1:
    输入: s = "anagram", t = "nagaram"
    输出: true
    示例 2:
    输入: s = "rat", t = "car"
    输出: false
    说明:
    你可以假设字符串只包含小写字母
    '''

    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def isAnagramV2(self, s: str, t: str) -> bool:
        s_dict, t_dict = {}, {}
        for x in s:
            s_dict[x] = s_dict.get(x, 0) + 1
        for y in t:
            t_dict[y] = t_dict.get(y, 0) + 1
        return s_dict == t_dict

    def two_sum(self, nums, target):
        record = {}
        for index, key in enumerate(nums):
            record[key] = index
        for index, key in enumerate(nums):
            temp = target - key
            if temp in record and index != record.get(temp):
                return [index, record.get(temp)]
        return None

    def twoSum(self, nums, target):
        record = {}
        for index, key in enumerate(nums):
            tem = target - key
            if tem in record:
                return [index, record.get(tem)]
            record[key] = index

    '''
    给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
    注意：答案中不可以包含重复的三元组。
    '''

    def threeSum(self, nums, target):
        if len(nums) < 2:
            return []
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l <= r:
                sum = nums[i] + nums[l] + nums[r]
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    # 这两个循环主要是去重
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    # 去重以后需要把做指针和右指针分别移动一位
                    r -= 1
                    l += 1
        return res
