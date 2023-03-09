with open('dane8.txt') as dane:
    ciag=list(map(int,[i.rstrip() for i in dane]))
    len_path=[1]*len(ciag)
    for inx, element in enumerate(ciag):
        paths=[len_path[i] for i in range(inx) if ciag[i]<element]
        len_path[inx]=max(paths, default=0)+1
    print(max(len_path, default=0))