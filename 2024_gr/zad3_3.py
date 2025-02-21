

IN_FILE = "zal/liczby.txt"
with open(IN_FILE, "r") as file:
    LICZBY = [int(x) for x in file.readlines()]



c_wieksza = 0
c_rowna = 0
c_mniejsza = 0

rowne = []

for liczba in LICZBY:

    listliczba = [int(c) for c in str(liczba)]

    najw = sorted(listliczba, reverse=True)
    najm = sorted(listliczba)

    l_najw = 0
    l_najm = 0
    for ind in range(len(najw)):
        c_najw = najw[ind]
        c_najm = najm[ind]

        mult = len(najw) - (ind + 1)

        l_najw += c_najw * (10 ** mult)
        l_najm += c_najm * (10 ** mult)


    roznica = l_najw - l_najm
    #print(f"{liczba} | {l_najw} | {l_najm}")
    if roznica > liczba:
        c_wieksza += 1
    elif roznica == liczba:
        c_rowna += 1
        rowne.append(liczba)
    elif roznica < liczba:
        c_mniejsza += 1


print(f"Różnica większa od liczby: {c_wieksza}")
print(f"Różnica równa liczbie: {c_rowna}, te liczby to {rowne}")
print(f"Różnica mniejsza od liczby: {c_mniejsza}")