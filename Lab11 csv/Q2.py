import csv

def tem(filename) :
    with open(filename) as tem_file :
        data = csv.DictReader(tem_file)
        # for i in data :
        #     print(i)
        max_tem = 0
        sum,count = 0,0
        min_tem = 999
        for row in data :
            if float(row['temperature']) >= max_tem :
                max_tem = float(row['temperature'])
            if min_tem >= float(row['temperature']) :
                min_tem = float(row['temperature'])
            sum += float(row['temperature'])
            count += 1
        avr = sum / count
        print(f'Minimum: {min_tem:.2f}')
        print(f'Maximum: {max_tem:.2f}')
        print(f'Average temperature: {avr:.4f}')


filename = input('Enter file name: ')
# filename = 'Cities.csv'
tem(filename)