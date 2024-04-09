m,n = map(int, input().split())
snack = list(map(int, input().split()))

start, end = 1, max(snack)

result = 0

while start <= end:
    mid = (start + end) // 2
    count = 0
    
    for x in snack:
        count += x // mid
        
        if count >= m:
            break
        
    if count < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
        
print(result)