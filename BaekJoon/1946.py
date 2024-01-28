import sys

input = sys.stdin.readline

result = []

T = int(input())

for i in range(T):
    score = []
    N = int(input())
    for i in range(N):
        score.append(list(map(int, input().split())))

    score.sort()
    cnt = 0
    
    cut = score[0][1]
    
    for x in range(N):
        if score[x][1] <= cut:
            cnt+=1
            cut = score[x][1]
    result.append(cnt)       
    
for i in result:
    print(i)