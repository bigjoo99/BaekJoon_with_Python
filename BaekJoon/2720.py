T = int(input())

coin = [25, 10, 5, 1]

result = []

for _ in range(T):
    C = int(input())
    coin_x = []
    for i in coin:
        x = C//i
        C = C%i
        coin_x.append(x)
    result.append(coin_x)
    
for i in range(T):
    for j in range(4):
        print(result[i][j], end=' ')
    print()