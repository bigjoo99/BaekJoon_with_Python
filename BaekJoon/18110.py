import sys

input = sys.stdin.readline

n = int(input())

score = []

for i in range(n):
    score.append(int(input()))
    
score.sort()

if n == 0:
    print(0)
else:
    cut = n*0.15
    cut = int(cut+0.5)    

    for i in range(cut):
        score[i] = 0
    
    for i in range(n-cut,n):
        score[i] = 0

    
    result = sum(score)/(n-2*cut)
    result = int(result+0.5)

    print(result)