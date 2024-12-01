from zad_3_1 import NieparzystySkrot

PLIK_WEJSCIA = "./2024/zalaczniki/skrot.txt"
PLIK_WYJSCIA = "./2024/wyniki/wyniki3_2.txt"

with open(PLIK_WEJSCIA, "r") as f:
    LICZBY = [int(x) for x in f.readlines()]


count = 0
liczby_bez = []

for i in LICZBY:
    if not NieparzystySkrot(i):
        liczby_bez.append(i)
        count += 1

najw = max(liczby_bez)

print(f"{count}\n{najw}")

with open(PLIK_WYJSCIA, "w+") as f:
    f.writelines(f"{count}\n{najw}")