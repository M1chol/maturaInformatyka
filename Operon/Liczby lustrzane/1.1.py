def lustro(liczba: int) -> str:
    return str(liczba)[::-1] if int(liczba)>9 else False

with open('liczby.txt') as dane:
    dane=[i.rstrip() for i in dane]
ile=0
for inx, baza in enumerate(dane):
    for sprw in range(inx+1, len(dane)):
        if str(baza) == lustro(dane[sprw]):
            ile += 1
print(ile)
