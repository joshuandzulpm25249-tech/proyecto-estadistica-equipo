def multiplicacion (a,b):
    rest = a*b
    return rest 
"""
devuelve el resultado de multiplicacion.
Args:
    a(float): Primer valor a multiplicar.
    b(float): Segundo valor a multiplicar.

Return:
    rest(float):resultado de la multiplicacion.
"""
def divicion (a,b):
    rest = a/b
    return rest 
"""
devuelve el resultado de divicion.
Args:
    a(float): Primer valor a dividir.
    b(float): Segundo valor a dividir.

Return:
    rest(float):Resultado de la divicion:
"""
def main():
    print("---Analizador de datos v1.0---")
    datos = [10,20,30,40,50,60] #datos de prueba
    print(f"datos a procesar: {datos}")

    #aqui se llamaran las funciones de los integrantes del equipo
if __name__ == "__main__":
    main()