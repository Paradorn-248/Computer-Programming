import csv

class Country :
    def __init__(self,country,population,EU,coastline) :
        self.country = country
        self.population = population
        self.EU = EU
        self.coastline = coastline
    
    def is_eu_not_coastline(self) :
        res = []
        for i in range(len(self.country)) :
            if self.EU[i] == 'no' and self.coastline[i] == 'yes' :
                res.append(self.country[i] + ' ' + str(self.population[i]))
        for i in res :
            print(i)

filename = input('Enter File name: ')
# filename = 'Countries.csv'
with open(filename) as country_file :
    data = csv.DictReader(country_file)
    country,population,EU,coastline= [],[],[],[]
    for row in data :
        country.append(row['country'])
        population.append(float(row['population']))
        EU.append(row['EU'])
        coastline.append(row['coastline'])

a = Country(country,population,EU,coastline)
a.is_eu_not_coastline()