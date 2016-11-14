word = input ('Введите слово: ')
vocab = []

while word:
    vocab.append(word)
    word = input('Введите слово: ')

for i in range (len(vocab)):
    if len(vocab[i]) > 5:
        print(vocab[i])

        

    
	
