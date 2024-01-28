def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                          
import sys
sys.setrecursionlimit(150000)
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for i in range(n+1)]

for i in range(m):
    u,v = map(int,input().split())    
    graph[u].append(v)
    graph[v].append(u)
graph = [sorted(sublist) for sublist in graph]

cnt = 1


visited_dfs= [False]*(n+1)
dfs(graph, r, visited_dfs)

print( )
visited_bfs = [False]*(n+1)
bfs(graph, r, visited_bfs)