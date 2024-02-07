n = int(input())

word = list(input())
result = 0

for _ in range(n-1):
    s = input()
    word_x = word[:]
    cnt = 0
        
    for x in s:
        if x in word_x:
            word_x.remove(x)
        else:
            cnt += 1
    
    if cnt < 2 and len(word_x) < 2:
        result += 1
        
print(result)