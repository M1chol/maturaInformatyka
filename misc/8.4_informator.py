#zadanie 8.4 z informatora maturalnego https://arkusze.pl/informatory/informator-maturalny-informatyka-2023.pdf
def nastWieksza(liczba, ciag):
    t=[i>liczba for i in ciag]
    if any(t): return t.index(True)
    return None

with open('dane8.txt') as dane:
    #ciag=[int(i.rstrip()) for i in dane]
    ciag_rosn=[]
    max_len=1
    last_inx=[]
    ciag=[2, 4, 10, 6, 8, 1, 3, 7, 9, 5]
    mask=[True for i in ciag]
    for i in range(len(ciag) - 1):
        ciag_copy=ciag.copy()
        ciag_rosn.append(ciag_copy[i])
        last_inx.append(i)
        j=i
        while True:
            ciag_copy_masked=[i[1] for i in enumerate(ciag_copy) if mask[i[0]]]
            nast_wieksza=nastWieksza(ciag_copy_masked[j], ciag_copy_masked[j + 1:])
            if nast_wieksza is None:
                if len(last_inx)==1: break
                ciag_rosn=ciag_rosn[:-1]
                mask[last_inx.pop()]=False
                j=last_inx[-1]
            else:
                ciag_rosn.append(ciag_copy_masked[nast_wieksza + j + 1])
                j=nast_wieksza+j+1
                last_inx.append(j)
            if len(ciag_rosn)>max_len: max_len=len(ciag_rosn)
        ciag_rosn=[]
        last_inx=[]
    print(max_len)
