with open('dane_geny.txt') as dane:
    t=[len(i.rstrip()) for i in dane]
    c=t.count(max(t,key=t.count))
    print(len(set(t)),c)