N = int(input())
arr = dict()

for _ in range(N):
    a = input()
    if a in arr:
        arr[a] += 1
    else:
        arr[a] = 1

arr_sort = sorted(arr.items(), key=lambda x: (-x[1], x[0]))

print(arr_sort[0][0])