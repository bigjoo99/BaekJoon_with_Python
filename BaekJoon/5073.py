result = []

while True:
    arr = []
    a1, a2, a3 = map(int, input().split())
    
    if a1 ==0 and a2 ==0 and a3 == 0:
        break
    else:
        arr.append(a1)
        arr.append(a2)
        arr.append(a3)
    
        arr.sort()
        if arr[0] + arr[1] <= arr[2]:
            result.append('Invalid')
        elif arr[0] == arr[2]:
            result.append('Equilateral')
        elif (arr[0]==arr[1] and arr[0]!= arr[2]) or (arr[1] ==arr[2] and arr[0] != arr[2]):
            result.append('Isosceles')
        elif arr[0] != arr[1] and arr[1] != arr[2]:
            result.append('Scalene')
    
for i in result:
    print(i)