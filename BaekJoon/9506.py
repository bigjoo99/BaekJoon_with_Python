arr = []
state = False

while state ==False:
    n = int(input())
    if n == -1:
        state = True
    else:
        arr.append(n)
        state = False

result = []
for i in arr:
    measure = []
    for j in range(1,i+1):
        if i % j == 0:
            measure.append(j)
    result.append(measure)
    
for i in range(len(arr)):
    sum = 0
    for j in range(len(result[i])-1):
        sum+= result[i][j]
    
    if arr[i] == sum:
        print(arr[i], end='')
        print(' = ', end='')
        for k in range(len(result[i])-2):
            print(result[i][k], end='')
            print(' + ', end='')
        print(result[i][-2])
            
    else:
        print(arr[i], end='')
        print(" is NOT perfect.")
        