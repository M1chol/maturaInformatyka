from math import sqrt
def dl(list):
    x, y, x2, y2 = list
    return sqrt((x-x2)**2+(y-y2)**2)
with open('wspolrzedneTR.txt') as dane:
    maxdl=0
    for line in dane:
        x1, y1, x2, y2, x3, y3 = map(int,line.split())
        dlugosci=map(dl,[[x1,y1,x2,y2],[x2,y2,x3,y3],[x3,y3,x1,y1]])
        temp=round(sum(dlugosci),2)
        if maxdl<temp:
            maxdl=temp
            maxpkt=[x1,y1,x2,y2,x3,y3]


    print(f'A:{maxpkt[0],maxpkt[1]}, B{maxpkt[2],maxpkt[3]}, C{maxpkt[4],maxpkt[5]}; obw: {maxdl}')