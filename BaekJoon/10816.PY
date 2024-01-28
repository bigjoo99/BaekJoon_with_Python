import sys
from bisect import bisect_right, bisect_left

N = int(sys.stdin.readline())
list_N = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
list_M = list(map(int, sys.stdin.readline().split()))

list_N.sort()
cnt_list = []

for i in list_M:
    cnt = 0
    start = bisect_left(list_N,i)
    end = bisect_right(list_N, i)
    
    cnt = end - start
    cnt_list.append(cnt)
    
print(*cnt_list)