# segundo programa: Capaz de contar la cantidad de mayusculas en una string introducida por el usuario
frase = input("Introduce una frase que tu quieres y te contare el numero de Mayusculas que tiene tu frase : ")
mayusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
n_mayusculas = 0
n_minusculas = 0

for letra in frase:
    if letra in mayusculas:
        n_mayusculas += 1
    else:
        n_minusculas += 1

print("El numero de mayusculas es {}".format(n_mayusculas))
print("El numero de minusculas es {}".format(n_minusculas))