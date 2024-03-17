x = int(input())

d = [-1]*5001

d[3] = d[5] = 1

for i in range(6,x+1):
    if d[i-3] > 0 and d[i-5] > 0:
        d[i] = min(d[i-3]+1, d[i-5]+1)
        
    elif d[i-3] > 0 and d[i-5] < 0:
        d[i] = d[i-3] + 1
    
    elif d[i-3] < 0 and d[i-5] > 0:
        d[i] = d[i-5] + 1
    
    else:
        d[i] = -1    
    
print(d[x])