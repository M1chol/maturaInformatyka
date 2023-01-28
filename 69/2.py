with open('dane_geny.txt') as dane:
    ile=0
    for i in dane:
        geny=[]
        i=i.rstrip()
        while True:
            if 'AA' in i:
                i=i[i.index('AA'):]
            else:
                break
            if 'BB' in i:
                geny.append(i[:i.index('BB')+2])
                i=i[i.index('BB')+2:]
            else:
                break
        for j in geny:
            if 'BCDDC' in j:
                ile+=1
    print(ile)