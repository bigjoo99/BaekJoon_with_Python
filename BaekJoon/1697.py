from collections import deque
import sys
sys.setrecursionlimit(150000)

dx = [-1, 1, 2]
    
def bfs(n, k):
    queue = deque()
    queue.append(n)
    
    while queue:
        x = queue.popleft()
        
        if x == k:
            return graph[k]
        
        for i in range(3):
            if i == 2:
                nx = x + x
            else:
                nx = x + dx[i]
    
    
            if nx<0 or nx>=200000:
                continue
            
            if graph[nx]==0:
                graph[nx] = graph[x] + 1
                queue.append(nx)



n, k = map(int, input().split())
graph = [0 for _ in range(200000)]

print(bfs(n,k))