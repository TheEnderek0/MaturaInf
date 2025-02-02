def J(n):
    c = 0
    while n > 0:
        c += 1
        if n % 2 == 1:
            print(c)

        n = n // 2


if __name__ == "__main__":
    print(J(19))
    print(J(6))
    print(J(42))