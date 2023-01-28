def czyTroj(tab):
    tab = sorted(tab)
    if tab[0]**2+tab[1]**2 == tab[2]**2:
        return True
    return False

with open('trojki.txt') as dane:
    ilepar=0
    for i in range(999):
        if i == 0:
            temp = list(map(int, dane.readline().rstrip().split(' ')))
        tab2=list(map(int,dane.readline().rstrip().split(' ')))
        if czyTroj(temp) and czyTroj(tab2):
            print(temp,tab2)
        temp=tab2