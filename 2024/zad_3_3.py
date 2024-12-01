from zad_3_1 import NieparzystySkrot
from math import gcd

PLIK_WEJSCIA = "./2024/zalaczniki/skrot2.txt"
PLIK_WYJSCIA = "./2024/wyniki/wyniki3_3.txt"

with open(PLIK_WEJSCIA, "r") as f:
    LICZBY = [int(x) for x in f.readlines()]


wyniki = []

for liczba in LICZBY:
    nskrot = NieparzystySkrot(liczba)

    nwd = gcd(nskrot, liczba)
    if nwd == 7:
        wyniki.append(liczba)

print(wyniki)

with open(PLIK_WYJSCIA, "w+") as f:
    f.writelines([str(x) + "\n" for x in wyniki])