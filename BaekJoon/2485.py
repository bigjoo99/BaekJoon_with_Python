from math import gcd 

N = int(input())

arr=[]
for _ in range(N):
    arr.append(int(input()))
    
distance = []
for x in range(N-1):
    distance.append(arr[x+1] - arr[x])
    
g = distance[0]
for x in range(1, len(distance)):
    g = gcd(g , distance[x])

result = 0
for each in distance:
    result += each // g - 1
print(result)