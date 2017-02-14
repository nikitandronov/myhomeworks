import re


with open('korp.xml', 'r', encoding='utf-8') as f:
    t = f.read()
m = open('inf.txt','w', encoding='utf-8')


types = dict()

result = re.finditer('<w lemma=[^>]*>', t)
for match in result:
    match_t = match.group()
    type_t = match_t[match_t.index('type="') + 6: -2]
    if type_t in types:
        types[type_t] +=1
    else:
        types[type_text] = 1

for type_t in types:
    m.write(type_t + str(types[type_t] + '\n')
    

