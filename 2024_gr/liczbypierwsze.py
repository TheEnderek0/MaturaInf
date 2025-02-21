from math import floor, sqrt


LICZBY_PIERWSZE = []

for i in range(1000, 10000):
    znaleziono = False
    for x in range(2, floor(sqrt(i))):
        if i % x == 0:
            znaleziono = True
            break

    if not znaleziono:
        LICZBY_PIERWSZE.append(i)


print(LICZBY_PIERWSZE)