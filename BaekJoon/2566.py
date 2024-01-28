grid = []

for i in range(9):
    grid.append(list(map(int,input().split())))
    
grid_max = max(map(max,grid))
index_i=0
index_j=0

for i in range(9):
    for j in range(9):
        if grid[i][j] == grid_max:
            index_i = i+1
            index_j = j+1
            
print(grid_max)
print(index_i,index_j, end='')