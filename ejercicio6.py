def contar_primos(n):
    total = [2]
    ind = 3

    if n < 2:
        return 0

    while ind <= n:
        for e in range(3, ind, 2):
            if ind & e == 0:
                ind = ind + 2
                break
        else:
            total.append(ind)
            ind = ind + 2

    print(total)
    return len(total)

contar_primos(50)