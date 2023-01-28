with open('liczby2.txt') as dane:
    temp=[i.rstrip() for i in dane]
    ile=0
    for i in temp:
        for j in i:
            if j == '6':
                ile+=1
    print(f's10 {ile}')

    ile=0
    temp2=[oct(int(i)) for i in temp]
    for i in temp2:
        ile+=str(i).count('6')
    print(f's6 {ile}')
