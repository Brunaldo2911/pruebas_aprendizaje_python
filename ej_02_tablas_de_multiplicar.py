# ejercicio que permite obtener las tablas de multiplicar solo por multiplos de 2
# Uso de la funcion

print("Bienvenidos a la tabla de multiplicar")
n_usuario = int(input("Ingresa el numero  que quieras y te dare una tabla de multiplicar del 0 al 12 : "))
rango = range(0,13,2)

for multiplo in rango:
    print("{} * {} = {}".format(n_usuario, multiplo, n_usuario*multiplo))