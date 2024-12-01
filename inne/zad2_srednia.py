from lib import LoadFile
IN_FILE = "./zal/liczby2.txt"
OUT_FILE = "./wyniki/zad2_srednia.txt"


nums = LoadFile(IN_FILE)

Srednia = lambda x: sum(x) / len(x)

to_write = [str(Srednia(x)) + "\n" for x in nums]

with open(OUT_FILE, "w") as f:
    f.writelines(to_write)