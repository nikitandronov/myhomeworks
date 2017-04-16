


with open('викинги.txt', 'r', encoding='utf-8') as f:
    t = f.read()

m = re.sub(u'викинг', u'бурундук',t)
m = re.sub(u'Викинг', u'Бурундук',m)

with open('vysupir.txt', 'w', encoding='utf-8') as d:
    d.write(m)

print('Вы молодец - см.файд vysupir')
