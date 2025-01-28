#pass == continue
#break


a = [1,2,3]

for elemento in a:
    i = a.index(elemento)
    print(f'Indice {i}: {elemento}')


dic = {1: 'uno', 2: 'dosh'}

#for elemento in dic: #keys
#for elemento in dic.values():
#for elemento in dic.items():
for a,b in dic.items():
    print(f'Key: {a} Value: {b}')

bb = 5
while bb < 10:
    print(bb)
    bb = bb + 1
else:
    print('fin')

#rangos
#for a in range(10):
#for a in range(2, 10):
for a in range(1, 20, 3):
    print(a)


#Enumeradores
ff = [1,2,3]

for ind, val in enumerate(ff):
    print(f'Indice: {ind} Valor: {val}')


