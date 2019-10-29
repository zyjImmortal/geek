from typing import List
import itertools


class Solution:
    def removeDuplicates(self, nums) -> int:
        length = len(nums)
        if length < 2:
            return length
        pre, cur = 0, 1
        while cur < length:
            if nums[cur] == nums[pre]:
                nums.pop(pre)
            else:
                pre += 1
                cur += 1
            length = len(nums)
        return length

    def search(self, nums, target):
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi = mid - 1
            elif nums[mid] < target:
                lo = mid + 1
        return -1

    def searchRange(self, nums, target: int):
        start = self.search(nums, target)
        if start != -1:
            end = self.search(nums[start + 1:], target)
            if end != -1:
                return [start, end]
        return [-1, -1]

    def searchRangeV2(self, nums, target):
        """
                :type nums: List[int]
                :type target: int
                :rtype: List[int]
                """
        res = [-1, -1]
        if not nums or target == None:
            return res

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                res[0] = mid
                r = mid - 1
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                res[1] = mid
                l = mid + 1
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return res

    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        sum = 0
        for num in nums:
            if sum > 0:
                sum += num
            else:
                sum = num
            ans = max(sum, ans)
        return ans

    def climbStairs(self, n: int) -> int:
        record = {}
        if n < 0:
            return 0;
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n in record:
            return record[n]
        else:
            value = self.climbStairs(n - 1) + self.climbStairs(n - 2)
            record[n] = value
            return value

    def climbStairsV2(self, n: int) -> int:
        if n < 0:
            return 0;
        if n == 1:
            return 1
        if n == 2:
            return 2
        a, b = 1, 2
        for i in range(3, n + 1):
            temp = a + b
            a = b
            b = temp
        return temp

    def guess(self, num):
        if num < 6:
            return 1
        elif num == 6:
            return 0
        else:
            return -1

    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo, hi = 0, n
        while lo <= hi:
            mid = (lo + hi) // 2
            value = self.guess(mid)
            if 0 == value:
                return mid
            elif 1 == value:
                lo = mid + 1
            else:
                hi = mid - 1

    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # range()
        length = len(nums)
        cur = 0
        while cur < length:
            if nums[cur] == val:
                nums.remove(nums[cur])
                length = len(nums)
            #     如果遇到相等元素，删除一个元素，后面的元素会向前移动
            # 此时保持cur指针位置不变且重新计算length，这样就能保证继续比较新的元素且不会越界
            else:
                cur += 1
        return len(nums)

    def removeElementV2(self, nums, val):
        # 从后往前比较，删除一个元素后面的向前移动，不影响前面的，
        # 指针指向前一个，而且还不会越界，如果正向比较就会越界
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                nums.pop(i)
        return len(nums)

    def searchInsert(self, nums, target):
        """
        给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置
        思路：插入后保持原来顺序，就是查找插入target以后保持nums顺序不变，和python原生模块bisect的bisect_left方法的思路一样
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        import bisect
        return bisect.bisect_left(nums, target)
        pass

    def twoSum(self, nums, target):
        """
        给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSumV2(self, nums, target):
        table = {}
        for index, item, in enumerate(nums):
            table[item] = index
        for index, item in enumerate(nums):
            if (target - item) in table.keys() and index != table[target - item]:
                return [index, table[target - item]]

    def twoSumV3(self, nums, target):
        table = {}
        for index, item in enumerate(nums):
            complement = target - item
            if complement in table.keys():
                return [index, table[complement]]

    def _back(self, nums, result, temp_list):
        if len(temp_list) == len(nums):
            result.append(temp_list[:])
        for num in nums:
            if num in temp_list:
                continue
            temp_list.append(num)
            self._back(nums, result, temp_list)
            temp_list.pop(len(temp_list) - 1)

    def permute(self, nums):
        """
        给定一个没有重复数字的序列，返回其所有可能的全排列
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        temp_list = []
        self._back(nums, result, temp_list)
        return result

    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        判断是否存在重复元素
        :param nums:
        :return:
        """
        count_record = {}
        for num in nums:
            count = count_record.get(num) if count_record.get(num) else 0
            if count > 1:
                return True
            count += 1
            count_record[num] = count
        return False

    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        最长上升子序列
        :param nums:
        :return:
        """
        max_length = 0
        for i in range(len(nums)):
            temp = [nums[i]]
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i] and temp[-1] < nums[j]:
                    temp.append(nums[j])
                if temp[-1] > nums[j] and nums[j] > nums[i]:
                    temp.remove(temp[-1])
                    temp.append(nums[j])
            max_length = max(len(temp), max_length)
        return max_length

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        合并两个有序数组,类似于归并排序的合并操作,只不过这里不产生新数组，在原有的数组上操作
        :param nums1:
        :param m: 元素个数
        :param nums2:
        :param n:
        :return:
        """
        import bisect
        for x in nums2:
            bisect.insort_right(nums1, x, lo=0, hi=n)
            n += 1


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 11, 0, 0]
    b = [2, 3]
    solution = Solution()
    # print(solution.removeElementV2(a, 8))
    # print(list(range(5,-1,-1)))
    # c = [1, 2, 3, 4]
    # print(list(itertools.permutations(c)))
    # print(solution.permute(c))
    # a = {}
    solution.merge(a, 7, b, 2)
    print(a)
