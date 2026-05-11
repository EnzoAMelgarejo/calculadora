# Ejecutar solo tests smoke
# py -m pytest -m smoke

# Ejecutar solo tests exception
# py -m pytest -m exception

import pytest
from calculadora import sumar, dividir, restar, multiplicar



#FIXTURES
#FIXTURES
#FIXTURES



@pytest.fixture #FIXTURES
def numerosEnteros():
    "Prepara valores de prueba reutilizables para los diferentes tests"
    return 20, 5



#TEST
#TEST
#TEST



@pytest.mark.parametrize("a, b, res", [(2, 3, 5), (1, -1, 0), (7.4, 0.3, 7.7)])

@pytest.mark.smoke
def test_suma_exitosa(a, b, res):
    assert a, b == res

@pytest.mark.parametrize("a, b", [("a", 5), (5,"a"), ("a", "b")])

@pytest.mark.smoke
def test_suma_fallo(a, b):
    with pytest.raises(ValueError):
        sumar(a, b)

@pytest.mark.parametrize("a, b, res", [(2, 3, -1), (1, -1, 2), (7.4, 0.3, 7.1)])

def test_resta_exitosa(a, b, res):
    assert restar(a, b)  == pytest.approx(res)

@pytest.mark.parametrize("a, b", [("a", 5), (5,"a"), ("a", "b")])        

def test_resta_fallo(a, b):
    with pytest.raises(ValueError):
        restar(a, b)

@pytest.mark.parametrize("a, b, res", [(2, 3, 6), (1, -1, -1), (7.4, 0.3, 2.22)])
def test_multilicacion_exitosa(a, b, res):
    assert multiplicar(a, b)  == pytest.approx(res)

@pytest.mark.parametrize("a, b", [("a", 5), (5,"a"), ("a", "b")])        

def test_nultiplicacion_fallo(a, b):
    with pytest.raises(ValueError):
        multiplicar(a, b)

@pytest.mark.parametrize(
    "a, b, res", 
    [
        (50, 20, (2, 10)),
        (30, 3, (10, 0)),
        (7, 2, (3, 1))
    ]
    )

@pytest.mark.smoke
def test_division_exitosa(a, b, res):
    assert dividir(a, b) == res

@pytest.mark.smoke
def test_division_cero():
    with pytest.raises(ValueError) as excinfo: #Ejemplo de un assert avanzado para verificar no solo el error sino el tipo de error
        dividir(1, 0)
        assert "No se puede dividir por cero" in str(excinfo.value) #Verifica que el mensaje programado este contenido dentro del error

@pytest.mark.parametrize("a, b", [(-5, 10), (5,-10), (-5, -10)])

@pytest.mark.smoke
def test_dividir_numerosNegativos(a, b):
    with pytest.raises(ValueError) as excinfo:
        dividir(a, b)
        assert "Solo maneja divisiones entereas" in str(excinfo.value)
