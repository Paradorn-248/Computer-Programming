class Country:
  nbCountry = 0
  def __init__(self, country, population, EU,coastline):
    self.country = country
    self.population = float(population)
    self.EU = EU
    self.coastline = coastline
    Country.nbCountry += 1

class City:
  nbCity = 0
  def __init__(self, city, country, latitude, longitude, temperature):
    self.city = city
    self.country = country
    self.latitude = float(latitude)
    self.longitude = float(longitude)
    self.temperature = float(temperature)
    City.nbCity += 1

def read_country(filename) :
    with open(filename) as f :
        n = 0
        res = []
        for line in f :
            if n == 0 :
                n += 1
                continue
            else :
                add = line.strip().split(',')
                data = Country(add[0],add[1],add[2],add[3])
            res.append(data)
    return res

def read_city(filename) :
    with open(filename) as f :
        n = 0
        res = []
        for line in f :
            if n == 0 :
                n += 1
                continue
            else :
                add = line.strip().split(',')
                data = City(add[0],add[1],add[2],add[3],add[4]) 
                res.append(data)
    return res

def question(dcity,dcountry) :
    res = dict()
    for i in range(len(dcity)) :
        for j in range(len(dcountry)) :
            if dcity[i].country == dcountry[j].country and dcountry[j].EU == 'no' and dcountry[j].coastline == 'yes' :
                if dcity[i].country not in res :
                    res[dcity[i].country] = [dcity[i].temperature]
                else :
                    res[dcity[i].country].append(dcity[i].temperature)
    # co = []
    # avr_tem = []
    # for i in res :
    #     co.append(i)
    # co = sorted(co)
    # for i in co :
    #     avr_tem.append(res[i])
    # for i in range(len(avr_tem)) :
    #     avr_tem[i] = sum(avr_tem[i])/len(avr_tem[i])
    # for i in range(len(co)) :
    #     print(f'{co[i]} {avr_tem[i]:.2f}')    
    # print(res)

    b = {i:res[i] for i in sorted(res)}
    # print(b)
    for i in b :
        print(f'{i} {sum(b[i])/len(b[i]):.2f}')

city_file = 'Cities.csv'
country_file = 'Countries.csv'
data_city = read_city(city_file)
data_country = read_country(country_file)
question(data_city,data_country)