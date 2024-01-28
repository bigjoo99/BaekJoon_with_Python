arr = [0 for _ in range(30)]

for i in range(28):
    x = int(input())
    arr[x-1] = 1
    
for j in range(30):
    if arr[j] != 1:
        print(j+1)
