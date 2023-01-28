with open('ciagi.txt') as dane:
    temp = []
    for i in range(100):
        li = int(dane.readline())
        ciag = dane.readline().rstrip().split(' ')
        ciag = list(map(int, ciag))

        for liczba in ciag:
            pierw=round(liczba ** (1. / 3))
            if pierw**3 == liczba:
                temp.append(liczba)
        if temp:
            print(max(temp))

        temp=[]