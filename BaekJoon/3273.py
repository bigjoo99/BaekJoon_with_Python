import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
x = int(input())
cnt = 0

arr.sort()
start = 0
end = n-1

while start < end:
    sum = arr[start] + arr[end]
    if sum == x: 
        cnt += 1
        start += 1
    elif sum < x: 
        start+=1
    else:
        end-=1
print(cnt)