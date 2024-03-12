import sys
input = sys.stdin.readline

N = int(input())
arr = []
result = [0] * 1001

for _ in range(N):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: x[1], reverse=True)

for day, score in arr:
    x = day
    if result[x] == 0:
        result[x] = score
    else:
        while x > 0:
            if result[x] == 0:
                result[x] = score
                break
            x -= 1
        if x == 0:
            continue
 
print(sum(result))