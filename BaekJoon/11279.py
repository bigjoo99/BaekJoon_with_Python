import heapq
import sys

heap = []
result = []
cnt = 0 
input = sys.stdin.readline

n = int(input())

for i in range(n):
    x = int(input())
    
    if x>0:
        heapq.heappush(heap, -x)
        
    elif x==0:
        cnt +=1
        if len(heap) == 0:
            result.append(0)
        else:   
            result.append(-heapq.heappop(heap))
        

for a in range(cnt):
    if not result[a]:
        print(0)
    else:
        print(result[a])