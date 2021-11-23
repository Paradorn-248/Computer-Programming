import json

def read_json(filename) :
    with open(filename) as f :
        data = f.read()
        data = json.loads(data)
    return data

def menu(m,data) :
    if m == '1' :
        print(len(data))

    if m == '2' :
        res = []
        for i in range(len(data)):
            if data[i]['author'] not in res :
                res.append(data[i]['author'])
        print(len(res))

    if m == '3' :
        user = []
        tweet = []
        for i in range(len(data)) :
            if data[i]['author'] not in user :
                user.append(data[i]['author'])
                tweet.append(1)
            else :
                tweet[user.index(data[i]['author'])] += 1
        
        max1 = max(tweet)
        for i in range(len(user)) :
            if max1 == tweet[i] :
                print(user[i])

    if m == '4' :
        topic = []
        for i in range(len(data)) :
            if data[i]['topic'] not in topic :
                topic.append(data[i]['topic'])
        print(len(topic))

    if m == '5' :
        count = 0
        for i in range(len(data)) :
            if data[i]['topic_priority'] == 'ALERT' :
                count += 1 
        print(count)

    if m == '6' :
        count = 0
        for i in range(len(data)) :
            if data[i]['topic_priority'] == 'UNIMPORTANT' :
                count += 1 
        print(count)

    if m == '7' :
        count = 0
        for i in range(len(data)) :
            if data[i]['language'] != 'EN' :
                print(True)
        print(False)

    if m == '8' :
        max_word = 0
        for i in range(len(data)) :
            if max_word <= len(data[i]['text'].split()) :
                max_word = len(data[i]['text'].split())
        print(max_word)

filename = input('File name: ')
# filename = 'twitter.json'
data = read_json(filename)
print(data)
m = input('input: ')
menu(m,data)
