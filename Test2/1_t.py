import re


with open('korp.xml', 'r', encoding='utf-8') as f:
    t = f.read()

m = re.findall('title',t)
b = str(m)
t = b.count('i')

with open('infa.txt', 'w') as d:
    d.write('Число вхождений заголовка XML = ' + str(t))

print('Вы молодец - см.файд infa')
