with open('quotes.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

    k = 0

    for line in lines:
        line = line.strip()
        line,trash = line.split('—',1)
        word = line.split(' ')
        for i in range(len(word)):
            if word[i] == 'разум':
                k += 1
                print(trash)
            
    print('Слово разум встречается в цитатах ',k,'раз(а)')

                
