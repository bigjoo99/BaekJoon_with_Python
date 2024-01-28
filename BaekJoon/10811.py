N, M = map(int,input().split())

arr = [0 for _ in range(N)]

for i in range(N):
    arr[i] = i+1

for _ in range(M):

    i, j = map(int, input().split())
    x_arr = arr[i-1:j]
    x_arr.reverse()
    arr[i-1:j] = x_arr
        

for i in arr:
    print(i, end =' ')
            
    
    
    