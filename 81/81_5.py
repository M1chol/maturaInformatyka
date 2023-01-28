with open('wspolrzedneTR.txt') as dane:
    ile=0
    for line in dane:
        x1, y1, x2, y2, x3, y3 = map(int,line.split())
        xs, ys = (x1+x3)/2, (y1+y3)/2
        dx, dy = 2*(xs-x2)+x2, 2*(ys-y2)+y2
        if dx/dy==1:
            print(f'A{x1,y1}, B{x2, y2}, C{x3, y3}, D{dx, dy}')
