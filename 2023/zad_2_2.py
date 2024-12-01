from zad_2_1 import Bloki
from os import getcwd
PLIK_WEJSCIA = "zal/bin_przyklad.txt"

with open(PLIK_WEJSCIA, "r") as f:
    liczby = [int(x, base=2) for x in f.readlines()]

c = 0
for liczba in liczby:
    if (bl := Bloki(liczba)) <= 2:
        c += 1

print(c)