import math
import sys

input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int,input().split())))

min_distance = 100000000
x,y = 0,0

for i in range(n):
    x1, y1 = arr[i][0], arr[i][1]
    max_distance = 0    
    for j in range(n):
        x2, y2 = arr[j][0] , arr[j][1]
        
        distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
        if distance > max_distance:
            max_distance = distance
    
    if max_distance < min_distance:
        x, y = x1, y1
        min_distance = max_distance
            
print(x, y)