n = int(input())

arr = [list(input()) for _ in range(n)]

max_count = 0

for i in range(n):
    count = arr[i].count('Y')
    if count >= max_count:
        max_count = count

print(max_count)
