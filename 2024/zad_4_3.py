PLIK_WEJSCIA = "./2024/zalaczniki/liczby_przyklad.txt"


with open(PLIK_WEJSCIA, "r") as f:
    LICZBY_RAW = f.readlines()
    LICZBY = []
    for linia in LICZBY_RAW:
        LICZBY.append([int(x) for x in linia.split(" ")])


def factorize(x: int):
    b = []
    for i in range(2, x + 1):
        while not x % i:
            b.append(i)
            x //= i
    
    return b

wyniki = []
for liczba in LICZBY[1]:
    factors = factorize(liczba)

    licz = LICZBY[0].copy()

    for f in factors.copy():
        if f in licz:
            licz.remove(f)
            factors.remove(f)
    

    if len(factors) == 0:
        wyniki.append(liczba)



print(wyniki)