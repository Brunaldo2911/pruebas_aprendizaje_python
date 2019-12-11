import random

numero_intentos = 0
num_min = 1
num_max = 20

print("Hola! Cual es tu nombre?: ")
nombre_usuario = input()

numero_elegido = random.randint(num_min, num_max)
print("Bueno, " + nombre_usuario + '. Estoy pensando en un numero entre ' + str( num_min )  + ' and ' + str( num_max ))

while numero_intentos < 10:
    print("Intenta con un numero: " )
    intento = int(input())

    numero_intentos = numero_intentos + 1

    if intento < numero_elegido:
        print("Tu numero es muy bajo, intenta otra vez.")
    if intento > numero_elegido:
        print("tu numero es demasiado alto, intenta de nuevo.")
    if intento == numero_elegido:
        break

if intento == numero_elegido:
    print("Lo hiciste muy bien " + nombre_usuario + '!, adivinaste el numero en ' + str(numero_intentos) + ' intentos')
elif intento != numero_elegido:
    print("Lo siento" + nombre_usuario + ', no adivinaste esta vez, el numero que estaba pensando era ' + str(numero_elegido))



