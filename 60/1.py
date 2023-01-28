with open('liczby.txt') as plik:
    new=[i for i in plik if int(i)<1000]
    print(len(new),new[-1],new[-2])