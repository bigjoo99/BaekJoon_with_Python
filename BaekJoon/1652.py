n = int(input())
arr = [list(input()) for _ in range(n)]

width = 0
height = 0

for i in range(n):
    cnt = []
    for j in range(n):
        if arr[i][j] == '.':
            cnt.append(arr[i][j])
        elif arr[i][j] == 'X':
            if cnt.count('.') >= 2:
                width += 1
                cnt.clear()
            else:
                cnt.clear()
    if cnt.count('.') >= 2:
        width += 1
                
for j in range(n):
    cnt = []
    for i in range(n):
        if arr[i][j] == '.':
            cnt.append(arr[i][j])
        elif arr[i][j] == 'X':
            if cnt.count('.') >= 2:
                height += 1
                cnt.clear()
            else:
                cnt.clear()
    if cnt.count('.') >= 2:
        height += 1
            
print(width, height)