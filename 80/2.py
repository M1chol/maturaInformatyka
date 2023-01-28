def czyTr(a, b, c):
    return True if b+c>a else False
with open('dane_trojkaty.txt') as dane:
    new_dane=[int(i.rstrip()) for i in dane]
    new_dane=sorted(new_dane,reverse=True)
    for i in range(len(new_dane)-2):
        if czyTr(new_dane[i], new_dane[i+1], new_dane[i+2]):
            print(sum([new_dane[i], new_dane[i+1], new_dane[i+2]]))
            break

