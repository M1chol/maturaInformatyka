with open('dane_geny.txt') as dane:
    ile=0
    maxLen=0
    maxGen=0
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
        if len(geny)>maxGen: maxGen=len(geny)
        j=[len(i) for i in geny]
        if max(j)>maxLen:maxLen=max(j)
    print(f'najwięcej genów: {maxGen}\nnajwiększa długość {maxLen}')
