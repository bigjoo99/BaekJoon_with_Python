N = int(input())

dp = [0] * 1001

dp[1] = 'SK'
dp[2] = 'CY'
dp[3] = 'SK'

for i in range(4,N+1):
    if dp[i-1] == 'SK' or dp[i-3] == 'SK':
        dp[i] = 'CY'
    
    else:
        dp[i] = 'SK'
        
print(dp[N])