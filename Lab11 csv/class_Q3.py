import csv

class City :
    def __init__(self,city,country,latitude,longitude,temperature) :
        self.city = city
        self.country = country
        self.latitude = latitude
        self.longitude = longitude
        self.temperature = temperature

    def avr_temp(self) :
        tem = dict()
        for i in range(len(country)) :
            if self.country[i] not in tem :
                tem[self.country[i]] = self.temperature[i]
            else :
                tem[self.country[i]] += self.temperature[i]

        for i in tem :
            print(f'{i} {tem[i]/self.country.count(i):.2f}')

filename = input('Enter file name: ')
# filename = 'Cities.csv'
city,country,latitude,longitude,temperature = [],[],[],[],[]
with open(filename) as city_file :
    data = csv.DictReader(city_file)
    for row in data :
        city.append(row['city'])
        country.append(row['country'])
        latitude.append(float(row['latitude']))
        longitude.append(float(row['longitude']))
        temperature.append(float(row['temperature']))

a = City(city,country,latitude,longitude,temperature)
a.avr_temp()