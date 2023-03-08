def czy_pal(liczba):
    l1=liczba
    l2=0
    while liczba>0:
        l2+=liczba%10
        liczba//=10
        l2*=10
    if l1==l2//10: return True
    return False

ile=0
with open('dane.txt') as dane:
    for liczba in dane:
        liczba=liczba.rstrip()
        if sorted(set(liczba))==['0','1'] and czy_pal(int(liczba)):
            ile+=1
print(ile)