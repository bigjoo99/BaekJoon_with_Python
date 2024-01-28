S = input()
n = len(S)
cnt = 0

for i in range(n):
    if S[i] ==S[n-1-i]:
        cnt+=1
    else:
        print(0)
        break
    
if cnt >= len(S)/2:
    print(1)