from collections import deque

dx = [-1, -1, 1, 1, -2, -2, 2, 2]
dy = [-2, 2, -2, 2, -1, 1, -1, 1]
    
def bfs(start_x, start_y, end_x, end_y):
    queue = deque()
    queue.append((start_x,start_y))
    
    while queue:
        x, y = queue.popleft()
        
        if x == end_x and y == end_y:
            return graph[end_x][end_y]
        
        for i in range(8):
            nx = x +dx[i]
            ny = y +dy[i]
            
            if nx<0 or ny<0 or nx>=l or ny>=l:
                continue
            
            if graph[nx][ny]==0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))


T = int(input())
result = []
for _ in range(T):
    l = int(input())
    start_x, start_y = map(int,input().split())
    end_x, end_y = map(int,input().split())
    graph = [[0 for _ in range(l)] for _ in range(l)]
    result.append(bfs(start_x, start_y, end_x, end_y))

for i in result:
    print(i)