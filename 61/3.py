with open('bledne.txt') as dane:
    ile_arytm=0
    max_r=0
    for i in range(100):
        le = int(dane.readline())
        ciag = dane.readline().rstrip().split(' ')
        ciag = list(map(int,ciag))

        r=[ciag[j+1]-ciag[j] for j in range(le-1)]
        if r[0]!=r[1] & r[1]==r[2]: print(ciag[0])
        if r[0]!=r[2] & r[1]!=r[2] & r[3]==r[2]: print(ciag[1])
        for j in range(le-1):
            if r[j]!=r[0]:
                print(ciag[j+1])
                break