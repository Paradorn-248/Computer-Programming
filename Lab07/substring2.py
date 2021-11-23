text = input('Text: ')
res = text
len_text = len(text)
substring = input('Substring: ')

len_substring = len(substring)
i,j = 0,0

while i < len_text :
    arr = []
    if text[i:i+len_substring] == substring :
        res = res[:j]+'['+res[j:j+len_substring]+']'+res[j+len_substring:]
        j += len_substring + 2
        i += len_substring
    
    elif text[i:i+len_substring] != substring:
        for k in range(len_substring) :
            check = 0
            if text[i] != substring[k] :
                check += 1
                arr.append(k)

            if check <= 2 :
                res = res[:j]+'['+res[j:j+len_substring]+']'+res[j+len_substring:]
                for l in range(len(arr)) :
                    res = res.replace(res[arr[l]],'?')
                j += len_substring + 2
                i += len_substring

    else :
        i += 1
        j += 1

print(res)