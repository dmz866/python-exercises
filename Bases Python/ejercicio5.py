def repetidos(*args):
    total = 0
    found = False

    for e in args:
        if(e == 0):
            found = True
            total = total + 1

            if(total == 2):
                return True
        else:
            found = False

    return False

print(repetidos(1,2,3,4,0,65,54,4))