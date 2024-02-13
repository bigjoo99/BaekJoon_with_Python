arr = list(map(int, input().split()))

ascending = [1,2,3,4,5,6,7,8]
descending = [8,7,6,5,4,3,2,1]

arr_sort = sorted(arr)
arr_sort_reverse = sorted(arr, reverse=True)

if arr_sort == arr:
    print('ascending')    
elif arr_sort_reverse == arr:
    print('descending')
else:
    print('mixed')
    
     