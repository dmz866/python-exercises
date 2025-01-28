s = set([1,2,3])
s2 = set((1,2,3))
s3 = {1,2,3}

#Inmutables no soporta listas pero si tuplas ni valores repetidos
#s3[0] = 44 #Error
#Error s4 = {1,2,3 [1,2]}
s5 = {1,2,3, (4,5)}

s6 = {1,2,2,3}
s7 = {3,4,5,6}

s6.add(10)
s6.remove(10) #error si no existe el valor
s6.discard(10)
s6.pop() # elimina cualquier valor aleatoriamente
s6.clear()
print(s6.union(s7))



