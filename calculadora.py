print("calculadora: Ingrese los numeros y la operacion que desea realizar respectivamente.")

try:
    valor1 = int(input("Primer valor "))
    operacion = input("Operacion ")
    valor2 = int(input("Segundo valor "))
except ValueError:
    print("Debe ingresar numeros enteros")


def multiplicar(valor1, valor2):
    res = 0
    for i in range(valor2):
        res += valor1
    return res

def dividir(valor1, valor2):
    res = 0
    i = 0

    if valor2 == 0:
        print("Error: Division por cero")

    else:
        while res + valor2 <= valor1:
            res += valor2
            i += 1
        resto = valor1 - res
        return i, resto

def sumar(valor1, valor2):
    res = 0
    valor1 += valor2
    res += valor1
    return res
    
def restar(valor1, valor2):
    res = 0
    valor1 -= valor2
    res += valor1
    return res

operaciones = {
    "x": multiplicar,
    "/": dividir,
    "+": sumar,
    "-": restar,
}

if operacion in operaciones:
    print(operaciones[operacion](valor1, valor2))

else:
    print("operacion invalida")