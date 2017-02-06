import re


with open('city.html', 'r', encoding='utf-8') as f:
    t = f.read()

m = re.findall('UTC.[0-1]?[0-9]:[0:5][0:9]',t)
b = 'Часовой пояс' + ' ' + str(m)

with open('infa.txt', 'w') as d:
    d.write(b)

print('Вы молодец - см.файд infa')
