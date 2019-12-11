
pokemon_elegido = input("Contra que pokemon quieres luchar? (Pearson / Choclet / Swing ) : ")

vida_pikachu = 100
vida_enemigo = 0
ataque_pokemon = 0


if pokemon_elegido == "Pearson":
    vida_enemigo = 90
    nombre_pokemon = "Pearson"
    ataque_pokemon = 10

elif pokemon_elegido == "Choclet":
    vida_enemigo = 80
    nombre_pokemon = "Choclet"
    ataque_pokemon = 12

elif pokemon_elegido == "Swing":
    vida_enemigo = 100
    nombre_pokemon = "Swing"
    ataque_pokemon = 14

while vida_pikachu > 0 and vida_enemigo > 0:
    ataque_elegido = input("Que ataque vamos a usar? (Chispazo, Bola Voltio)")

    if ataque_elegido == "Chispazo":
        vida_enemigo -= 10
    elif ataque_elegido == "Bola Voltio":
        vida_enemigo -= 12

    print("La vida del {} es de {}".format(nombre_pokemon, vida_enemigo))

    print("{} te hace un dano de {}".format(pokemon_elegido, ataque_pokemon))
    vida_pikachu -= ataque_pokemon
    print("La vida de Pikachu ahora es de {}".format(vida_pikachu))

if vida_pikachu <= 0:
    print( "He caido con los choclets")

elif vida_enemigo <= 0:
    print( "Perdi papu")


    print("codigo combate")


