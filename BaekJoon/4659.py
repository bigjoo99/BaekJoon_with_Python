result = []
word_list = []

while True:
    state = True
    word = input()
    if word == 'end':
        break
    
    word_list.append(word)
    binary_word = []
    
    for i in range(len(word)):    
        if word[i] == 'a' or word[i] == 'e' or word[i] == 'i' or word[i] == 'o' or word[i] == 'u':
             binary_word.append(1)
        else:
            binary_word.append(0)
            
    if 1 not in binary_word:
        result.append(0)
        state = False
        continue
    
    if len(word) >= 3:
        for i in range(len(word)-2):
            x = str(binary_word[i]) + str(binary_word[i+1]) + str(binary_word[i+2])
            if x == '000' or x == '111':
                result.append(0)
                state = False
                break
    
    if len(word) >= 2:
        for i in range(len(word)-1):
            x = word[i]
            if x != 'e' and x != 'o':
                if word[i] == word[i+1]:
                    result.append(0)
                    state = False
                    break
    
    if state == True:
        result.append(1)
    

for i in range(len(word_list)):
    if result[i] == 0:
        print('<'+word_list[i]+'> is not acceptable.')
    
    else:
        print('<'+word_list[i]+'> is acceptable.')