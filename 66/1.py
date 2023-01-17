def suma(li):
    ile=0
    for i in str(li):
        ile+=int(i)
    return ile

with open('trojki.txt') as dane:
    for i in dane:
        l1, l2, l3 = map(int, i.split(' '))
        if suma(l1) + suma(l2) == l3:
            print(i.rstrip())