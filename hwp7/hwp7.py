def openfile(): 
    f=open(input()) 
    words = f.read() 
    words=words.replace(',','') 
    words=words.replace('.','') 
    words=words.replace('?','') 
    words=words.replace('!','') 
    words=words.replace('—','') 
    words=words.replace(':','') 
    words=words.replace('“','') 
    words=words.replace('”','') 
    words=words.replace(';','') 
    words=words.split() 
    return words 

def findness(): 
    a=[] 
    g=openfile() 
    for i in g: 
        if i.endswith('ness'): 
            a.append(i) 
    return a 

def chistota(): 
    a=findness() 
    b=[] 
    t=0
    s=len(a)
    for i in a: 
        if a.count(i)>t: 
            t=a.count(i)
            if t>1:
                s=s-t+1
                b.append(i)
    return (s,b) 

print (chistota())

