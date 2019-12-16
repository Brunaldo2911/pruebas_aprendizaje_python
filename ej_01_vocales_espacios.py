print("Bienvenidos al programa que cuenta el numero de espacios, comas y puntos")
frase_usuario = input("Introduce la frase que quieras: ")

puntos = ["."]
espacio = [" "]
comas = [","]

n_puntos = 0
n_espacios = 0
n_comas = 0

for letra in frase_usuario:
    if letra in puntos:
        n_puntos += 1
    elif letra in espacio:
        n_espacios += 1
    elif letra in comas:
        n_comas += 1

print("El numero de puntos es {}, el de comas es {} y el espacios es {}".format(n_puntos, n_comas, n_espacios))
