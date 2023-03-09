def czy_pal(liczba):
    if liczba == ''.join(list(reversed(liczba))): return True
    return False

def do_systemow(liczba: int) -> list:
    dg='0123456789ABCDEF'
    wynik=[]
    for system in range(2,17):
        liczba_copy=liczba
        ret_liczba=''
        while liczba_copy>0:
            ret_liczba+=dg[liczba_copy%system]
            liczba_copy//=system
        wynik.append(''.join(list(reversed(ret_liczba))))
    return wynik

wszystko=[]
with open('dane.txt') as dane:
    for liczba in dane:
        temp=[0 for i in range(15)]
        liczba = int(liczba.rstrip())
        for inx, liczba_system in enumerate(do_systemow(liczba)):
            if czy_pal(liczba_system): temp[inx]+=1
        wszystko.append((liczba, temp))
wszystko = sorted(wszystko, key=lambda x: sum(x[1]), reverse=True)[:3]
for i in wszystko:
    print(i[0], sum(i[1]),' ', end='')
    for inx, j in enumerate(i[1]):
        if j==1: print(inx+2, end=' ')
    print('')