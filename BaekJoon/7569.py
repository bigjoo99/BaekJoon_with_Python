from collections import deque

m, n, h = map(int, input().split())


graph = []
queue = deque()

for k in range(h):
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
        for j in range(m):
            if arr[i][j]==1:
                queue.append((k,i,j))
    graph.append(arr)
    
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():    
    while queue:
        z, x, y = queue.popleft()  
        for i in range(6):
            nz = z +dz[i]
            nx = x +dx[i]
            ny = y +dy[i]
            
            if nx<0 or ny<0 or nz<0 or nx>=n or ny>=m or nz>=h:
                continue
                
            if graph[nz][nx][ny]== -1:
                continue
                
            if graph[nz][nx][ny]==0:
                graph[nz][nx][ny] = graph[z][x][y] + 1
                queue.append((nz,nx,ny))
    
bfs()

result = 0
for i in graph:
    for j in i:
        for k in j:
            if k==0:
                print(-1)
                exit(0)
        result = max(result,max(j))


print(result-1)