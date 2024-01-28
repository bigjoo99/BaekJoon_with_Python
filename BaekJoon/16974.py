N, X = map(int,input().split())

arr =[[]for _ in range(N)]
bg = 'P'

for i in range(N):
    arr.insert(0,'B')
    arr.append(bg)
    arr.append('p')
    arr.append('')