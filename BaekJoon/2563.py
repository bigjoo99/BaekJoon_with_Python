import sys

n = int(sys.stdin.readline())

arr = [[0 for _ in range(100)] for __ in range(100)]
cnt = 0

for i in range(n):
    w,h = map(int, sys.stdin.readline().split())
    x = w
    y = 90-h
    for n in range(x,x+10):
        for m in range(y,y+10):
            arr[n][m] = 1
            
for x in range(100):
    for y in range(100):
        if arr[x][y] != 0 :
            cnt +=1
            
print(cnt)
