from lib import LoadFile

IN_FILE = "./zal/liczby1.txt"
OUT_FILE = "./wyniki/zad1_suma.txt"

NUMBERS = LoadFile(IN_FILE)


to_write = [str(sum(x)) + "\n" for x in NUMBERS]


with open(OUT_FILE, "w") as f:
    f.writelines(to_write)
        

