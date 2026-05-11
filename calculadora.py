def multiplicar(valor1, valor2):
    if not isinstance(valor1, (int, float)) or not isinstance(valor2, (int, float)):
        raise ValueError("Los valores ingresados deben ser numericos")
    else:
        return valor1 * valor2

def dividir(valor1, valor2):
    res = 0
    i = 0

    if valor2 == 0:
        raise ValueError("Division por cero")
    
    elif valor2 < 0 or valor1 < 0:
        raise ValueError("Solo maneja divisiones positivas")
    
    else:
        while res + valor2 <= valor1:
            res += valor2
            i += 1
        resto = valor1 - res
        return i, resto

def sumar(valor1, valor2):
    if not isinstance(valor1, (int, float)) or not isinstance(valor2, (int, float)):
        raise ValueError("Los valores ingresados deben ser numericos")
    else:
        return valor1 + valor2
    
def restar(valor1, valor2):
    if not isinstance(valor1, (int, float)) or not isinstance(valor2, (int, float)):
        raise ValueError("Los valores ingresados deben ser numericos")
    else:
        return valor1 - valor2

operaciones = {
    "x": multiplicar,
    "/": dividir,
    "+": sumar,
    "-": restar,
}

if __name__ == "__main__":
    print("calculadora: Ingrese los numeros y la operacion que desea realizar respectivamente.")

    try:
        valor1 = input("Primer valor ")
        operacion = input("Operacion ")
        valor2 = input("Segundo valor ")
    except ValueError:
        print("Debe ingresar numeros enteros")

    if operacion in operaciones:
        print(operaciones[operacion](valor1, valor2))

    else:
        print("operacion invalida")