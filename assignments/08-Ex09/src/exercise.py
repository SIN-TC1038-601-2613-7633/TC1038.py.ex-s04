def main():
    """
    Haz un programa sirva para calcular el precio que va a pagar un cliente por comprar cemento.

    El programa debe leer la cantidad de bultos de cemento que va a comprar el cliente, y el precio del bulto de cemento.

    El programa debe mostrar como salida 3 datos uno en cada renglón: el precio antes de impuestos, los impuestos (que son el 16% del precio) y el total a pagar por el cliente.

    Entrada

    La cantidad de bultos de cemento

    El precio por bulto de cemento

    Salidas

    El precio antes de impuestos

    Los impuestos

    El total a pagar

    Ejemplo de ejecución del programa:

    >>5

    >>180

    900.0

    144.0

    1044.0
    """

    cantidad_bultos = int(input())
    precio_bulto = float(input())

    precio_sin_impuestos = cantidad_bultos * precio_bulto
    impuestos = precio_sin_impuestos * 0.16
    total_a_pagar = precio_sin_impuestos + impuestos

    print(f"{precio_sin_impuestos:.1f}")
    print(f"{impuestos:.1f}")
    print(f"{total_a_pagar:.1f}")

if __name__=='__main__':
    main()
