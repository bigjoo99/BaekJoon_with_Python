import heapq
import sys

input = sys.stdin.readline

n = int(input())
arr = []
classroom = []

for i in range(n):
    arr.append(list(map(int,input().split())))

arr.sort()

heapq.heappush(classroom, arr[0][1])

for i in range(1,n):
    if arr[i][0] < classroom[0]:
        heapq.heappush(classroom, arr[i][1])
    else:
        heapq.heappop(classroom)
        heapq.heappush(classroom, arr[i][1])
        
print(len(classroom))