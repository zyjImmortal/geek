

def bf(main, pattern):
    """
    单模式串暴力匹配算法，也叫朴素匹配算法
    :param main:
    :param pattern:
    :return:
    """
    m = len(main)
    p = len(pattern)
    if p >= m:
        return 0 if pattern == main else -1
    i = j = 0 # i 是main主串的字符的指针， j 模式串的指针
    while i < m - p + 1:
        while j < p:
            if main[i + j] == pattern[j]:
                # 如果模式串的指针已经到最后一个字符，说明已经匹配到了
                if j == p - 1:
                    return i
                else:
                    # 如果模式字符串还没到最后一个字符，模式串的指针向后移动一位，继续比较
                    j += 1
            else:
                # 如果发生有模式串的字符和主串的不想当，就结束当前这一轮的比较，进行下一轮的比较
                break
        i += 1
    return -1