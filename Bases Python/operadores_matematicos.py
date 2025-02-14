print(1 / 2)

#division sin decimales
print(1 // 2)

#exp
print(2**3)

#round
print(round(90/7))
print(round(90/7, 3))


#index
a = 'Hola me llamo David'
print(a[0])
print(a[-1])
print(a.index('l'))
print(a.index('la'))
#print(a.index('xxxxxxx')) #error when no subs is found
print(a.find('xxxxx'))#-1
print(a.index('a'))
print(a.index('a', 4)) #index start from
print(a.rindex('a'))

#substrings
print(a[0:4])
print(a[0:])#hasta al final
print(a[0:10:2])#Desde la pos 0 cada 2 pos
print(a[::2])#Desde la pos 0 cada 2 pos
print(a[::-2])#Desde el final cada 2 pos

#metodos
print(a.upper())
print(a.lower())
print(a.split())
print(a.split('a'))

print(' '.join(['Hola', 'David']))

print(a.replace('David', 'Dosh'))

#strings son inmutables
var1 = 'Hola'
#var1[0] = 'a' #Error

print(var1 * 5)

multilinea = """ASDF
 GHJGHJ"""

print(multilinea)

print('David' in multilinea) #false
print('David' not in multilinea) #true

#length
print(len('David'))



