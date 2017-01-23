import csv

with open('example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    d = {}
    for row in readCSV:
        d[row[0]] = row[1]

    for key in d.keys():
        c = d.get(key)
        i = 0
        m = ''
        while i < len(key):
            m = m + '.'
            i+=1
        print(c+' ' + m)        
        f = input()
        if f == key :
            print('Верно')
        else:
            print('Неверно')
            
