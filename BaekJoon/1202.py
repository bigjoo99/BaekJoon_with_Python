import sys
import heapq

input = sys.stdin.readline
n , k = map(int, input().split())

arr = []
bag = []
heap = []
result = 0

for _ in range(n):
    arr.append(list(map(int,input().split())))

for _ in range(k):
    bag.append(int(input()))
    
arr.sort()
bag.sort()

for x in bag:
    while arr and x >= arr[0][0]:
        heapq.heappush(heap, -arr[0][1])  
        heapq.heappop(arr)
    
    if heap:
        result += heapq.heappop(heap)
        
print(-result)