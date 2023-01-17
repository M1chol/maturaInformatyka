with open('szyfr3.txt') as dane:
    slowo=list(dane.readline().rstrip())
    klucz=[6,2,4,1,5,3]
    x=len(slowo)%len(klucz)+len(klucz)-1
    for inx_znak in range(len(slowo)-1,-1,-1):
        slowo[inx_znak], slowo[(klucz[inx_znak%len(klucz)]-1)] = slowo[(klucz[inx_znak%len(klucz)]-1)], slowo[inx_znak]
    print(''.join(slowo))