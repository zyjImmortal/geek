import requests
import heapq
from bisect import *

response = requests.get('https://www.meipian.cn/wap/downloadpage/monitor')
mask_id = '1shb6d5v'
host_urls = ['www.meipian1.cn','www.meipian2.cn','www.meipian3.cn','www.meipian3.cn','www.meipian4.cn',
             'www.meipian5.cn','www.meipian6.cn','www.meipian7.cn','www.meipian8.cn','www.meipian9.cn']

def monitor():
    for host in host_urls:
        url = "https://" + host +"/" + mask_id
        response = requests.get(url)

def bisect_left_self(a,x,lo=0,hi=None):
    if lo<0:
        raise ValueError("lo必须是非负整数")
    if hi is None:
        hi=len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        # 就是当a[mid]=x的时候是从左侧找还是从右侧找，最终找到的位置
        # 也就是左侧插入右侧插入
        if a[mid] < x:
            lo = mid+1
        else:
            hi = mid
    return lo

def test_heapq():
    heapq.heappush()
    pass

nums = [5,7,7,8,8,10]
x = 9
print(bisect_left(nums,x))
