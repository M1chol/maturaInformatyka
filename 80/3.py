with open('dane_trojkaty.txt') as dane:
    def czyTr(a,b,c):
        return (a+b>c) and (a+c>b) and (b+c>a)
    ile=0
    new_dane=[int(i.rstrip()) for i in dane]
    for i in range(500-2):
        for j in range(i+1,500-1):
            for k in range(j+1,500):
                if czyTr(new_dane[i], new_dane[j], new_dane[k]):
                    ile+=1
    print(ile)