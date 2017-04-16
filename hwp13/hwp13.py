import os

folder = 'C:\\hwp\\'
print(os.listdir(folder))

for f in os.listdir(folder):
     with open(os.path.join(folder, f)) as text:
        if f.isalpha():
            print(f)
