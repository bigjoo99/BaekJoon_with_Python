def binary_search(arr, target, start, end):
    if start > end:
        return print(0)
    mid = (start+end)//2
    
    if arr[mid] == target:
        return print(1)
    elif arr[mid] < target:
        return binary_search(arr, target, mid+1, end)
    else:
        return binary_search(arr, target, start, mid-1)

T = int(input())
for _ in range(T):
    n = int(input())
    arr_n = list(map(int, input().split()))
    arr_n.sort()

    m = int(input())
    arr_m = list(map(int, input().split()))

    for x in arr_m:
        binary_search(arr_n, x, 0, n-1)