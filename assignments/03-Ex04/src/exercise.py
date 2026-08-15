def main():
    """
    Realiza un programa que indique el número de lustros que ha vivido una persona por medio de su año de nacimiento y el año actual.

    Entradas:

    Dos números enteros. Primero el año de nacimiento y luego, el año actual. Uno en cada línea.

    Salidas:

    Un número con punto decimal que representa los lustros vividos por la persona. Solo el número. No poner ningún mensaje.

    Ejemplo de ejecución del programa:

    >>>2003

    >>>2025

    4.4
    """

    agno_nacimiento = int(input())
    agno_actual = int(input())
    
    lustros_vividos = (agno_actual - agno_nacimiento) / 5

    print(f"{lustros_vividos:.1f}")


if __name__=='__main__':
    main()
