def dl(list):
    x, y, x2, y2 = list
    return (x-x2)**2+(y-y2)**2

with open('wspolrzedneTR.txt') as dane:
    ile=0
    for line in dane:
        x1, y1, x2, y2, x3, y3 = map(int,line.split())
        a, b, c = sorted(map(dl,[[x1,y1,x2,y2],[x2,y2,x3,y3],[x3,y3,x1,y1]]))
        if a+b==c:
            ile+=1
    print(ile)
