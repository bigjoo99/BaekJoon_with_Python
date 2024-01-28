from collections import deque

def bfs(graph, start, visited):
    global cnt
    queue = deque([start])
    visited[start] = cnt
    
    while queue:
        v = queue.popleft()
        
        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                cnt+=1
                visited[i] = cnt
            
import sys
sys.setrecursionlimit(150000)
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for i in range(n+1)]

for i in range(m):
    u,v = map(int,input().split())    
    graph[u].append(v)
    graph[v].append(u)
graph = [sorted(sublist, reverse=True) for sublist in graph]

cnt = 1
visited = [0]*(n+1)

bfs(graph,r,visited)

for i in range(1, n+1):
    print(visited[i])