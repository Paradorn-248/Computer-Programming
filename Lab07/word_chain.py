text = input('Text: ').split()
len_text = len(text[0])
text += ['0'*len_text]
len_chain = 1
count_chain = 1
check = 0
max_len = 0
ch = 0
arr = []
for i in range(len(text)-1) :
    check = 0
    for j in range(len_text) :
        if text[i][j] != text[i+1][j] :
            check += 1
    if check <= 2 :
        arr.append(text[i])
        len_chain += 1
    else :
        count_chain += 1
        if ch == 0 :
            max_len = len_chain
            ch += 1
        if len_chain >= max_len :
            max_len = len_chain
        len_chain = 1
        arr.append(text[i])
        # print(arr)
        arr = []



# print(text)
print(f'{count_chain-1} Chain(s). Maximum length is {max_len} word(s).')
        
