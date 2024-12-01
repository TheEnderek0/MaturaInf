PLIK_WEJSCIA = "./2024/zalaczniki/liczby_przyklad.txt"


with open(PLIK_WEJSCIA, "r") as f:
    LICZBY_RAW = f.readlines()
    LICZBY = []
    for linia in LICZBY_RAW:
        LICZBY.append([int(x) for x in linia.split(" ")])


l = LICZBY[0]
l = sorted(l, reverse=True)
print(l[100])