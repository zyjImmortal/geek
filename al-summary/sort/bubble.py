def bubble(nums):
    """
    冒泡排序
    最好情况时间复杂度：O(n) 已经排好序
    最坏情况时间复杂度：O(n2)，倒序

    是稳定排序算法
    """
    size = len(nums)
    hasChange = True
    for i in range(size):
        if hasChange:
            break
        hasChange = False
        for j in range(i + 1, size):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                hasChange = True
    return nums


def insert(nums):
    """
    [2,3,1,8,6,1]
    :param nums:
    :return:
    """
    if len(nums) <= 1:
        return nums
    i = 1
    while  i < len(nums):
        value = nums[i]
        # 从左开始到j区间都是已排序的区间，核心思路就是，每次去一个元素，在已排序区间找到合适的位置插入
        j = i -1
        while j >= 0:
            if nums[j] > value:
                nums[j+1] = nums[j]
            else:
                break
            j -= 1
        nums[j+1] = value
        i+=1

    return nums


def quick(nums):
    '''快速排序'''
    if nums == []:
        return []
    else:
        first = nums[0]
        left = quick([l for l in nums[1:] if l < first])
        right = quick([r for r in nums[1:] if r >= first])
        return left + [first] + right


if __name__ == '__main__':
    nums = [4, 6, 2, 88, 3, 45, 43]
    print(insert(nums))
    # print(list(range(10, -1, -1)))
