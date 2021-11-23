def word_count(filename) :
    with open(filename) as f :
        word = f.read().split()
        word = len(word)
    return word

def sentence_count(filename) :
    with open(filename) as f :
        num = list("1234567890")
        not_sentence = 1
        data = f.read().split('.')
        for i in range(len(data)-1) :
            if data[i][len(data[i])-1] in num and data[i+1][0] in num :
                not_sentence += 1
        sentence = len(data)
        # print(data)
    return sentence - not_sentence


filename = input('File name: ')
# filename = 'input.txt'
word = word_count(filename)
sentence = sentence_count(filename)
print(f'There are {sentence} sentences and {word} words.')



