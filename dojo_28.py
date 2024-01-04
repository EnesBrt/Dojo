# tower breaker

def towerBreakers(n, m):
    
    if m == 1:
        return 2
    elif m > 1 and n % 2 == 0:
        return 2
    elif m > 1 and n % 2 != 0:
        return 1

print(towerBreakers(1 , 4))