from fractions import Fraction
with open('dane_ulamki.txt') as dane:
    ile=0
    for i in dane:
        l1, l2 = map(int,i.rstrip().split(' '))
        l3, l4 = Fraction(l1,l2).as_integer_ratio()
        if l1 == l3 and l2 == l4:
            ile+=1
    print(ile)