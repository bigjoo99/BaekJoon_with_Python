import sys

n , game = input().split()

people = set()   

for _ in range(int(n)):
    people.add(sys.stdin.readline().rstrip())

p = len(people)

if game == 'Y':  
    print(p)
elif game == 'F':
    print(p//2)
else:   
    print(p//3)