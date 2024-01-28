div = 0
sum = 0

for i in range(20):
    S, num, grade = input().split()
    
    if grade == 'P':
        continue
    else:
        div += float(num)
    
        if grade == 'A+':
            sum+=float(num)*4.5
            
        elif grade == 'A0':
            sum+=float(num)*4
            
        elif grade == 'B+':
            sum+=float(num)*3.5
            
        elif grade == 'B0':
            sum+=float(num)*3
            
        elif grade == 'C+':
            sum+=float(num)*2.5
            
        elif grade == 'C0':
            sum+=float(num)*2
            
        elif grade == 'D+':
            sum+=float(num)*1.5
            
        elif grade == 'D0':
            sum+=float(num)*1
            
        elif grade == 'F':
            sum+=0

result = sum/div

print("{:.6f}".format(result))