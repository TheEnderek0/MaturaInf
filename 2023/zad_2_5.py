

WEJSCIE = "./zal/bin_przyklad.txt"
WYJSCIE = "./wyn/wyniki2_5.txt"

with open(WEJSCIE, "r") as f:
    liczby = [int(x, base=2) for x in f.readlines()]


operacja = lambda p: p ^ ( p // 2 )

liczby = map(operacja, liczby)

with open(WYJSCIE, "w") as f:
    f.writelines([f"{x:b}\n" for x in liczby])