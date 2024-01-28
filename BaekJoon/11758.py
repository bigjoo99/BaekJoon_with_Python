import sys

x,y = [],[]

for _ in range(3):
    a,b =  map(int, sys.stdin.readline().split())
    x.append(a)
    y.append(b)
x.append(x[0])
y.append(y[0])

A = 0
B = 0

for i in range(3):
    A+=x[i]*y[i+1]
    B+=y[i]*x[i+1]

s = ((A-B)/2)

if s < 0:
    print('-1')

elif s > 0:
    print('1')

elif s == 0:
    print('0')