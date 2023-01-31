def czy_szach(lis):
    global bszach
    global cszach
    lis=[''.join(list(map(lambda x: x if x!='.' else '',i))) for i in lis]
    for uklad in lis:
        if 'kW' in uklad or 'Wk' in uklad:
            bszach+=1
        if 'wK' in uklad or 'Kw' in uklad:
            cszach+=1

with open('szachy.txt') as dane:
    bszach=0
    cszach=0
    for i in range(125):
        kol=[[] for _ in range(8)]
        for j in range(9):
            wiersz=''
            if j==9:
                dane.readline()
                continue
            for inx, pion in enumerate(list(dane.readline().rstrip())):
                kol[inx]+=pion
                wiersz+=pion
            czy_szach([wiersz])
        czy_szach(kol)
    print(bszach,cszach)
