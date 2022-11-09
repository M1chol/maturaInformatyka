with open('liczby1.txt') as dane:
    dane2=[i for i in dane]
    print(max(dane2),min(dane2))