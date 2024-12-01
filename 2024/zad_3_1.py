
def NieparzystySkrot(x: int):
    m = 0
    b = 1
    while x:
        a = x % 10 # Cyfra dziesiętna
        x //= 10 # Zmniejsz o cyfre dziesiętną

        if not a % 2 == 0 and a != 0:
            m += a * b
            b *= 10
        
    
    return m