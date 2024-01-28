n = int(input())
m = int(input())

arr = [
    [ 0 for _ in range(n)]
    for _ in range(n)
    ]

ax, ay = 0,0

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
x, y = 0,0          
dir_num = 0
           

arr[x][y] = n*n

for i in range(n * n -1 ,0,-1):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    
    if not in_range(nx, ny) or arr[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4

    x, y = x + dxs[dir_num], y + dys[dir_num]
    arr[x][y] = i
    
    if arr[x][y] == m:
        ax = x + 1
        ay = y + 1
    
for i in arr:
    print(*i)

if m == n*n:
    ax = 1
    ay = 1
    
print(ax,ay)
