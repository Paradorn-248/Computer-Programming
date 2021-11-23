import json

def read_data(filename) :
    with open(filename) as f :
        data = [json.loads(line) for line in f]
    return data

def menu(m,data) :
    if m == '1' :
        print(len(data))
    
    if m == '2' :
        res = []
        for i in range(len(data)) :
            if data[i]['reviewerID'] not in res :
                res.append(data[i]['reviewerID'])
        print(len(res))

    if m == '3' :
        res = []
        for i in range(len(data)) :
            if data[i]['productID'] not in res :
                res.append(data[i]['productID'])
        print(len(res))

    if m == '4' :
        res = []
        for i in range(len(data)) :
            tmp = data[i]['category'].split('>')
            if tmp[0] not in res :
                res.append(tmp[0])
        # print(res)        
        print(len(res))

    if m == '5' :
        res = []
        for i in range(len(data)) :
            tmp = data[i]['category'].split('>')
            if tmp[1] not in res :
                res.append(tmp[1])
        # print(res)        
        print(len(res))

    if m == '6' :
        name = []
        max_arr = []
        for i in range(len(data)) :
            if data[i]['reviewerID'] not in name :
                name.append(data[i]['reviewerID'])
                max_arr.append(1)
            else :
                max_arr[name.index(data[i]['reviewerID'])] += 1
        
        max_nub = max(max_arr)
        print(name[max_arr.index(max_nub)])

    if m == '7' :
        product = []
        nub = []
        score = []
        res = []
        for i in range(len(data)) :
            if data[i]['productName'] not in product :
                product.append(data[i]['productName'])
                nub.append(1)
                score.append(data[i]['overall'])
            else :
                score[product.index(data[i]['productName'])] += data[i]['overall']
                nub[product.index(data[i]['productName'])] += 1

        for i in range(len(score)) :
            ovr = score[i] / nub[i]
            res.append(ovr)
        max1 = max(res)
        # print(max1)
        max_nub = 0
        # print(res)
        for i in range(len(res)) :
            if max1 == res[i] :
                if max_nub <= nub[i] :
                    max_nub = nub[i]
        # print(max_nub)
        for i in range(len(res)) :
            if max1 == res[i]:
                if nub[i] == max_nub :
                    print(product[i])

    if m == '8' :
        product = []
        nub = []
        len_word = []
        res = []
        for i in range(len(data)) :
            if data[i]['productName'] not in product :
                product.append(data[i]['productName'])
                nub.append(1)
                len_word.append(len(data[i]['reviewText']))
            else :
                len_word[product.index(data[i]['productName'])] += len(data[i]['reviewText'])
                nub[product.index(data[i]['productName'])] += 1

        for i in range(len(len_word)) :
            tmp = len_word[i] / nub[i]
            res.append(tmp)
        max_word = max(res)

        for i in range(len(res)) :
            if  max_word == res[i] :
                print(product[i])
        
 
# filename = input('file name: ')
filename = 'amazon1.json'
data = read_data(filename)
m = input('input: ')
menu(m,data)
