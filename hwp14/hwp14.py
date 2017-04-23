import os

for d, dirs, files in os.walk('C:\\hwp'):
    for f in files:
        if f.find('[а-я]*]')!= -1:
            print(f)
