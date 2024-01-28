s, n =map(int, input().split())

result = []
arr_r = []

while(s>=n):
    r = s % n
    arr_r.insert(0,r)
    s = s//n
    
arr_r.insert(0,s)

for i in arr_r:
    if i>=10:
        i+=55
        result.append(chr(i))
    else:
        result.append(i)

for x in result:
    print(x, end ='')