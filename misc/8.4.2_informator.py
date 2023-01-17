def glebokosc(tab):
    ile=0
    ile_max=0
    for i in str(tab):
        if i == '[': ile+=1
        elif i == ']': ile-=1
        if ile>ile_max:ile_max=ile
    return ile_max-1

def step(ciag):
    kolejne=[ciag[i:] for i in range(len(ciag))]
    kolejne_rosnace=[]
    for i in kolejne:
        licz=i[0]
        kolejne_rosnace.append([j for j in i if j>licz])
    if not kolejne_rosnace: return []
    return [step(i) for i in kolejne_rosnace]

with open('dane8.txt') as dane:
    ciag=[int(i.rstrip()) for i in dane]
print(glebokosc(step(ciag)))

