import math

N = 2*123456

array = [False,False]+[True for i in range(N-1)] 

# 에라토스테네스의 체 알고리즘
for i in range(2, int(math.sqrt(N)) + 1):
    if array[i] == True: 
        j = 2
        while i * j <= N:
            array[i * j] = False
            j += 1

arr = []
result = []
while True:
      x = int(input())
      arr.append(x)
      cnt = 0
      if x == 0:
            break
      for i in range(x+1, 2*x+1):
        if array[i]:
            cnt+=1
      result.append(cnt)
  
                
for x in result:
      print(x)