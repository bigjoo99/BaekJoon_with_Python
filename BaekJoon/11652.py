import sys
input = sys.stdin.readline

n = int(input())
dict = {}

for i in range(n) :
    x = int(input())
    if x in dict :
        dict[x] += 1
    else :
        dict[x] = 1

result = sorted(dict.items(),key = lambda x : (-x[1],x[0]))
print(result[0][0])