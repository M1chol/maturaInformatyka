from fractions import Fraction
with open('dane_ulamki.txt') as dane:
    ile=0
    for i in dane:
        l1, l2 = map(int,i.split(' '))
        l3 = Fraction(l1,l2).as_integer_ratio()[0]
        ile+=l3
    print(ile)