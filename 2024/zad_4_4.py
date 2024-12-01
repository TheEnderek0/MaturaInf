PLIK_WEJSCIA = "./2024/zalaczniki/liczby.txt"


with open(PLIK_WEJSCIA, "r") as f:
    LICZBY_RAW = f.readlines()
    LICZBY = []
    for linia in LICZBY_RAW:
        LICZBY.append([int(x) for x in linia.split(" ")])


def arithmetic_mean(numba:int):
    return sum(numba) / len(numba)


LICZ = LICZBY[0]
srednie =   []
start =     []
dlugosc =   []


for i in range(dl := len(LICZ)):
    if (dl - 1) - i < 50: # Koniec
        break

    for j in range(i + 50, dl):
    
        compare = LICZ[i:j]

        srednie.append(arithmetic_mean(compare))
        start.append(LICZ[i])
        dlugosc.append(j - i)

m = max(srednie)
ind = srednie.index(m)
print(m, dlugosc[ind], start[ind])

with open("./test.txt", "w") as f:
    f.writelines([str(x) + "\n" for x in srednie])