
IN_FILE = "zal/prostokaty.txt"
with open(IN_FILE, "r") as file:
    PROSTOKATY = [x.split(" ") for x in file.readlines()]
    PROSTOKATY = [(int(x), int(y)) for x, y in PROSTOKATY]




# W TYM ZADANIU POMYLILEM SZEROKOSC Z DLUGOSCIA (ICH KOLEJNOSC)
# Niby nie ma to znaczenia bo to tylko nazwy zmniennych ale nadal

prev_szerokosc = -1
prev_dlugosc = -1
counter = 0

WYNIKI = {} # Traktowanie tego jak dict pozwoli nam na latwe znalezienie maksimum

for szerokosc, dlugosc in PROSTOKATY:

    if szerokosc <= prev_szerokosc and dlugosc <= prev_dlugosc: # Miesci sie
        counter += 1
        prev_szerokosc, prev_dlugosc = szerokosc, dlugosc
        continue
    else: # Nie miescimy sie
        try:
            WYNIKI[counter] # Testujemy czy mamy juz te wartosc
        except KeyError:
            WYNIKI[counter] = (prev_szerokosc, prev_dlugosc)

        prev_szerokosc, prev_dlugosc = szerokosc, dlugosc
        counter = 1  # Liczymy ten jako pierwszy

        if prev_szerokosc == prev_dlugosc == -1: # Rozpoczynamy, usun niepoprawna wartosc
            WYNIKI.pop(counter)


maksimum = max(WYNIKI.keys())

szr, dl = WYNIKI[maksimum]

print(f"Wynik to {maksimum} {szr} {dl}")