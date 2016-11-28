word = input ('Введите слово: ')
vocab = []
k = ' '
h = 0
i = 0

for i in range (len(word) + 1):
    k = word[0:h]
    vocab.append(k)
    h += 1
    

for i in range (len(vocab)):
    print(vocab[i])
