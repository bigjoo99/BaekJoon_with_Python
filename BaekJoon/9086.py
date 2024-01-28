n = int(input())

arr_s = []
arr_e = []

for i in range(n):
    s = input()
    arr_s.append(s[0])
    arr_e.append(s[-1])
    
for j in range(n):
    print(arr_s[j]+arr_e[j])