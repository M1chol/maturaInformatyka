def czyTroj(tab):
    tab=sorted(tab)
    if tab[0]+tab[1] > tab[2]:
        return True
    return False

with open('trojki.txt') as dane:
    ciag=1
    maxciag=0
    ile=0
    for i in range(1000):
        tab=list(map(int,dane.readline().rstrip().split(' ')))
        if czyTroj(tab):
            ciag+=1
            ile+=1
        else: ciag=0
        if ciag>maxciag: maxciag=ciag
    print(maxciag, ile)