import string as st
alf=st.ascii_lowercase

def koduj(slowo, klucz):
    return ''.join([alf[(alf.index(j) * klucz[0] + klucz[1]) % 26] for j in slowo])

def znajdzSzyfr(orginal, zaszyfrowane):
    temp=''
    A=0
    B=0
    while temp != zaszyfrowane:
        B+=1
        if B > 25:
            B=0
            A+=1
        if A > 25:
            raise Exception('brak klucza w przedziale')
        temp=koduj(orginal, (A, B))
    else:
        return A, B

with open('probka.txt') as dane:
    odp=[]
    for linia in dane:
        slowo, kod = linia.split()
        print(f'Szyfrujący: {znajdzSzyfr(slowo, kod)} Deszyfrujący: {znajdzSzyfr(kod, slowo)}')

