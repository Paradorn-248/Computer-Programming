import csv

class City :
    def __init__(self,city,country,latitude,longitude,temperature) :
        self.city = city
        self.country = country
        self.latitude = latitude
        self.longitude = longitude
        self.temperature = temperature

    def temp(self) :
        max_temperature = max(self.temperature)
        min_temperature = min(self.temperature)
        avr_temperature = sum(self.temperature) / len(self.temperature)
        print(f'Minimum: {min_temperature:.2f}')
        print(f'Maximum: {max_temperature:.2f}')
        print(f'Average temperature: {avr_temperature:.4f}')

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
a.temp()