n = int(input())
arr = list(map(int, input().split()))
max_max = max(arr)
min_min = min(arr)

print(max_max*min_min)