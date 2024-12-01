

PLIK_WEJSCIA = "./2024/zalaczniki/liczby_przyklad.txt"


with open(PLIK_WEJSCIA, "r") as f:
    LICZBY_RAW = f.readlines()
    LICZBY = []
    for linia in LICZBY_RAW:
        LICZBY.append([int(x) for x in linia.split(" ")])

counter = 0
for liczba_1 in LICZBY[0]:
    for liczba_2 in LICZBY[1]:
        if liczba_2 % liczba_1 == 0:
            counter += 1
            break

print(counter)