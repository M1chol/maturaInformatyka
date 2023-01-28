def czyPier(li):
    if li<2: return False
    for i in range(2,round(li**(1/2))):
        if li%i==0:
            return False
    return True

with open('trojki.txt') as dane:
    for i in dane:
        l1, l2, l3 = map(int, i.split(' '))
        if czyPier(l1) and czyPier(l2) and l1*l2==l3:
            print(i.rstrip())