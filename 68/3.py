with open('dane_napisy.txt') as dane:
    tab=[''.join(sorted(i)) for j in dane for i in j.rstrip().split(' ')]
    print(tab.count(max(tab,key=tab.count)))