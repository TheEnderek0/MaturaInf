
from math import floor, sqrt, pow

IN_FILE = "zal/liczby.txt"



with open(IN_FILE, "r") as file:
    LICZBY = [int(x) for x in file.readlines()]


#lista_sprawdzen = list( map(lambda x: x*x, range(floor(sqrt(1000)), floor(sqrt(9999)) + 1))  )

# Liczby są [1000, 9999]

lista_sprawdzen = []
a = floor(sqrt(1000)) # 31
b = floor(sqrt(9999)) + 1 # 100

przedzial = list(range(a, b))

for x in przedzial:
    lista_sprawdzen.append(x ** 2)

l = 0
counter = 0
for liczba in LICZBY:
    if liczba in lista_sprawdzen:
        if not l:
            l = liczba

        counter += 1

print(counter)
print(l)