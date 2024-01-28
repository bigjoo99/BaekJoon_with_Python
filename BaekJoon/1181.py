n = int(input())

arr = []

for i in range(n):
    arr.append(input())

arr_set = set(arr)
arr= list(arr_set)

arr.sort()
arr.sort(key=lambda x: len(x))

for i in arr:
    print(i)

