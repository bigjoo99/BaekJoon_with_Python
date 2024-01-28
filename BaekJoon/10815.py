N = int(input())

<<<<<<< HEAD
arr_N = list(map(int, input().split()))
set_N = set(arr_N)

M = int(input())

arr_M = list(map(int, input().split()))
set_M = set(arr_M)

arr_N_M = set_M.intersection(set_N)

for i in arr_M:
    if i in arr_N_M:
        print(1, end =' ')
    else:
        print(0, end=' ')
        
=======
arr_n = list(map(int, input().split()))

M = int(input())

arr_m = list(map(int,input().split()))

result = []

for i in arr_m:
    if i in arr_n:
        result.append(1)
    else:
        result.append(0)
        
for i in result:
    print(i, end=' ')
>>>>>>> 2587d4f6deae093d5f7a17d47664ab24330fc533
