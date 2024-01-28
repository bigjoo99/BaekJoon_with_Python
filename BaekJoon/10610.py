n = input()

if '0' not in n:
    print(-1)

else:
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    
    if sum %3 != 0:
        print(-1)
        
    else:
        sort_n = sorted(n, reverse=True)
        result = "".join(sort_n)
        print(result)
