print("Bienvenidos a la Calculadora Basica disenada por Bruno Salas")
operacion = input("Que operacion quieres realizar? (SUMA / RESTA / MULTIPLICACION / DIVISION ) :")
a = float(input("Escoge el primer numero: "))
b = float(input("Escoge el segundo numero: "))
if operacion == "SUMA":
    print("el resultado es: ", a + b)
elif operacion == "RESTA":
    print("el resultado es: ", a - b)
elif operacion == "MULTIPLICACION":
    print("el resultado es: ", a * b)
elif operacion == "DIVISION":
    print("el resultado es: ", a / b)