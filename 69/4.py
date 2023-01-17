def geny(i):
    geny=[]
    while True:
        if 'AA' in i:
            i=i[i.index('AA'):]
        else:
            return geny
        if 'BB' in i:
            geny.append(i[:i.index('BB') + 2])
            i=i[i.index('BB') + 2:]
        else:
            return geny

with open('dane_geny.txt') as dane:
    ile_odp=0
    ile_sil_odp=0

    for i in dane:
        i=i.rstrip()
        if geny(i) == geny(i[::-1]):
            ile_odp +=1
        if i == i[::-1]:
            ile_sil_odp+=1

    print(f'ile odpornych: {ile_odp}\nile silnie odpornych: {ile_sil_odp}')