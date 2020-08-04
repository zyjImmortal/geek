


def bubble(nums):
    size = len(nums)
    for i in range(size):
        for j in range(i + 1, size):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
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
    nums = [4,6,2,88,3,45,43]
    print(quick(nums))