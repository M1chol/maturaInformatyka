def wyszukaj_wzorzec(lancuch: str, wzorzec: str) -> int:
    """
    Algorytm wyszukiwania wzorca w tekście
    :param lancuch: tekst do przeszukania
    :param wzorzec: szukany podciąg
    :return: index pierwszego wystąpienia wzorca
    """
    len_lancuch = len(lancuch)
    len_wzorzec = len(wzorzec)
    for inx in range(0, len_lancuch-len_wzorzec+1):
        if lancuch[inx:inx+len_wzorzec]==wzorzec: return inx

print(wyszukaj_wzorzec('alamakota', 'kot'))

def bubble_sort(lista: list[int]) -> list[int]:
    """
    Algorytm sortowania bąbelkowego
    :param lista: lista do sortowania
    :return: posortowana lista
    """
    for _ in range(len(lista)-1):
        for i in range(len(lista)-1):
            if lista[i]>lista[i+1]: lista[i], lista[i+1] = lista[i+1], lista[i]
    return lista

print(bubble_sort([6,2,7,9,2,76,3,10,5,1]))

def insertion_sort(lista: list) -> list:
    """
    Algorytm sortowania listy przez przestawienie
    :param lista: lista do sortwania
    :return: posortowana lista
    """
    for i in range(1, len(lista)):
        temp=lista[i]
        j=i-1
        while j>=0 and temp<lista[j]:
            lista[j+1]=lista[j]
            j-=1
        lista[j+1]=temp
    return lista

print(insertion_sort([6,2,7,9,2,76,3,10,5,1]))

def szyfr_cezar(slowo: str, klucz: int) -> str:
    """
    Algorytm szyfru cezara
    :param slowo: slowo do zaszyfrowania
    :param klucz: klucz szyfrowania
    :return: zaszyfrowany tekst
    """
    uppercase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    translated=''
    for inx in range(len(slowo)):
        if slowo[inx]==' ':
            translated+=' '
            continue
        znak = slowo[inx].upper()
        translated+=uppercase[(uppercase.index(znak)+klucz)%26]
    return translated

print(szyfr_cezar('NRCLRO', -3))

def szyfr_przestaw(slowo: str) -> str:
    """
    Algorytm szyfru przestawieniowego
    :param slowo: slowo do zaszyfrowania
    :return: zaszyfrowane slowo
    """
    translated=''
    for i in range(1, len(slowo), 2):
        translated+=slowo[i]
        translated+=slowo[i-1]
    if len(slowo)%2==1: translated+=slowo[-1]
    return translated

print(szyfr_przestaw('LA AAMK TOA'))

def euklides_nwd(l1: int, l2: int) -> int:
    """
    Znajdywanie NWD algorytmem Euklidesa
    :param l1: liczba 1
    :param l2: liczba 2
    :return: NWD
    """
    while l1!=l2:
        if l1>l2:
            l1-=l2
        else:
            l2-=l1
    return l1

print(euklides_nwd(12, 18))

def nww(l1: int, l2: int) -> int:
    """
    Algorytm znajdywania NWW przy pomocy NWD
    :param l1: liczba 1
    :param l2: liczba 2
    :return: NWW
    """
    return int(l1*l2/euklides_nwd(l1,l2))

print(nww(6, 15))

def eratostenes(klucz: int) -> list:
    """
    Algorytm zwraca wszystkie liczby pierwsze z przedziału 2-n
    :param klucz: górna wartość przedziału
    :return: liczby pierwsze
    """
    lista=[True for _ in range(klucz+1)]
    p=2
    while p*p<=klucz:
        if not lista[p]: continue
        for i in range(p*p, klucz+1, p):
            lista[i]=False
        p+=1
    return [i for i in range(2, klucz) if lista[i]]

print(eratostenes(15))

def reszta(suma: int, nominaly: list) -> list:
    """
    Algorytm wydawania reszty
    :param suma: suma (W GROSZACH!)
    :param nominaly: lista możliwych nominałów (W GROSZACH!)
    :return:
    """
    reszty=[]
    for nom in nominaly:
        ilosc, suma = suma//nom, suma%nom
        reszty.append(ilosc)
    return reszty

print(reszta(12_25, [10_00, 5_00, 2_00, 1_00, 50, 20, 10, 5, 2, 1]))

def lider(zbior: list) -> int:
    """
    Algorytm szukania lidera w zbiorze (najwięcej wystąpień >połowa)
    :param zbior: zbior
    :return: lider
    """
    ctr=0
    while ctr<len(zbior)-1:
        if zbior[ctr]!=zbior[ctr+1]:
            zbior.pop(ctr)
            zbior.pop(ctr)
        else: ctr+=1
    l=zbior[0]
    for i in zbior:
        if i!=l: return False
    return l

print(lider([1, 3, 2,3, 3, 3, 2, 1, 3, 3, 3]))

def podciag_niemal(zbior: list[int]) -> list[int]:
    """
    Algorytm szukania najdłuższego podciągu niemalejącego
    :param zbior: zbior
    :return: najdluższy podciag niemalejacy
    """
    maks=0
    maks_ciag=[]
    for inx, val in enumerate(zbior):
        temp=val
        for i in range(inx+1, len(zbior)):
            if zbior[i]<temp: break
            temp=zbior[i]
            if i+1-inx>maks:
                maks=i+1-inx
                maks_ciag=zbior[inx:i+1]
    return maks, maks_ciag

print(podciag_niemal([6,7,2,3,6,8,2,6,5,3,1]))

def podciag_max_suma(zbior: list[int]) -> list[int]:
    """
    Algorytm szukania maksymalnej sumy w podciągu
    :param zbior: zbior
    :return: podciąg o największej sumie elementów
    """
    maks=0
    maks_ciag=[]
    for inx, val in enumerate(zbior):
        for i in range(inx+1, len(zbior)):
            suma=sum(zbior[inx:i+1])
            if suma>maks:
                maks=suma
                maks_ciag=zbior[inx:i+1]
    return maks, maks_ciag

print(podciag_max_suma([-2,-4,4,-1,-2,1,5,-3]))

def zmiana_systemu(liczba: str, system_org: int, system_doc: int) -> str:
    """
    Algorytm zamiany systemów liczbowych
    :param liczba: liczba orginalna do zamiany
    :param system_org: system liczby orginalnej
    :param system_doc: system docelowy
    :return: liczba przeliczona
    """
    hex='0123456789abcdefABCDEF'
    def dec_to(liczba: int, system: int) -> str:
        if liczba < system:
            return hex[liczba%system]
        else:
            return dec_to(liczba // system, system) + hex[liczba%system]
    def to_dec(liczba: str, system: int) -> int:
        return int(liczba, system)
    if system_doc == system_org: return liczba
    dec=to_dec(liczba, system_org)
    return dec_to(dec, system_doc)

print(zmiana_systemu('F12', 16, 8))

def potega(liczba: int, pot: int) -> int:
    """
    funkcja podnoszenia do potęgi o złożoności log(n)
    :param liczba: liczba
    :param pot: potęga
    :return: wynik
    """
    w=1
    while pot>0:
        if pot%2==1:
            w*=liczba
        liczba*=liczba
        pot//=2
    return w
