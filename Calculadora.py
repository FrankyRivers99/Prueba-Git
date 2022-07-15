

print("Calculadora GitHub")

print("1.- Suma \n2.-Resta \n3.-Multiplicación \n4.-Division \n5.-Modulo")

Opcion = input("Ingrese el numero de la operación que desea realizar: ")

valor_1 = input("Ingrese el primer valor: ")
valor_2 = input("Ingrese el segundo valor: ")


def Suma(valor1, valor2):
    resultado = int(valor1) + int(valor2)
    return print("El resultado es: " + str(resultado))

def Resta(valor1, valor2):
    resultado = int(valor1) - int(valor2)
    return print("El resultado es: " + str(resultado))

def Multiplicacion(valor1, valor2):
    resultado = int(valor1) * int(valor2)
    return print("El resultado es: " + str(resultado))

def Division(valor1, valor2):
    resultado = int(valor1) / int(valor2)
    return print("El resultado es: " + str(resultado))

def Residuo(valor1, valor2):
    resultado = int(valor1) % int(valor2)
    return print("El resultado es: " + str(resultado))

if Opcion == str(1):
    Suma(valor_1, valor_2)
else:
    if Opcion == str(2):
        Resta(valor_1, valor_2)
    else:
        if Opcion == str(3):
            Multiplicacion(valor_1, valor_2)
        else:
            if Opcion == str(4):
                Division(valor_1, valor_2)
            else:
                if Opcion == str(5):
                    Residuo(valor_1, valor_2)

input("a")