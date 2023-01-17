from string import ascii_uppercase
alf=ascii_uppercase

with open('szyfr.txt') as dane:
    tekst, klucz = [i for i in dane]
    tekst, klucz = tekst.rstrip(), klucz.rstrip()
    tekst=list(tekst)
    key_counter=0
    for i in range(len(tekst)):
        if tekst[i] == ' ' or tekst[i]==',' or tekst[i]=='.':
            continue
        tekst[i]=alf[(alf.index(tekst[i])-alf.index(klucz[key_counter%len(klucz)]))%len(alf)]
        key_counter+=1
    print(''.join(tekst))