with open('dane4.txt') as dane:
    t=[int(i.rstrip()) for i in dane]
    c=list(zip(t, t[1:]))
    b=[abs(i-j) for i, j in c]
    last=0
    ile=1
    ile_max=0
    max_inx=0
    for inx, i in enumerate(b):
        if inx==0:
            last=i
            continue
        if last == i:
            ile+=1
            if ile > ile_max:
                ile_max=ile
                max_inx=inx
        else: ile=1
        last=i
    print(ile_max+1, t[max_inx-ile], t[max_inx+1])
    print(max_inx+ile)
