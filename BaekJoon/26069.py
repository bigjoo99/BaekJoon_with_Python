n = int(input())

dict = {'ChongChong'}

for _ in range(n):
    s1, s2 = input().rstrip().split()
    
    if s1 in dict:
        dict.add(s2)
    
    if s2 in dict:
        dict.add(s1)
        
print(len(dict))