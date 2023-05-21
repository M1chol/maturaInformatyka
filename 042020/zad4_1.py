with open('dane4.txt') as dane:
    t=[int(i.rstrip()) for i in dane]
    c=list(zip(t, t[1:]))
    b=[abs(i-j) for i, j in c]
    print(max(b), min(b))