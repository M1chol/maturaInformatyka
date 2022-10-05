with open('liczby.txt') as data:
    def iloczyn_cyfr(liczba):
        t=list(map(int, liczba[:-1]))
        iloczyn=1
        for i in t: iloczyn*=i
        return str(iloczyn)
    moc=0
    maxmoc=0
    maxl=''
    minl=''
    minmoc=0
    dict=dict([[i,0] for i in range(9)])
    for inx, liczba in enumerate(data):
        while len(liczba)>2:
            liczba=iloczyn_cyfr(liczba)+'f'
            moc+=1
        if inx==0:
            minmoc=moc
            maxmoc=moc
        if moc>maxmoc:
            maxmoc=moc
            maxl=liczba
        if moc<minmoc:
            minmoc=moc
            minl=liczba
        if moc<9:
            dict[moc]+=1
    print(dict,maxl, minl)
