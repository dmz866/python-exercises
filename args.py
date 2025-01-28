#def suma(*args):
def suma(*nums):
    total = 0

    for el in nums:
        total = total + el

    return total

print(suma(1,2,3,4))

