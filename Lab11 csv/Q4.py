import csv

def alg(city,country) :
    with open(country) as country_file :
        data = csv.DictReader(country_file)
        countries = dict()
        for row in data :
            if row['EU'] == 'no' and row['coastline'] == 'yes' :
                if not row['country'] in countries:
                    countries[row['country']] = []
    
    with open(city) as city_file:
        data2 = csv.DictReader(city_file) 
        for row in data2 :
            if row['country'] in countries.keys() :
                countries[row['country']].append(float(row['temperature']))

        for i in countries :
            if len(countries[i]) > 0 :
                countries[i] = sum(countries[i]) / len(countries[i])
                print(f'{i} {countries[i]:.2f}')

        # อีกวิธีหนึ่ง
        # x = countries.values()
        # x = list(x)
        # # print(x)
        # avr_temp = [] 
        # for i in range(len(x)) :
        #     if len(x[i]) > 0 :
        #         tmp = sum(x[i])/len(x[i])
        #         avr_temp.append(tmp)
        #     else :
        #         avr_temp.append('nodata')
        # # print(avr_temp)
        # j = 0
        # for i in countries :
        #     if avr_temp[j] != 'nodata' :
        #         print(f'{i} {avr_temp[j]:.2f}')
        #         j += 1
        #     else :
        #         j +=1

city_file = input('Enter city file: ')
country_file = input('Enter country file: ')
# city_file = 'Cities.csv'
# country_file = 'Countries.csv'
print('Average temperature of countries having coastline, but not in EU:')
alg(city_file,country_file) 