class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)

        self.numero_cuenta = numero_cuenta
        self.balance = balance

print('Cuenta Bancaria')
print('1 Depositar')
print('2 Retirar')
print('3 Salir')

opciones = [1,2,3]
seleccion = int(input('Seleccione una opcion:'))

while seleccion not in opciones:
    seleccion = int(input('Seleccione una opcion:'))

while seleccion != 3:
    if seleccion == 1:
        valor = int(input('Cuanto quiere depositar?'))


