from typing import *


class Solution:
    """
    数组类题型总结：
    元素出现次数类： hash表、位运算
    矩阵搜索
    有序数组合并
    最长连续递增子序列
    移除重复元素
    给定和或者差，找数组中存在元素或者判断是否存在
    排列组合问题

    """

    def singleNumber(self, nums):
        """
        给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
        说明：你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗
        :param nums:
        :return:
        """
        record = {}
        for num in nums:
            record[num] = record.get(num, 0) + 1
        for key in record.keys():
            if record[key] == 1:
                return key
        return -1

    def singleNumberV2(self, nums):
        '''位运算，相同的两个数做异或运算结果为0，0与数字做异或运算结果为数字，位运算满足交换律'''
        result = 0
        for num in nums:
            # 异或运算符
            result = result ^ num
        return result

    def singleNumbers(self, nums: List[int]) -> List[int]:
        """
        一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。
        请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)
        :param nums:
        :return:
        """
        record = {}
        for num in nums:
            record[num] = record.get(num, 0) + 1
        result = []
        for key in record.keys():
            if record[key] == 1:
                result.append(key)
        return result
        # return [n for n, v in collections.Counter(nums).items() if v == 1]

    def searchMatrix(self, matrix, target):
        '''
        在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
        请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数
        每行中的整数从左到右按升序排列。
        每行的第一个整数大于前一行的最后一个整数

        因为每一行递增，每一列递增。所以我们可以从右上角往左下角找或者从左下角往右上角找。每次比较可以排除一行或者一列，时间复杂度为O(m+n)
        :param matrix:
        :param target:
        :return:
        '''
        if len(matrix) == 0:
            return False
        row, col = 0, len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False

    def searchMatrixBy(self, matrix, target):
        if len(matrix) == 0:
            return False

        row_start, row_end, row = 0, len(matrix) - 1, 0
        col = len(matrix[0]) - 1
        while row_start <= row_end:
            row_mid = (row_start + row_end) // 2
            if matrix[row_mid][0] <= target and matrix[row_mid][col] >= target:
                row = row_mid
                break
            elif target < matrix[row_mid][0]:
                row_end = row_mid - 1
            elif matrix[row_mid][col] < target:
                row_start = row_mid + 1

        start, end = 0, col
        while start <= end:
            mid = (start + end) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return False

    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        给定两个排序后的数组 A 和 B，其中 A 的末端有足够的缓冲空间容纳 B。 编写一个方法，将 B 合并入 A 并排序。
        初始化 A 和 B 的元素数量分别为 m 和 n
        """
        i, j, index = m - 1, n - 1, m + n - 1
        while j >= 0:
            if i < 0:
                A[:j + 1] = B[:j + 1]
                break
            elif A[i] > B[j]:
                A[index] = A[i]
                i -= 1
            else:
                A[index] = B[j]
                j -= 1
            index -= 1

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
        给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，
        使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k

        :param nums:
        :param k:
        :return:
        '''
        record = {}
        for i in range(len(nums)):
            if nums[i] in record.keys() and (i - record[nums[i]]) <= k:
                return True
            record[nums[i]] = i
        return False

    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        '''
        给定一个整数数组，判断数组中是否有两个不同的索引 i 和 j，
        使得 nums [i] 和 nums [j] 的差的绝对值最大为 t，并且 i 和 j 之间的差的绝对值最大为 ķ

        :param nums:
        :param k:
        :param t:
        :return:
        '''
        if k < 0 or t < 0:
            return False
        # if k == 10000:
        #     return False
        for i in range(len(nums)):
            # 当i + k + 1大于nums的长度的时候会产生越界异常，所以要取两个小的那个
            for j in range(i + 1, min(len(nums), i + k + 1)):
                if abs(nums[i] - nums[j]) <= t:
                    return True
        return False

    def findLengthOfLCIS(self, nums: List[int]) -> int:
        '''
        给定一个未经排序的整数数组，找到最长且连续的的递增序列
        :param nums:
        :return:
        '''
        if len(nums) == 0:
            return 0
        max_length = 1
        start, cur, end = 0, 0, 1
        while end < len(nums):
            if nums[end] > nums[cur]:
                length = end - start + 1
                max_length = max(max_length, length)
                end += 1
                cur += 1
            else:
                start = cur = end
                end += 1
        return max_length

    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。`
        不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成

        :param nums:
        :return:
        '''
        if len(nums) < 2:
            return 0
        i, j = 0, 1
        while j < len(nums):
            if nums[j] == nums[i]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
                j += 1
        return i + 1

    def _backtrack(self, i, nums, res, tmp):
        res.append(tmp)
        for j in range(i, len(nums)):
            tmp.append(nums[j])
            self._backtrack(j + 1, nums, res, tmp)
            tmp.pop()
            
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
        说明：解集不能包含重复的子集
        :param nums:
        :return:
        '''
        res = []
        self._backtrack(0, nums, res, [])
        return res



if __name__ == '__main__':
    solution = Solution()
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    matrixv2 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
    nums = [1, 3, 5, 4, 2, 3, 4, 5]

    print(solution.findLengthOfLCIS(nums))
