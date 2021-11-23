def reader(filename) :
    with open(filename) as f :
        head = f.readline().strip().split(',')
        data = []
        read = [line.strip().split(',') for line in f]
        for i in read :
            add = Country(i[0],float(i[1]),i[2],i[3])
            data.append(add)
            # print(i)
        # print(data)
        # print(head)
        # print(read)
    return data

class Country :
    def __init__(self,country,population,EU,coastline):
        self.country = country
        self.population = population
        self.EU = EU
        self.coastline = coastline
    
def notinEUhascoastline(data) :
    res = []
    for i in range(len(data)) :    
        char = ''
        if data[i].EU == 'no' and data[i].coastline == 'yes' :
            char += f'{data[i].country} {data[i].population}'
            res.append(char)
    return res


filename = 'Countries.csv'
data = reader(filename)
res = notinEUhascoastline(data)
for i in res :
    print(i)