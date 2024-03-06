from collections import deque

def left(arr):
    d = arr
    x = d.popleft()
    d.append(x)
    return d

def right(arr):
    d = arr
    x = d.pop()
    d.appendleft(x)
    return d

n , m = map(int, input().split())
arr_pop = list(map(int, input().split()))
arr = deque([i for i in range(1,n+1)])

cnt = 0

for i in arr_pop:
    while True:
        if arr[0] == i:
            arr.popleft()
            break
        else:
            if arr.index(i) < len(arr)/2:
                while arr[0] != i:
                    arr = left(arr)
                    cnt += 1
            else:
                while arr[0] != i:
                    arr = right(arr)
                    cnt += 1
                    
print(cnt)