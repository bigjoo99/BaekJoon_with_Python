from collections import deque

n = int(input())

arr = list(map(int, input().split()))

result = [-1] * n
stack = deque()

for i in range(n):
    while stack and (stack[-1][0] < arr[i]):
        _, idx = stack.pop()
        result[idx] = arr[i]
    stack.append([arr[i], i])
    
print(*result)