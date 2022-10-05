from multiprocessing import Pool

with open('liczby.txt') as data:
    liczby=[int(i) for i in data]
def czynniki(liczba):
    if liczba%2==0:
        return False
    dziel=[]
    i=3
    while i*i<=liczba:
        if liczba%i:
            i+=1
        else:
            liczba//= i
            dziel.append(i)
    if liczba>1: dziel.append(liczba)
    dziel=list(dict.fromkeys(dziel))
    if len(dziel)==3: return True
    return False

if __name__ == '__main__':
    with Pool() as pool:
        t=pool.map(czynniki, liczby)
    print(sum(t))
