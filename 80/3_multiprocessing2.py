import multiprocessing

def czyTr(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)

def liczTr(dane, start, stop):
    ile = 0
    for i in range(start, stop):
        for j in range(i + 1, 500 - 1):
            for k in range(j + 1, 500):
                if czyTr(dane[i], dane[j], dane[k]):
                    ile += 1
    return ile

if __name__ == '__main__':
    with open('dane_trojkaty.txt') as dane:
        new_dane = [int(i.rstrip()) for i in dane]

    pool = multiprocessing.Pool(processes=10)
    results = [pool.apply_async(liczTr, (new_dane, i, i + (500 - 2) // 5)) for i in range(0, 500 - 2, (500 - 2) // 5)]
    ile = sum([result.get() for result in results])

    print(ile)