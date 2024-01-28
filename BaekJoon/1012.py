import sys
sys.setrecursionlimit(150000)

def dfs(x,y):
    if x<= -1 or x>=n or y<= -1 or y>= m:
        return False
    
    if graph[x][y] == 1:
        graph[x][y] = 0
        
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

T = int(input())
result = []

for x in range(T):
    m,n,k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(k):
        x,y = map(int, input().split())
        graph[y][x] = 1
    cnt = 0
    for i in range(n):
        for j in range(m):
            if dfs(i,j) == True:
                cnt+=1
    result.append(cnt)

for i in result:
    print(i)