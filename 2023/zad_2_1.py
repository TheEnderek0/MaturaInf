def Bloki(x: int):

    ilosc = 0
    r = -1
    while x > 0:
        r_new = x % 2
        x //= 2

        if r != r_new:
            r = r_new
            ilosc = ilosc + 1

    return ilosc


if __name__ == "__main__":
    print(Bloki(245))