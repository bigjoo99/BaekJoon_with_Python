import sys

input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

sum = 0

for i in range(N):
    c = A[i]*B[i]
    sum += c     
    
print(sum)