S = input()

cnt_0 = S.count('0')
cnt_1 = S.count('1')

new_S = ''

for i in range(int(cnt_0/2)):
    new_S+='0'
    
for i in range(int(cnt_1/2)):
    new_S+='1'
    
print(new_S)
