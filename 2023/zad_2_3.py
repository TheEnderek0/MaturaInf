
WEJSCIE = "./zal/bin_przyklad.txt"

with open(WEJSCIE, "r") as f:
    liczby = [int(x, base=2) for x in f.readlines()]

print(f"{max(liczby):b}")