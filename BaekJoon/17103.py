import sys
input = sys.stdin.readline

N = 1000000

array = [False,False]+[True]*(N-1)  

# 에라토스테네스의 체 알고리즘
for i in range(2, N+1):
    if array[i]:
        for j in range(i*2, N+1, i):
            array[j] = False

T = int(input())

for _ in range(T):
    x = int(input())
    cnt = 0
    for i in range(2, x//2+1):
        if array[i] and array[x-i]:
            cnt+=1
    print(cnt)       