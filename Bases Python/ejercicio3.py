def devolver_distintos(n1,n2,n3):
    list = [n1,n2,n3]
    total = n1 + n2 + n3
    
    if(total > 15):
        return max(list)
    elif(total < 10):
        return min(list)
    else:
        list.sort()
        return list[1]


print(devolver_distintos(1,5,2))