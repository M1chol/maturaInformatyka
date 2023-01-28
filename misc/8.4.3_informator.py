ciag=[2, 4, 10, 6, 8, 1, 3, 7, 9, 5]
# with open('dane8.txt') as dane:
#     ciag=[int(i.rstrip()) for i in dane]
kolejne=[ciag[i:] for i in range(len(ciag))]
temp=[]
for i in kolejne:
    licz=i[0]
    temp.append((i[0],[j for j in i if j>licz],))
graf=dict(temp)

def dephFirst(graf, start):
    max_len = 0
    stack=[start]
    while len(stack)>0:
        current=stack.pop()
        for neighbour in graf[current]:
            stack.insert(0,neighbour)
    return max_len

print(dephFirst(graf, 2))