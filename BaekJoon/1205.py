N, score, P = map(int, input().split())
result = 0
cnt = 0

if N ==0:
    print(1)
else:
    arr = list(map(int,input().split()))
    
    for i in range(N):
        if score == arr[i]:
            cnt += 1
            
    if min(arr) >= score:
        rank = N+1
        if rank <= P:
            result = rank - cnt
            print(result)
        else:
            result = -1
            print(result)
    else:
        for i in range(N):
            if score > arr[i]:
                arr.insert(i,score)
                rank = i+1
                if rank <= P:
                    result = rank - cnt
                    print(result)    
                    break
                else:
                    result = -1
                    print(result)    
                    break
