alpha = 300
W,H,X,Y,P = map(int, input().split())

R = H/2
X +=alpha
Y +=alpha

cnt = 0

for i in range(P):
    a,b = map(int,input().split())
    a= a+alpha
    b= b+alpha
    
    if (a>=X and a<=X+W) and (b>=Y and b<=Y+H):
        cnt+=1
    elif (a>=X-R and a<X) and (b>Y and b<Y+H):
        if (a-X)*(a-X)+(b-(Y+R))*(b-(Y+R)) <= R*R:   
            cnt+=1
    elif (a>X+W and a<=X+W+R) and (b>Y and b<Y+H):
        if (a-(X+W))*(a-(X+W))+(b-(Y+R))*(b-(Y+R)) <= R*R:   
            cnt+=1  
    
print(cnt)