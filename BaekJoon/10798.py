s = []

for i in range(5):
    s.append(input())
    
        
for j in range(15):
    for i in range(5):
        if j < len(s[i]):
            print(s[i][j], end='')