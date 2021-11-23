class City:
    Country = {}
    nbCity = 0
    nbCountry = 0
    def __init__(self, city, country, latitude, longitude, temperature):
        self.city = city
        self.country = country
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.temperature = float(temperature)
        if country not in City.Country.keys():
            City.Country[country] = []
            City.nbCountry += 1
        City.Country[country].append((city, float(temperature)))
        City.nbCity += 1

def read(filename) :
    with open(filename) as f :
        datas = []
        n = 0
        for line in f :
            if n == 0 :
                n += 1
                continue
            else :
                add = line.strip().split(',')
                data = City(add[0],add[1],add[2],add[3],add[4])
                datas.append(data)
    return datas

def question(data) :
    for i in City.Country:
        sum = 0
        for j in range(len(City.Country[i])):
            sum += City.Country[i][j][1]
        print(f'{i} {sum/len(City.Country[i]):.2f}')
    print(City.nbCity,City.nbCountry)
    
filename = 'Cities.csv'
data = read(filename)
question(data)