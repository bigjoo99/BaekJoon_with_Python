n = int(input())

arr = list(map(int,input().split()))

x = int(input())
cnt = 0

for i in range(n):
    for j in range(i+1,n):
        if arr[i]+arr[j] == x:
            cnt +=1

print(cnt)