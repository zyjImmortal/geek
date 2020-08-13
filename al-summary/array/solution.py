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

    def pivotIndex(self, nums: List[int]) -> int:
        '''给定一个整数类型的数组 nums，请编写一个能够返回数组“中心索引”的方法
            定义数组中心索引的：数组中心索引的左侧所有元素相加的和等于右侧所有元素相加的和
            不存在中心索引，那么我们应该返回 -1。如果数组有多个中心索引，那么我们应该返回最靠近左边的那一个
        '''
        size = len(nums)
        for i in range(size):
            left = right = 0
            for j in range(i):
                left += nums[j]
            for z in range(i + 1, size):
                right += nums[z]
            if left == right:
                return i
        return -1

    def pivotIndexV2(self, nums: List[int]) -> int:
        size = len(nums)
        left = 0
        right = sum(nums)
        for i in range(size):
            right -= nums[i]
            if left == right:
                return i
            left += nums[i]
        return -1

    def pivotIndexV3(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0
        for index, value in enumerate(nums):
            if left == total - value - left:
                return index
            left += value
        return -1

    def dominantIndex(self, nums: List[int]) -> int:
        '''
        在一个给定的数组nums中，总是存在一个最大元素 。
        查找数组中的最大元素是否至少是数组中每个其他数字的两倍。
        如果是，则返回最大元素的索引，否则返回-1
        :param nums:
        :return:
        '''
        max_value = max_index = 0
        for index, value in enumerate(nums):
            if value > max_value:
                max_value = value
                max_index = index
        for index, value in enumerate(nums):
            if max_value < value * 2 and index != max_index:
                return -1
        return max_index

    def dominantIndexV2(self, nums: List[int]) -> int:
        max_value = max(nums)
        if all(max_value > x * 2 for x in nums):
            return nums.index(max_value)
        return -1

    def plusOne(self, digits: List[int]) -> List[int]:
        '''
        给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
        最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
        你可以假设除了整数 0 之外，这个整数不会以零开头
        :param digits:
        :return:
        '''
        mod = 0
        size = len(digits)
        for i in range(size - 1, -1, -1):
            if i == size - 1:
                value = digits[i]
                digits[i] = (value + 1) % 10
                mod = (value + 1) // 10
            else:
                value = digits[i] + mod
                digits[i] = value % 10
                mod = value // 10

        if mod != 0:
            digits.insert(0, mod)
        return digits

    def plusOneV2(self, digits: List[int]) -> List[int]:
        mod = 1
        size = len(digits)
        for i in range(size - 1, -1, -1):
            value = digits[i]
            digits[i] = (value + mod) % 10
            mod = (value + mod) // 10
        return digits if mod == 0 else [mod].extend(digits)

    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        '''
        给定一个含有 M x N 个元素的矩阵（M 行，N 列），请以对角线遍历的顺序返回这个矩阵中的所有元素
        :param matrix:
        :return:
        '''

    def removeElementV2(self, nums: List[int], val: int) -> int:
        """需要移动元素，无序列表
           需要两个指针，快慢指针
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                i += 1
                nums[i] = nums[j]
        return i + 1

    def removeElement(self, nums: List[int], val: int) -> int:
        """
        3 5 7 7 0 9 ,,7
        :param nums:
        :param val:
        :return:
        """
        i = 0
        size = len(nums)
        while i < size:
            if nums[i] == val:
                nums[i] = nums[size - 1]  # 但是这种方式会有一个问题
                size -= 1
                continue
            i += 1
        return size

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

    def removeDuplicatesV2(self, nums: List[int], k) -> int:
        """

        [1,1,1,2,2,3]
        :param nums:
        :return:
        """
        if nums is None:
            return 0
        if len(nums) <= k:
            return len(nums)
        # index表示不重复集合的右边界。边界是从0开始到k-1.总共k个数，已经包含进去k个数了，所有右边界的值为k-1
        index = k-1
        for i in range(k, len(nums)):
            # 新加入的元素不能构成连续相同的三个元素
            if nums[i] != nums[index -1]:
                index += 1
                nums[index] = nums[i]
        return index + 1

    def rotate(self, nums, k):
        k = k % len(nums)
        self.reverse(nums, 0, len(nums)-1)
        self.reverse(nums, 0, k -1)
        self.reverse(nums, k, len(nums) - 1)

    def reverse(self, nums, start, end):
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1


if __name__ == '__main__':
    solution = Solution()
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    matrixv2 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
    # nums = [9, 9]

    nums = [0, 0, 1, 1, 1, 1, 2, 2, 3, 3]

    print(solution.reverse(nums, 0, len(nums)-1))
    print(nums)
