import copy
# a1 = ['afff', 'b','c']
# a = ('afff', 'b','c', a1)
# c = copy.copy(a)
# d = copy.deepcopy(a)
#
# if c == d:
#      print("c和d的值相等")
# if id(c) == id(d):
#     print("c和d的地址相等")
# print(id(a))
# print(id(c))
# print(id(d))
 #
 #     a = [1,2,3]
 # b = [4,5,6,a]
 # import copy
 # c = copy.copy(b)
 # c [4, 5, 6, [1, 2, 3]]
 # a.append(8)
 # c [4, 5, 6, [1, 2, 3, 8]]
 # d = copy.deepcopy(b)
 # d [4, 5, 6, [1, 2, 3, 8]]
 #
 # a.append(66)
 #
 # d = [4, 5, 6, [1, 2, 3, 8]

# a = (1,2,3)
# b = copy.copy(a)
# c = copy.deepcopy(a)
# print(id(a))
# print(id(b))
# print(id(c))
#
# a1 = [1,2,3]
# a = (1,2,3, a1)
# b = copy.copy(a)
# c = copy.deepcopy(a)
# print(id(a))
# print(id(b))
# print(id(c))
import time


def runtime(func):
    def f(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        print("运行时间:{}".format(time.time() - start))
        return res
    return f

@runtime
def run(i):
    print(i)


run("jsjjs")