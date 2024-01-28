N = int(input())

array = [False for i in range(N+1)] 

for i in range(1,N+1):
    j = 1
    while i*j<= N:
        if array[i*j] == False:
            array[i*j] = True
        else:
            array[i*j] = False
        j += 1
            
cnt = 0
for i in array:
    if i == True:
        cnt +=1

print(cnt)