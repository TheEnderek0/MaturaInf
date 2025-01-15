welcome_msg = """
Witamy! Wpisz 'help' aby uzyskać pomoc."""


help_msg = """
Dostępne komendy:
help - wyswietl tą wiadomość
nowa_tabela <nazwa> kolumna1=None, nazwisko=brak, ... - stwórz nową tabele
zaladuj <sciezka> <nazwa> - załaduj tabelę z pliku i daj jej tą nazwę (bez rozszerzenia)
wejdz <nazwa> - wejdź do tabeli o tej nazwie

W tabeli:
usun <id> - usun wiersz o tym id
nowy kolumna1=cos nazwisko=Kowalski ... - utwórz nowy wiersz i wpisz go do tabeli
edytuj <id> <kolumna> <wartość> - edytuj wiersz <id> w kolumnie <kolumna> wpisz wartość <wartość>
zapisz <sciezka> - zapisz tą tabelę w pliku (bez rozszerzenia)
""" 


DEFAULT_SELECTOR = ">>>"


selector = DEFAULT_SELECTOR
def main():
    print(welcome_msg)
    while True:
        ProcessCmd(input(selector  + " "))


def ProcessCmd(cmd: str):
    args = cmd.split(" ")
    for i in range(len(args)):
        if not args[i]: # Purge empty args
            del args[i]
            i -= 1
    
    cmd = args[0]
    args = args[1:]

    match cmd:
        case 'help':
            print(help_msg)
            return
        
        case 'nowa_tabela':
            nowa_tabela(args)
            return
        
        case _:
            print("Niezrozumiana komenda!")
            return


def nowa_tabela(args: list[str]):
    pass

if __name__ == "__main__":
    main()