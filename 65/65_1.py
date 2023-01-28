from fractions import Fraction
with open('dane_ulamki.txt') as dane:
    liczby=[]
    for l in dane:
        l1 ,l2 = map(int,(l.rstrip().split(' ')))
        liczby.append((Fraction(l1,l2),l1,l2))
    print(min(liczby, key=lambda x: x[0]))