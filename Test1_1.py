with open('quotes.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

    for line in lines:
        line = line.strip()
        line,trash = line.split('—',1)
        word = line.split(' ')
        if  len(word)<10:
            print(line)
        

        
    
          
        
        
