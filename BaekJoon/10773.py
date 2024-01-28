k = int(input())

arr = []

for i in range(k):
    n = int(input())
    if i==0 and n==0:
        break
    elif n==0:
        arr.pop()
    else:
        arr.append(n)

print(sum(arr))
      