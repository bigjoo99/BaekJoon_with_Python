S = input()

x = 1
s = set()

while x <= len(S):
    for i in range(len(S)-x+1):
        string = ''
        string += S[i:i+x]
        s.add(string)
    x+=1
    
print(len(s))     


