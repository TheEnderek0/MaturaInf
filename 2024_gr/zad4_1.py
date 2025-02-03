


IN_FILE = "zal/prostokaty.txt"
with open(IN_FILE, "r") as file:
    PROSTOKATY = [x.split(" ") for x in file.readlines()]
    PROSTOKATY = [(int(x), int(y)) for x, y in PROSTOKATY]



POLA = [x * y for x, y in PROSTOKATY]

print(f"Najmniejsze pole: {min(POLA)}")
print(f"Najwieksze pole: {max(POLA)}")