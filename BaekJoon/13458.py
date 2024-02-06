import sys
input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))
B,C = map(int, input().split())

result = 0

for i in A:
    result += 1
    i -= B
    
    if i > 0:
        if i%C : 
            result += (i//C + 1)
        else:
            result += (i//C)
            
print(result)