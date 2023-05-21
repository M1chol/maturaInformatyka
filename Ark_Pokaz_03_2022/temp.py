with open('szachy.txt') as dane:
    """
    ile=0
    for i in range(125):
        t=[dane.readline().rstrip() for _ in range(9)]
        biale=''
        czarne=''
        for i in t:
            for j in i:
                if j=='.': continue
                if j.isupper(): biale+=j
                else: czarne+=j
        if sorted(czarne.upper()) == sorted(biale): ile+=1
    print(ile)"""

    """    
    # t=[]
    # for i in range(9):
    #     t.append(dane.readline().rstrip())
    # print(t)
    ile_cz=0
    ile_b=0
    for _ in range(125):
        t=[dane.readline().rstrip() for _ in range(9)]
        kol=['' for i in range(8)]
        wiersze=[]
        for wiersz in t:
            for inx, znak in enumerate(wiersz):
                kol[inx]+=znak
            if wiersz!='': wiersze.append(wiersz)


        for wk in [wiersze, kol]:
            for w in wk:
                v=w.replace('.','')
                if 'wK' in v or 'Kw' in v:
                    ile_cz+=1
                if 'Wk' in v or 'kW' in v:
                    ile_b+=1
    print(ile_b, ile_cz)"""

A=['X',1,2,3,4,10,20,40,80,40]
for k in range(1,201):
    s=k
    B=[0 for i in range(s+1)]
    n=len(A)-1
    B[0]=1
    for j in range(n):
        k=j+1
        for i in range(s,A[k]-1,-1):
            if B[i-A[k]]==1 and B[i]==0:
                B[i]=1
    if B[-1]==1:
        print(B)
    else:
        print('niepowodzenie', k)
        break