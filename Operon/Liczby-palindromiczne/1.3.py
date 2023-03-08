def czy_pal(liczba):
    if liczba == ''.join(list(reversed(liczba))): return True
    return False

def do_systemow(liczba: int) -> list:
    dg='0123456789ABCDEF'
    wynik=[]
    for system in range(2,17):
        if system == 10:
            wynik.append(str(liczba))
            continue
        liczba_copy=liczba
        ret_liczba=''
        while liczba_copy>0:
            ret_liczba+=dg[liczba_copy%system]
            liczba_copy//=system
        wynik.append(''.join(list(reversed(ret_liczba))))
    return wynik


print(do_systemow(246))

temp=[0 for i in range(15)]
with open('dane.txt') as dane:
    for liczba in dane:
        liczba = int(liczba.rstrip())
        for inx, liczba_system in enumerate(do_systemow(liczba)):
            if czy_pal(liczba_system): temp[inx]+=1
print(temp)