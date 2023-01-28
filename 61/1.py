with open('ciagi.txt') as dane:
    ile_arytm=0
    max_r=0
    for i in range(100):
        le = int(dane.readline())
        ciag = dane.readline().rstrip().split(' ')
        ciag = list(map(int,ciag))

        r=ciag[1]-ciag[0]
        for j in range(1,le-1):
            if ciag[j+1]-ciag[j]!=r: break
        else:
            ile_arytm +=1
            if r > max_r: max_r=r
    print(ile_arytm, max_r)