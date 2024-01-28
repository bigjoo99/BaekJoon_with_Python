a ,b ,c = map(int, input().split())

arr = []

arr.append(a)
arr.append(b)
arr.append(c)

arr.sort()

if arr[0] + arr[1] <= arr[2]:
    sum = arr[0]+arr[1]
    print(sum+sum-1)
else:
    print(sum(arr))