rowne=0
l1wieksze=0

with open('liczby1.txt') as dane1, open('liczby2.txt') as dane2:
    for (d1, d2) in zip(dane1,dane2):
        if int(d1.rstrip(),8)==int(d2):
            rowne+=1
        if int(d1.rstrip(),8)>int(d2):
            l1wieksze+=1
    print(f'rowne {rowne}\nwieksze {l1wieksze}')