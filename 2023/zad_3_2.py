
WEJSCIE = "./zal/pi_przyklad.txt"

with open(WEJSCIE, "r") as f:
    liczby = [int(x) for x in f.readlines()]


def fragment2(i: int) -> str:
    if i+1 > len(liczby):
        return ""

    return f"{liczby[i - 1]}{liczby[i]}"




fragment_dic = {}
def conv(c):
    if len(str(c)) < 2:
        return f"0{c}"
    else:
        return str(c)

fragmenty = map(conv, range(0, 100))

for f in fragmenty:
    fragment_dic[f] = 0


fragmenty_p = [fragment2(i) for i in range(len(liczby) - 1)]

for f in fragmenty_p:
    fragment_dic[f] += 1

sorted()

