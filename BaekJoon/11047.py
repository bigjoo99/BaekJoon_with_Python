import sys

input = sys.stdin.readline

N, K = map(int, input().split())

coin_arr = []
cnt = 0

for i in range(N):
    coin = int(input())
    coin_arr.append(coin)
    
for coin in reversed(coin_arr):
    
    if K < 5:
            cnt+=K
            break
        
    if K//coin >0:
        cnt+=K//coin
        K = K%coin
        
    
print(cnt)