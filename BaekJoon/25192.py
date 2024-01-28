import sys

n = int(input())
name = set()
cnt = 0

for _ in range(n):
    s = input()

    if s == "ENTER":
        name= set()
    else:
        if s in name:
            continue
        else:
            name.add(s)
            cnt+=1

print(cnt)