text = input('Text: ') 
substring = input('Substring: ')
# text = 'Hey jude Don’t make it bad'
# substring = 'ude'

# print(text)
# print(substring)
len_text = len(text)
len_substring = len(substring)
# print(text[0:len_substring])
i = 0
j = 0
res = text
while i < len_text :
    if text[i:i+len_substring] == substring :
        res = res[:j]+'['+res[j:j+len_substring]+']'+res[j+len_substring:]
        j += len_substring + 2
        i += len_substring

    else :
        i += 1
        j += 1

print(res)