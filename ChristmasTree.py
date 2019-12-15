from time import sleep
from random import randint
import shutil
width = shutil.get_terminal_size().columns

md2=randint(1,30)
def gentree():
    print('\033c')
    for x in range(1,30,2):
        md1=randint(1, md2)
        if x==1:
            ch='$'
            print("\x1b[33m{:^33}\x1b[0m".format(ch*x).center(width))
            continue
        if md1%4==0:
            ch='o'
            print("\x1b[34m{:^33}\x1b[0m".format(ch*x).center(width))
            continue
        if md1%3==0:
            ch='i'
            print("\x1b[31m{:^33}\x1b[0m".format(ch*x).center(width))
            continue
        else: 
            ch='*'
        print("\x1b[32m{:^33}\x1b[0m".format(ch*x).center(width))
    print("\x1b[33m{:^33}\x1b[0m".format('||').center(width))
    print("\x1b[33m{:^33}\x1b[0m".format('||').center(width))
    sleep(.75)

while True:
    gentree()
