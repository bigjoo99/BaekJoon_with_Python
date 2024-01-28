from collections import deque

n,m  = map(int, input().split())

graph = [0] * 101
visited = [False] * 101

ladder = dict()
for i in range(n):              # 사다리 정보
    x, y = map(int, input().split())
    ladder[x] = y

snake = dict()
for j in range(m):              # 뱀 정보
    u, v = map(int, input().split())
    snake[u] = v
    
queue = deque()
dx = [1,2,3,4,5,6]

def bfs(x):
    queue.append(x)
    while queue:
        x = queue.popleft()
        
        if x == 100:
            print(graph[x])    
            break
        
        for i in range(6):
            nx = x +dx[i]
            
            if nx>=101:
                continue

            if nx in ladder.keys():
                nx = ladder[nx]
                
            if nx in snake.keys():
                nx = snake[nx]
            
            if not visited[nx]:
                visited[nx] = True
                graph[nx] = graph[x] + 1
                queue.append((nx))

bfs(1)