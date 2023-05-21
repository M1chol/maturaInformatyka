with open('dane4.txt') as dane:
    t=[int(i.rstrip()) for i in dane]
    c=list(zip(t, t[1:]))
    b=[abs(i-j) for i, j in c]
    d=[[i, b.count(i)] for i in set(b)]
    d=sorted(d, key=lambda x: x[1], reverse=True)
    print(d[:2])