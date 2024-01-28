import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

arr1 = sorted(list(set(arr)))

dic = {arr1[i]: i for i in range(len(arr1))}

for i in arr:
    print(dic[i], end = ' ')