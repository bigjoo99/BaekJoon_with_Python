n, k = map(int, input().split())
arr = list(map(int, input().split()))

multitap = []
cnt = 0

for i in range(k):
    if arr[i] in multitap:          # 사용할 플러그가 이미 멀티탭에 꽂혀있다면 패스
        continue
        
    elif len(multitap) < n:         # 멀티탭 구멍이 남는다면 꽂기
        multitap.append(arr[i])
        
    else:                           # 사용중인 플러그를 빼고 새로운 플러그를 꽂아야함
        ejaculation = 0
        far = 0
        for x in multitap:
            if x not in arr[i:]:
                ejaculation = x
                break
            
            elif arr[i:].index(x) > far:
                far = arr[i:].index(x)
                ejaculation = x
            
        multitap[multitap.index(ejaculation)] = arr[i]
        cnt += 1

print(cnt)