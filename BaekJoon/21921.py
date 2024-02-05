import sys

input = sys.stdin.readline

N, X = map(int, input().split())

arr = list(map(int, input().split()))

if max(arr) == 0:
    print("SAD")
else:
    max_visit = sum(arr[0:X])
    value = max_visit
    count = 1
    for i in range(X, N):
        value -= arr[i-X]
        value += arr[i]
        if value > max_visit:
            max_visit = value
            count = 1
        elif value == max_visit:
            count += 1
    print(max_visit)
    print(count)