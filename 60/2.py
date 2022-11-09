with open('liczby.txt') as plik:
    ile2=0
    for i in plik:
        i=int(i)
        ile=2
        l=[1,i]
        for j in range(2,i//2+1):
            if i%j==0:
                ile+=1
                l.append(j)
            if ile>18: pass
        if ile==18:
            print(i, l)