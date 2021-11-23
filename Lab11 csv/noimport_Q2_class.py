class City:
    nbCity = 0
    def __init__(self, city, country, latitude, longitude, temperature):
        self.city = city
        self.country = country
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.temperature = float(temperature)
        City.nbCity += 1

def read(filename):
    with open(filename) as f:
        res = []
        n = 0
        for line in f:
            if n == 0 :
                n += 1
                continue
            else :
                add = line.strip().split(',')
                s = City(add[0],add[1],add[2],add[3],add[4])
            # print(add)
                res.append(s)
    # print(res)
    return res

def result(data) :
    max,min = -999,9999
    sum = 0
    for i in range(len(data)) :
        if max <= data[i].temperature :
            max = data[i].temperature
        if min >= data[i].temperature :
            min = data[i].temperature
        sum += data[i].temperature
    return max ,min,sum/City.nbCity
        

filename = 'Cities.csv'
data = read(filename)
res1,res2,res3 = result(data)
print(f'Minimum: {res2:.2f}')
print(f'Maximum: {res1:.2f}')
print(f'Average temperature: {res3:.4f}')