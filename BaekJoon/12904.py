S = input()
T = input()

while T != S:
    if len(T) == 0:
        print(0)
        exit()
        
    if T[-1] == 'A':
        T = T[:-1]
        
    elif T[-1] == 'B':
        T = T[::-1]
        T = T[1:]
        
    else:
        print(0)
        exit()

print(1)