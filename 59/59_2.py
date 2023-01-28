with open('liczby.txt') as data:
    ile=0
    for liczba in data:
        liczba=int(liczba)
        liczba_rev=int(''.join((list(reversed(list(str(liczba)))))))
        suma=liczba+liczba_rev
        suma_rev=int(''.join((list(reversed(list(str(suma)))))))
        if suma == suma_rev:
            ile+=1
    print(ile)

