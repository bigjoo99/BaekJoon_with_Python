n = int(input())
plus = []
minus = []
sum = 0

for i in range(n):
    x = int(input())
    if x > 1 :
        plus.append(x)
    elif x <= 0:        
        minus.append(x)
    else:
        sum += x
        
plus.sort(reverse=True)
minus.sort()


for i in range(0, len(plus), 2):
    if i+1 >= len(plus):
        sum += plus[i]
    else:
        sum += plus[i] * plus[i+1]

for i in range(0, len(minus), 2):
    if i+1 >= len(minus):
        sum += minus[i]
    else:
        sum += minus[i] * minus[i+1]

print(sum)