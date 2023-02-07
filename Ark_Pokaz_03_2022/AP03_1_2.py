with open('szachy.txt') as dane:
    ile=0
    ile_pion=99
    for i in range(125):
        l_upper=''
        l_lower=''
        for j in range(9):
            if j==8:
                dane.readline()
                continue
            for pion in list(dane.readline().rstrip()):
                if pion=='.':
                    continue
                if pion.isupper():
                    l_upper+=pion
                else:
                    l_lower+=pion
        if sorted(l_lower.upper())==sorted(l_upper):
            ile+=1
            ile_pion=min(ile_pion, len(l_lower)*2)
    print(ile, ile_pion)