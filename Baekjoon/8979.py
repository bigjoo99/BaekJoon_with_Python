n, k = map(int, input().split())

arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))        
    
arr.sort(key=lambda x: (-x[1], -x[2], -x[3]))

for x in range(n):
    if arr[x][0] == k:
        rank = x+1
        location = x
    
for i in range(0,location):
    if arr[location][1:]== arr[i][1:] :
        rank -= 1
        
print(rank)
