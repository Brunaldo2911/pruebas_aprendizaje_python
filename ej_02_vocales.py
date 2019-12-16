# primer programa
frase = input("Introduce una frase que tu quieres y te contare el numero de vocales y consonantes que tienes tu frase : ")
vocales = ["a", "e", "i", "o", "u"]
n_vocales = 0
n_consonates = 0

for letra in frase:
    if letra in vocales:
        n_vocales += 1
    else:
        n_consonates += 1

print("El numero de vocales es {}".format(n_vocales))
print("El numero de consonantes es {}".format(n_consonates))