# 1/n- Cycle


def cycle(n):
    if n % 2 == 0 or n % 5 == 0:
        return -1

    k, mod = 1, 10 % n
    while mod != 1:
        mod = (mod * 10) % n
        k += 1
    return k
