import string as st
alf=st.ascii_lowercase
klucz=(5,2)
with open('tekst.txt') as dane:
    slowa=dane.readline().split()
    for i in slowa:
        if len(i)<10:
            continue
        print(''.join([alf[(alf.index(j)*klucz[0]+klucz[1])%26] for j in i]))


