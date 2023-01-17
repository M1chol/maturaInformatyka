with open('tekst.txt') as dane:
    slowa=dane.readline().split()
    for i in slowa:
        if i[0]=='d' and i[-1]=='d':
            print(i)