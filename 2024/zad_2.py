
def algorytm(n: int):
    b = 1
    c = 0
    counter = 0
    while n > 0:
        a = n % 10
        n //= 10
        if a % 2 == 0:
            c += b * (a // 2)
        else:
            c += b
            counter += 1
        b *= 10
    
    return c, counter


while True:
    x = int(input())
    print(algorytm(x))