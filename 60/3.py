from math import gcd
with open('liczby.txt') as plik:
    dane=[int(i) for i in plik]
    new=[]
    for i in range(len(dane)):
        for j in range(len(dane)):
            if j==i: continue
            if gcd(dane[i],dane[j])!=1:
                break
        else:
            new.append(dane[i])
    print(max(new))

