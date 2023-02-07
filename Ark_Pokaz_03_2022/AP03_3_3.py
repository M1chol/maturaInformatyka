def czy_pier(liczba):
    if liczba<2:
        return False
    for i in range(2, int(liczba**(1/2))+1):
        if liczba%i==0:
            return False
    return True

with open('liczby.txt') as dane:
    ile=0
    for line in dane:
        M, a, b = line.split()
        if czy_pier(int(M)): ile+=1
    print(ile)