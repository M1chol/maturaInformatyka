with open('szyfr1.txt') as dane:
    slowa=[i for i in dane]
    klucz=list(map(int,slowa.pop().split()))
    for slow in slowa:
        slow=list(slow.rstrip())
        for inx_znak in range(len(slow)):
            slow[inx_znak], slow[(klucz[inx_znak%len(klucz)]-1)] = slow[(klucz[inx_znak%len(klucz)]-1)], slow[inx_znak]
        print(''.join(slow))