import sys
input = sys.stdin.readline

n = int(input())

line = []

for i in range(n):
    line.append(tuple(map(int, input().split())))

line.sort()
left, right = line[0]
result = 0

for x in range(1,n):
    if right < line[x][0]:
        result += right - left
        left , right = line[x][0], line[x][1]
        continue
    right = max(right, line[x][1])
    
result += right - left

print(result)