def add_if_dot(kol):
    t=[0 for i in range(8)]
    for inx, pole in enumerate(kol):
        if pole=='.':
            t[inx]+=1
    return t

with open('szachy.txt') as dane:
    ile=0
    ile_kol=0
    for i in range(125):
        t=[0 for _ in range(8)]
        for j in range(9):
            if j==8:
                dane.readline()
                continue
            t=[sum(i) for i in zip(add_if_dot(list(dane.readline().rstrip())), t)]
        if max(t)==8:
            ile+=1
            ile_kol=max(ile_kol, t.count(8))
    print(ile, ile_kol)