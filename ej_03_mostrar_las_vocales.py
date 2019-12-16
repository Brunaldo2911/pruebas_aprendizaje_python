# tercer programa
frase = input("Introduce una frase que tu quieres y te mostrare las vocales que tiene tu frase : ")
vocales = ["a", "e", "i", "o", "u"]

for letra in frase:
    if letra in vocales:
        print("Las vocales que tiene la palabra son: {}".format(letra))

