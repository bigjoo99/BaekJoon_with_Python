def dfs(graph, v, visited):
    visited[v] = True
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            
import sys
sys.setrecursionlimit(150000)
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for i in range(n+1)]

for i in range(m):
    u,v = map(int,input().split())    
    graph[u].append(v)
    graph[v].append(u)
graph = [sorted(sublist) for sublist in graph]

cnt = 1
visited = [False]*(n+1)

dfs(graph,1,visited)

result = -1
for i in range(1, n+1):
    if visited[i]:
        result+=1

print(result)