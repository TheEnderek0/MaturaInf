

IN_FILE = "zal/prostokaty.txt"
with open(IN_FILE, "r") as file:
    PROSTOKATY = [x.split(" ") for x in file.readlines()]
    PROSTOKATY = [(int(x), int(y)) for x, y in PROSTOKATY]



# Slownik w ktorym kluczami sa wysokosci a wartosciami listy szerokosci danych prostokatow
szer_od_wys: dict[list] = {}

# Grupujemy prostokaty z ta sama wysokoscia
for wys, szer in PROSTOKATY:

    try:
        szer_od_wys[wys]
    except KeyError:
        szer_od_wys[wys] = [] # nowy klucz
    finally:
        szer_od_wys[wys].append(szer)


def maks_sklejenia(n):

    d = []

    for wys in szer_od_wys.keys():
        szerokosci = szer_od_wys[wys]
        szerokosci = sorted(szerokosci, reverse=True) # Od najwiekszej do najmniejszej
        # Suma n pierwszych da nam najwieksza mozliwa

        szerokosci = szerokosci[:n] # Tniemy do n (wlacznie)

        d.append(sum(szerokosci))


    return max(d)


print(f"2 prostokaty: {maks_sklejenia(2)}")
print(f"3 prostokaty: {maks_sklejenia(3)}")
print(f"5 prostokatow: {maks_sklejenia(5)}")