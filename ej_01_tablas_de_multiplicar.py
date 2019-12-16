# ejercicio que permite obtener las tablas de multiplicar de un numero que el usuario indique
# Uso de la funcion range()

print("Bienvenidos a la tabla de multiplicar")
n_usuario = int(input("Ingresa el numero  que quieras y te dare una tabla de multiplicar del 0 al 12 : "))
rango = range(12)

for multiplo in rango:
    print("{} * {} = {}".format(n_usuario, multiplo, n_usuario*multiplo))

