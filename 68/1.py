with open('dane_napisy.txt') as dane:
    ile=0
    for i in dane:
        a, b = i.rstrip().split(' ')
        if a.count(a[0]) == len(a) and b.count(b[0])==len(b) and a==b:
            ile+=1
    print(ile)