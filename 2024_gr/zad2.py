counter = 0
def F(x, p):
    global counter
    counter += 1
    if x == 0:
        return 0
    else:
        c = x % p
        if c % 2 == 1:
            return F(x // p, p) + c
        else:
            return F(x // p, p) - c


print(F(220, 4))
print(f"Counter:{counter}")

#lmao = 99
#while F(lmao, 4):
#    lmao -= 1

xnajw = 99

while F(xnajw, 3):
    xnajw -= 1


print(xnajw)