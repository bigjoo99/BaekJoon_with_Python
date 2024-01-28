n = int(input())

s = set()

for i in range(n):
    name, state = map(str, input().split())
    if state == 'enter':
        s.add(name)
    else:
        s.remove(name)
    
arr = list(s)

arr.sort(reverse=True)

for i in arr:
    print(i)