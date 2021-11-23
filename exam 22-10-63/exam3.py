def read(filename) :
    with open(filename) as f :
        n = 0
        res = []
        for line in f :
            if n == 0 :
                n +=1
                continue
            else :
                add = line.strip().split(',')
                data = Project(add[0],add[1],add[2],add[3],add[4],add[5],add[6],add[7],add[8])
            res.append(data)
    return res

class Project :
    def __init__(self,name,platform,licens,version,language,host,size,stars,readme) :
        self.name = name
        self.platform = platform
        self.licens = licens
        self.version = int(version)
        self.language = language
        self.host = host 
        self.size = float(size)
        self.stars = int(stars)
        self.readme = readme

def answer1(data) :
    plat = dict()
    for i in range(len(data)) :
        if data[i].platform not in plat :
            plat[data[i].platform] = 1
        else :
            plat[data[i].platform] += 1
    # for i in plat :
    #     print(plat[])
    a = sorted([(v,k) for (k,v) in plat.items()])
    print(len(plat),a[len(a)-1][1],a[len(a)-2][1])

def answer2(data) :
    lice = dict()
    for i in range(len(data)) :
        if data[i].licens not in lice :
            lice[data[i].licens] = 1
        else :
            lice[data[i].licens] += 1
    # print(len(lice))
    a = sorted([(v,k) for (k,v) in lice.items()])
    print(len(lice),a[len(a)-1][1],a[len(a)-2][1])

def answer3(data) :
    pro = dict()
    for i in range(len(data)) :
        # print(data[i].version)
        if data[i].name not in pro :
            pro[data[i].name] = [data[i].version]
        else :
            pro[data[i].name].append(data[i].version)
    maxx = 0
    namee = ''
    # print(len(pro))
    for i in pro :
        # print(pro[i])
        if maxx <= pro[i][0] :
            maxx = pro[i][0]
            namee = i
    print(maxx,namee)
        
def answer4(data) :
    summ = 0
    count = 0
    for i in range(len(data)) :
        if data[i].language != 'Python' :
            summ += data[i].size
            count += 1
    print(f'{summ/count:.3f}')

def answer5(data) :
    lang = dict()
    for i in range(len(data)) :
        if data[i].host == 'GitHub' :
            if data[i].language not in lang :
                lang[data[i].language] = 1
            else :
                lang[data[i].language] += 1
    a = sorted([(v,k) for (k,v) in lang.items()])
    minn = a[0][0]
    # print(a)
    count = 0
    for i in range(len(a)) :
        if a[i][0] == minn :
            count += 1
    print(count,minn)

def answer6(data) :
    sakul = []
    for i in range(len(data)) :
        tmp = data[i].readme.split('.')
        # print(tmp)
        if tmp[1] not in  ['markdown','md','mkd'] :
            if tmp[1] not in sakul :
                # print(tmp[1])
                sakul.append(tmp[1])
    # print(sakul)
    print(len(sakul))

def answer7(data) :
    lang = ''
    lice = ''
    maxlike = 0
    for i in range(len(data)) :
        if data[i].host == 'GitHub' :
            if maxlike <= data[i].stars :
                maxlike = data[i].stars
                lang = data[i].language
                lice = data[i].licens
    print(lang,lice)

def answer8(data) :  
    count = 0
    for i in range(len(data)) :
        tmp1 = data[i].name.split('js')
        tmp2 = data[i].name.split('Js')
        tmp3 = data[i].name.split('jS')
        tmp4 = data[i].name.split('JS')
        if len(tmp1) > 1 or len(tmp2) > 1 or len(tmp3) > 1 or len(tmp4) > 1:
            count += 1
    print(count)

filename = input()
# filename = 'out1.csv'
data = read(filename)
# print(data)
answer1(data)
answer2(data)
answer3(data)
answer4(data)
answer5(data)
answer6(data)
answer7(data)
answer8(data)
