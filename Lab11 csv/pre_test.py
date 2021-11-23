import re

class Student:
    nbStudent = 0
    stdWithNB = 0
    def __init__(self, timestamp, email, name, id, notebook, mac, a4):
        self.timestamp = timestamp.strip()
        self.email = email.strip()
        self.name = name.strip()
        self.id = id.strip()
        if notebook == 'ต้องการเอามาเอง':
            self.notebook = 'yes'
            Student.stdWithNB += 1
        else:
            self.notebook = 'using E201 PC'
        self.mac = mac.strip()
        self.a4 = a4.strip()
        Student.nbStudent += 1


def readCSV(filename, DEBUG=False): #'notebook_response.csv'
    with open(filename,encoding='utf-8') as f :
        head = f.readline().strip().split(',')
        data = [line.strip().split(',') for line in f]
        student = []
        for i in range(len(data)) :
            add = Student(data[i][0],data[i][1],data[i][2],data[i][3],data[i][4],data[i][5],data[i][6])
            student.append(add)
    return student

def readStd(filename): #'std_CPE34_63.csv'
    with open(filename,encoding='utf-8') as f :
        data = [line.strip().split(',') for line in f]
    return data

def cleanMac(m):
    string = ''
    m = m.upper()
    if len(m.split(':')) == 6 :
        return m
    if len(m) == 12 :
        string = m[0]+m[1]+':'+m[2]+m[3]+':'+m[4]+m[5]+':'+m[6]+m[7]+':'+m[8]+m[9]+':'+m[10]+m[11]
    if m == '':
        string = m + ' <-- NOT ALLOWED'
    # print(m.split('-'))
    if len(m.split('-')) == 6 :
        tmp = m.split('-')
        # print(tmp)
        for j in range(len(tmp)) :
            string += tmp[j]+':'
        string = string[:-1]
    if len(string) != 17 :
        string = m + ' <-- NOT ALLOWED'
    return string

def whoComeWithNoteBook(s, stdDico): #class std
    res = '<html><head><meta charset="utf8"><title>CPE43 Notebook Questionaire</title></head><body>\n'
    nub = 0
    # print(s[0].id)
    for i in range(len(s)) :
        for j in range(len(stdDico)) :
            # s[i].mac = 
            if s[i].id == stdDico[j][1] :
                if s[i].notebook == 'yes' :
                    nub += 1
                    url = f'[<a target="_blank" href="http://earth.mikelab.net:8080/~{stdDico[j][9].lower()}/">{stdDico[j][9].lower()}</a>]'
                    res += f'{nub:02} {url} {s[i].timestamp} {s[i].id} {s[i].name} comes to lab03 exam with notebook {cleanMac(s[i].mac)}<br>\n'
                break
    for i in range(len(s)) :
        for j in range(len(stdDico)) :
            # s[i].mac = 
            if s[i].id == stdDico[j][1] :
                if s[i].notebook == 'using E201 PC' :
                    if s[i].mac == '' :
                        nub += 1
                        url = f'[<a target="_blank" href="http://earth.mikelab.net:8080/~{stdDico[j][9].lower()}/">{stdDico[j][9].lower()}</a>]'
                        res += f'{nub:02} {url} {s[i].timestamp} {s[i].id} {s[i].name} comes to lab03 exam, using E201 PC<br>\n'
                    break
    res += '<br></body></html>'
    return res

def htmlWrap(s, fn, DEBUG=False):
    with open(fn,'w',encoding='utf-8') as f:
        f.write(s)

# Main begins here
filename = 'notebook_response.csv'
std_fn = 'std_CPE34_63.csv'
myStudents = readCSV(filename)
stdDico = readStd(std_fn)
result = whoComeWithNoteBook(myStudents, stdDico)
print(result)
print('--Done..')
# write a html file
htmlWrap(result, 'cpe34_nb.html')
print('http://earth.mikelab.net:8080/cpe34nb.html')
print('FORK version')