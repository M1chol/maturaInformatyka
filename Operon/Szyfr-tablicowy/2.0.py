from string import ascii_uppercase as uper
from random import randint
with open('przyklad.txt') as dane:
    for i in dane:
        slowo=i.rstrip()
        N=6
        tekstZ=''
        var=True
        dl=len(slowo)
        start=0
        while var:
            for n in range(start, start+N):
                i=n
                while i<start+N*N:
                    if i<dl:
                        tekstZ+=slowo[i]
                    else:
                        tekstZ+=uper[randint(0,len(uper)-1)]
                        var=False
                    i+=N
            start+=N*N
    print(tekstZ)
