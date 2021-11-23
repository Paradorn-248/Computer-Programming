import csv

def tem(filename) :
    with open(filename) as tem_file :
        data = csv.DictReader(tem_file)
        # for i in data :
        #     print(i)
        countries = []
        temp = []
        count = []
        for row in data :
            if row['country'] not in countries :
                countries.append(row['country'])
                count.append(1)
                temp.append(float(row['temperature']))
            else :
                temp[countries.index(row['country'])] += float(row['temperature'])
                count[countries.index(row['country'])] += 1
        for i in range(len(countries)) :
            avr = temp[i] / count[i]
            print(f'{countries[i]} {avr:.2f}')



filename = input('Enter file name: ')
# filename = 'Cities.csv'
tem(filename)