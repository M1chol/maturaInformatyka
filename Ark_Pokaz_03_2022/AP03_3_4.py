from math import gcd
with open('liczby.txt') as dane:
    ile=0
    for line in dane:
        M, a, b = line.split()
        if gcd(int(M), int(a))==1:
            ile+=1
    print(ile)