s=input("Введите слово:" )
t=len(s)
for t in range (0, t):
    if (t%2==0) and ((s[t]=='о') or (s[t]=='п') or (s[t]=='е')):
        print(s[t])
        
