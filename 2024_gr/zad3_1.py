
from math import floor, sqrt

IN_FILE = "zal/liczby.txt"



with open(IN_FILE, "r") as file:
    LICZBY = [int(x) for x in file.readlines()]


lista_sprawdzen = list( map(lambda x: x*x, range(floor(sqrt(1000)), floor(sqrt(9999)) + 1))  )

l = 0
counter = 0
for liczba in LICZBY:
    if liczba in lista_sprawdzen:
        if not l:
            l = liczba

        counter += 1

print(counter)
print(l)