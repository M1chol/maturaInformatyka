import time
with open('liczby.txt') as dane:
    """ile=0
    b=True
    for i in dane:
        i=i.rstrip()
        if i[0]==i[-1]:
            if b:
                print(i)
                b=False
            ile+=1
    print(ile)"""

    """
    def czyPierw(liczba):
        if liczba<2: return False
        for i in range(2, int(liczba**(1/2))+1):
            if liczba%i==0: return False
        return True

    def rozklad(liczba):
        i=2
        t=[]
        while liczba>1:
            if liczba%i==0:
                t.append(i)
                liczba//=i
            else:
                i+=1
            while not czyPierw(i):
                i+=1
        return t

    maxczyn=0
    maxroz=0
    liczba1, liczba2='', ''
    for i in dane:
        i=int(i.rstrip())
        c=rozklad(i)
        lczyn = len(c)
        lroz=len(list(set(c)))
        if lczyn>maxczyn:
            maxczyn=lczyn
            liczba1=i
        if lroz>maxroz:
            maxroz=lroz
            liczba2=i
    print(f'{liczba1}: {maxczyn}, {liczba2}: {maxroz}')
    """
    start = time.time()
    t=[int(i.rstrip()) for i in dane]
    t=sorted(t)
    ile=0
    for i in range(len(t)):
        for j in range(i+1, len(t)):
            for k in range(j+1, len(t)):
                for l in range(k+1, len(t)):
                    for m in range(l+1, len(t)):
                        if t[j]%t[i]==0 and t[k]%t[j]==0 and t[l]%t[k]==0 and t[m]%t[l]==0:
                            ile+=1
    print(ile)
    print(time.time()-start)