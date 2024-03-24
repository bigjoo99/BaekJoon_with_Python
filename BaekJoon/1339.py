n = int(input())

arr = []
number = {}
result = 0 
val = 0
num = 9

for _ in range(n):
    x = input()
    arr.append(x)
    
    for i in range(len(x)):
        val += 10 ** (len(x) - 1 - i)
        if x[i] not in number:
            number[x[i]] = val
        else:
            number[x[i]] += val
        val = 0
        
number_sort = sorted(number.items(), key=lambda x:x[1], reverse=True)   
    
for i in range(len(number_sort)):
    result += number_sort[i][1]*num
    num -= 1
    
print(result)