a, b = map(int, input().split())

cnt = 1

while b != a:
    if b %2 == 0:
        b = b//2
        cnt += 1
    
    elif str(b)[-1] == '1':
        b = int(str(b)[:-1])
        if b < a:
            cnt = -1
            break
        cnt += 1
            
    else:
        cnt = -1
        break

print(cnt)