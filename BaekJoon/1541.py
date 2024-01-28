import sys

input = sys.stdin.readline

N = input().split('-')
 
for i in range(len(N)):
    
    arr = N[i].split('+')              # '+'가 들어있다면 각 요소들을 더해주고 배열 N에 저장
    sum_x = 0
    
    for j in arr:
        x = int(j)
        sum_x += x
    N[i] = sum_x

result = N[0]

for j in N[1:]:
    result -= j
    
print(result)