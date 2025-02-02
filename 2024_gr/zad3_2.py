
from math import ceil, sqrt

IN_FILE = "zal/liczby.txt"
with open(IN_FILE, "r") as file:
    LICZBY = [int(x) for x in file.readlines()]


PRIMES = {2, 3, 5, 7, 11, 13} # Troche liczb pierwszych, reszta zostanie wygenerowana dynamicznie

def prime_range(start, stop): # Oblicza następną liczbę pierwszą

    n = start - 1
    list = []
    while n < stop:
        n += 1
        if n in PRIMES:
            list.append(n)

        if all( n % x != 0 for x in PRIMES): # Jezeli nie dzieli sie przez zadna z liczb pierwszych to nie dzieli sie przez nic
            PRIMES.add(n) # Dodaj n do zbioru
            list.append(n)

    return list


for liczba in LICZBY:
    c = 0
    for lp in prime_range(2, ceil(sqrt(liczba))): # Pobierz wszystkie możliwe dzielniki (rozkładu na liczby pierwsze)
        if liczba % lp == 0:
            c += 1 #znalezlismy dzielnik

        if c >= 5:
            print(liczba)
            break