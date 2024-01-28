def dfs(graph, v, visited):
    global cnt
    visited[v] = cnt
    
    for i in graph[v]:
        if visited[i] == 0:
            cnt+=1
            dfs(graph, i, visited)
            
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
visited = [0]*(n+1)

dfs(graph,r,visited)

for i in range(1, n+1):
    print(visited[i])