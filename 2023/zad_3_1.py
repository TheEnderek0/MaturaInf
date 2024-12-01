
WEJSCIE = "./zal/pi_przyklad.txt"

with open(WEJSCIE, "r") as f:
    liczby = [int(x) for x in f.readlines()]


def fragment2(i: int) -> str:
    if i+1 > len(liczby):
        return ""

    return f"{liczby[i - 1]}{liczby[i]}"

i = 1
j = 0
while st := fragment2(i):
    if int(st) > 90:
        j += 1
    i += 1

print(j)