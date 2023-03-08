def czy_pal(liczba):
    if liczba == ''.join(list(reversed(liczba))): return True
    return False

ile=0
with open('dane.txt') as dane:
    for liczba in dane:
        liczba=int(liczba.rstrip())
        l=hex(liczba)[2:]
        if czy_pal(l):
            ile+=1
print(ile)