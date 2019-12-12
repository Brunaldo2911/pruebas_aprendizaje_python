mi_lista_de_compra = []
input_usuario = input("Que es lo quieres comprar (Escribe FIN para salir): ")

while input_usuario != "FIN":
    mi_lista_de_compra.append(input_usuario)
    input_usuario = input("Que es lo quieres comprar (Escribe FIN para salir : ")

largo_lista = len(mi_lista_de_compra)
indice_actual = 0

#while indice_actual < largo_lista:
 #   print("Tengo que comprar {}".format(mi_lista_de_compra[indice_actual]))
 #   indice_actual += 1

for item in mi_lista_de_compra:
    print("Tengo que comprar {}".format(item))
print("Esta es la lista de compra")