A,B = map(int,input().split())
C = int(input())

D= C//60
E= C%60

if A+D>=24:
    H=A+D-24
else:
    H=A+D
    
if  B+E>=60: 
    if H+1>=24:
        print( int(H+1-24), int(B+E-60))
    else:
        print( int(H+1), int(B+E-60))        
else:
    print( int(H), int(B+E))
    