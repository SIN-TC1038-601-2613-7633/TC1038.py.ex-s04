def main():
    """
    GameStore tiene venta de videojuegos los nuevos tienen un costo de 1,000 y los usados 350.

    Escribe un programa que sirva para calcular el total de la compra.

    Entrada

    Dos números enteros, uno en cada renglón, el primero es la cantidad de juegos nuevos y el segundo la cantidad de juegos usados.

    Salida

    El total de la compra

    Ejemplo:

    >>>2

    >>>3

    3050
    """
    cantidad_juegos_nuevos = int(input())
    cantidad_juegos_usados = int(input())

    total_compra = (cantidad_juegos_nuevos * 1000) + (cantidad_juegos_usados * 350)

    print(f"{total_compra:.0f}")

if __name__=='__main__':
    main()
