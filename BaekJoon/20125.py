N = int(input())
cookie = []
breaker = False 
left_arm, right_arm, waist, left_leg, right_leg = 0,0,0,0,0

for i in range(N):
    cookie.append(list(input()))

for i in range(N):
    for j in range(N):
        if cookie[i][j] == '*':
            heart_x = i+2
            heart_y = j+1
            breaker = True
            break
    if breaker == True:
        break

for i in range(N):
    for j in range(N):
        if i == heart_x-1 and j < heart_y-1 and cookie[i][j] == '*':
            left_arm += 1
            
        if i == heart_x-1 and j > heart_y-1 and cookie[i][j] == '*':
            right_arm += 1
            
        if i >= heart_x and j == heart_y-1 and cookie[i][j] == '*':
            waist += 1
            
        if i >= heart_x + waist and j < heart_y-1 and cookie[i][j] == '*':
            left_leg += 1
            
        if i >= heart_x + waist and j > heart_y-1 and cookie[i][j] == '*':
            right_leg += 1
        
print(heart_x, heart_y)
print(left_arm, right_arm, waist, left_leg, right_leg )