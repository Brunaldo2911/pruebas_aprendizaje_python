print("Bienvenidos a la Calculadora Basica disenada por Bruno Salas")
operacion = input("Que operacion quieres realizar? (Suma / Resta / Multiplicacion / Division ) :").upper
a = float(input("Escoge el primer numero: "))
b = float(input("Escoge el primer numero: "))
resultado = 0

if operacion == "Suma":
    resultado = a+b
elif operacion == "Resta":
    resultado = a-b
elif operacion == "Multipliacion":
    resultado = a*b
elif operacion == "Division":
    resultado = a/b
print("El resultado de tu operacion es {}".format(resultado))