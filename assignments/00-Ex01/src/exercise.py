def main():
    """
    Escribe un programa que lea los datos: base (b) y altura (h) y muestre el área del triángulo.

    Entrada:

    base y altura, uno en cada renglón, usa valores flotantes.

    Salida

    El área del triángulo

    Ejemplo de ejecución del programa

    >>> 10

    >>> 4

    20.0
    """
    
    base = float(input())
    altura = float(input())

    area = base * altura / 2

    print(area)

if __name__=='__main__':
    main()
