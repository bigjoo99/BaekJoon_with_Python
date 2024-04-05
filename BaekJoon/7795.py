T = int(input())
result = []

for _ in range(T):
    n, m = map(int, input().split())
    arr_n = list(map(int, input().split()))
    arr_m = list(map(int, input().split()))
    
    arr_n.sort()
    arr_m.sort()
    
    cnt = 0
    
    for x in arr_n:
        start = 0
        end = m-1
        res = -1
        
        while start <= end:
            mid = (start + end) // 2            
                
            if x <= arr_m[mid]:
                end = mid - 1
            elif x > arr_m[mid]:
                res = mid          
                start = mid + 1
                
        cnt += (res+1)  
        
    result.append(cnt)    

for i in result:
    print(i)