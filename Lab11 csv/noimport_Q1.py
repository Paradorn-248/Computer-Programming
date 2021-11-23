def reader(filename) :
    with open(filename) as f :
        head = f.readline().strip().split(',')
        data = []
        read = [line.strip().split(',') for line in f]
        for i in read :
            add = dict()
            add[head[0]] = i[0]
            add[head[1]] = float(i[1])
            add[head[2]] = i[2]
            add[head[3]] = i[3]
            data.append(add)
            # print(i)
        # print(data)
        # print(head)
        # print(read)
        # print(data)
    return data

class Country :
    def __init__(self,country,population,EU,coastline):
        self.country = country
        self.population = population
        self.EU = EU
        self.coastline = coastline
    
    def notinEUhascoastline(self) :
        for i in range(len(EU)) :
            if self.EU[i] == 'no' and self.coastline[i] == 'yes' :
                print(self.country[i],self.population[i])

filename = 'Countries.csv'
data = reader(filename)
country,population,EU,coastline = [],[],[],[]
for i in data :
    country.append(i['country'])
    population.append(i['population'])
    EU.append(i['EU'])
    coastline.append(i['coastline'])

a = Country(country,population,EU,coastline)
a.notinEUhascoastline()
