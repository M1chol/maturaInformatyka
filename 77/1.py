from string import ascii_uppercase
alf=ascii_uppercase
klucz='LUBIMYCZYTAC'
with open('dokad.txt') as dane:
    tekst=list(dane.readline())
    key_counter=0
    for i in range(len(tekst)):
        if tekst[i] == ' ' or tekst[i]==',' or tekst[i]=='.':
            continue
        tekst[i]=alf[(alf.index(tekst[i])+alf.index(klucz[key_counter%len(klucz)]))%len(alf)]
        key_counter+=1
    print(''.join(tekst))