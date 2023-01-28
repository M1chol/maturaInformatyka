from string import ascii_uppercase
with open('szyfr.txt') as dane:
    slowo, klucz = dane.readline().rstrip(), dane.readline().rstrip()
    slownik={i: slowo.count(i) for i in ascii_uppercase}
    d=0.0285/(sum([slownik[i]*(slownik[i]-1) for i in ascii_uppercase])/(sum(slownik.values())*(sum(slownik.values())-1)) - 0.0385)
    print(f'Dlugosc klucza: {len(klucz)}, oszacowana dlugosc: {round(d,2)}')