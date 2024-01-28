s , n = map(str, input().split())

n = int(n)
result = 0
x = len(s)-1

for i in range(len(s)):
    if ord(s[i]) >= 65:
        xx = ord(s[i])-55
        result+= (xx)*(n**x)
    else:
        xx = int(s[i])
        result+= (xx)*(n**x)
    x-=1

print(result) 