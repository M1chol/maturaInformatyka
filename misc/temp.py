from itertools import compress
ciag_org=[2,4,10,6,8,1,3,7,9,5]

def nastWieksza(liczba, ciag, maska):
    t=[j>liczba for i, j in enumerate(ciag) if maska[i]]
    if any(t): return t.index(True)
    return None

for i in range(len(ciag_org)):
    ciag=ciag_org[i:]
    mask=[True for i in ciag]
    stack=[ciag[0]]
    analizowany_inx=0
    while stack:
        nast_wieksz=nastWieksza(ciag[analizowany_inx],ciag, mask)
        if nast_wieksz is not None:
            stack.append(ciag[nast_wieksz])
            analizowany_inx+=1
        else:
            stack.pop()
            mask[analizowany_inx]=False
            analizowany_inx-=1

