def czyPier(liczba):
    if liczba<2: return False
    for i in range(2,round(liczba**(1/2)+1)):
        if liczba%i==0:
            return False
    return True

with open('ciagi.txt') as dane:
    maxPier=0
    minPier=0
    ile=0
    for inx, ciag in enumerate(dane):
        ciag = ciag.rstrip()
        liczba=int(ciag,2)
        for i in range(2,liczba//2+1):
            if liczba%i==0 and czyPier(i) and czyPier(liczba/i):
                if inx==0: minPier=liczba;maxPier=liczba
                if liczba>maxPier: maxPier=liczba
                if liczba<minPier: minPier=liczba
                ile+=1
                break
    print(ile, maxPier, minPier)