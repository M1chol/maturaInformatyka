with open('dane_napisy.txt') as dane:
    ile=0
    for i in dane:
        a, b = i.rstrip().split(' ')
        if len(a)==len(b):
            if sorted(a)==sorted(b):
                ile+=1
    print(ile)