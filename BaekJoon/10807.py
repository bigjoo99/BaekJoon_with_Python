N = int(input())

arr = []
arr.append(input().split())

    
V = int(input())

cnt=0

for i in range(N):
   if arr[i] == V:
       cnt +=1
       
print(cnt)
       
