import sys


N , M = map(int, sys.stdin.readline().split())

dict = {}

for i in range(N):
    value = sys.stdin.readline().strip()
    dict.update({value:str(i+1)})
    dict.update({str(i+1):value})
    
arr = []

for _ in range(M):
    arr.append(dict[str(input())])    

for i in arr:
    print(i)