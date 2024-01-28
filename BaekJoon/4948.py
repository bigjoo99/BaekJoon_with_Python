N = 123456 * 2 + 1

arr = [True] * N

def prime_cnt(val):
    cnt = 0
    for i in range(val + 1, val * 2 + 1):
        if arr[i]:
            cnt += 1
    print(cnt)
    
for i in range(2, int(N**0.5)+1):
    if arr[i]:
        for j in range(2*i, N, i):
            arr[j] = False


while True:
    val = int(input())
    if val == 0:
        break
    prime_cnt(val)