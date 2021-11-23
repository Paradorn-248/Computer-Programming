import csv

def read_csv(filename) :
    with open(filename) as country_file :
        data = csv.DictReader(country_file)   
        # print(data)
        countries = []
        populations = []
        for row in data :
            if row['EU'] == 'no' and row['coastline'] == 'yes' :
                countries.append(row['country'])
                populations.append(row['population'])
            print(row)
        # print(countries)
            
        for i in range(len(countries)) :
            print(countries[i],populations[i])

# filename = input('Enter File name: ')
filename = 'Countries.csv'
read_csv(filename)