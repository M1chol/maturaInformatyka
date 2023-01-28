with open('wspolrzedne.txt') as dane:
    def wieksze(i): return 1 if int(i)>0 else 0
    ile=0
    for line in dane:
        if all(map(wieksze, line.split())):
            ile+=1
    print(ile)
