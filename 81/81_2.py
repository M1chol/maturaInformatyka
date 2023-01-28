with open('wspolrzedne.txt') as dane:
    ile=0
    for line in dane:
        x1, y1, x2, y2, x3, y3 = map(int,line.split())
        if x2!=x1:
            y=-(y2-y1)
            x=x2-x1
            c=-(x*y1+y*x1)
        else:
            if x3==x2:
                ile+=1
                continue
        if y*x3+x*y3+c==0:
            ile+=1
    print(ile)