def quick_sort(array):
    if len(array) < 1:
        return
    pivot = array[0]
    less_array = [x for x in array if x < pivot]
    more_array = [x for x in array if x >= pivot]
    return quick_sort(less_array) + quick_sort(more_array)


def partition(array, p, r):
    pivot = array[r - 1]
    less_array = []
    more_array = []
    for i in range(p, r):
        if array[i] > pivot:
            more_array.append(array[i])
        else:
            less_array.append(array[i])

    return pivot


def quick_sort_c(array, p, r):
    if p >= r:
        return
    q = partition(array, p, r)
    quick_sort_c(array, p, q - 1)
    quick_sort_c(array, q + 1, r)


def merge_sort(array):
    if len(array) == 1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result

array = [3, 2, 6, 8, 3, 4, 6, 9]
l2 = merge_sort(array)
print(l2)
