def read(filename) :
    with open(filename) as f :
        data = f.read()
        # print(data)
    return data

def sentence(data) :
    sentence_list = data.split('.')
    num = list("012346789")
    len_sentence = len(sentence_list)
    not_sentence = 1
    for i in range(len_sentence-1) :
        if sentence_list[i][len(sentence_list[i])-1] in num and sentence_list[i+1][0] in num :
            not_sentence += 1
    # print(sentence_list)
    # print(len_sentence - not_sentence)
    return len_sentence - not_sentence

def word(data) :
    word_list = data.split(' ')
    return len(word_list)


# filename = 'input.txt'
filename = input('File name: ')
data = read(filename)
s = sentence(data)
w = word(data)
print(f'There are {s} sentences and {w} words.',end = '')