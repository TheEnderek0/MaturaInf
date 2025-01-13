import dblib as db


mytable = db.Structure(imie=None, nazwisko="-", adres="-")

mytable.add_row(db.Row(imie="Jan",          nazwisko="Kowalski"))
mytable.add_row(db.Row(imie="Agnieszka",    nazwisko="Nowak", adres="Warszawa, ul. Aleje Jerozolimskie 1/2", dodatkowe=90))
mytable.add_row(db.Row(nazwisko="Blad"))

mytable.delete_row(1)
mytable.add_row(db.Row(ID = 1, imie="Anna", nazwisko="Wielka"))
mytable.add_row(db.Row(ID = 10, imie="Anna", nazwisko="August"))
print("Created table:")
print(mytable)

mytable.sort_rows()
#print(mytable)

mytable2 = db.Structure()

with open("./test.db", "wb") as file:
    file.write(mytable.serialize())

with open("./test.db", "rb") as file:
    mytable2.deserialize(file)

print("Loaded table from file:")
print(mytable2)