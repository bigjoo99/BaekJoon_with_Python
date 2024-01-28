n = int(input())
graph = []

for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x,y,cnt):
    count = cnt
    if x<= -1 or x>=n or y<= -1 or y>= n:
        return False
    
    if graph[x][y] == 1:
        graph[x][y] = count
        
        dfs(x-1, y,count)
        dfs(x, y-1,count)
        dfs(x+1, y,count)
        dfs(x, y+1,count)
        return True
    return False

result = 0
cnt = 2

for i in range(n):
    for j in range(n):
        if dfs(i,j,cnt) == True:
            result+=1
            cnt+=1
            
print(result)

arr = []
for i in range(2,result+2):
    count = 0
    for j in range(n):
        for k in range(n):
            if graph[j][k] == i:
                count+=1
    arr.append(count)

arr.sort()

for i in arr:
    print(i)