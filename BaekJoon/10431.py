P = int(input())

result = []

for _ in range(P):
    cnt = 0
    arr = list(map(int, input().split()))    
    for i in range(1, 20):
        for j in range(i+1,21):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                cnt +=1
    result.append(cnt)
    
for x in range(len(result)):
    print(x+1, result[x])