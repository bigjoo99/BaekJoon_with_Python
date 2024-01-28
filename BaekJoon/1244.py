import sys

input = sys.stdin.readline

N = int(input())

switch = list(map(int, input().split()))

student = int(input())

sex_arr = []
num_arr = []
state = True

for i in range(student):
    sex, num = map(int, input().split())
    
    if sex == 1 :               # 남학생일 경우
        for j in range(len(switch)):
            if num-1 ==0:
                if switch[0] == 0:
                    switch[0] = 1
                elif switch[0] == 1: 
                    switch[0] = 0
                break
            elif (j+1) % num == 0 and j !=0 :
                if switch[j] == 0:
                    switch[j] =1
                elif switch[j] ==1:
                    switch[j] = 0
    elif sex == 2:
        prev = num-2
        next = num
        if switch[num-1] ==0:
            switch[num-1] = 1
        elif switch[num-1] ==1:
            switch[num-1] = 0    
         
        while state:
            if prev<0:
                state = False
            elif next>len(switch):
                state = False
            else:
                if switch[prev] == switch[next]:
                    if switch[prev] ==0:
                        switch[prev] =1
                        switch[next] =1
                    elif switch[prev] ==1:
                        switch[prev] =0
                        switch[next] =0
                        
                    prev -=1
                    next +=1
                    continue
                state = False 
            
    
for i in range(len(switch)):
    if i %19 == 0 and i !=0:
        print()
    print(switch[i], end= ' ')