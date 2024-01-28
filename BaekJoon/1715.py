from queue import PriorityQueue

N = int(input())

q = PriorityQueue(maxsize=N)

for i in range(N):
    x = int(input())
    q.put(x)

result = 0

if N == 1:
    print(0)
else:
    for i in range(N-1):
        x = q.get()
        y = q.get()
        sum = x + y
        q.put(sum)
        result += sum
    print(result)
        