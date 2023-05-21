with open('jezyki.txt') as jezyki:
    jezyki.readline()
    t=[i.rstrip().split('\t')[1] for i in jezyki]
    s=list(set(t))
    v=[]
    for i in s:
       v.append([i, t.count(i)])
    v.sort(key=lambda x: x[1], reverse=True)
    print(v)
