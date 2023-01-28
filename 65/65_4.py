with open('dane_ulamki.txt') as dane:
    b=4*9*25*49*13
    ile=0
    for i in dane:
        l1, l2 = map(int,i.split(' '))
        t=b//l2
        ile+=l1*t
    print(ile)