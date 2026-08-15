def main():
    """
    Crea un programa que pregunte al usuario su edad y el año actual, como resultado le indicará el año en que cumplirá 100 años.

    NOTA: Haz la versión simple de este ejercicio, es decir, no consideres el mes de nacimiento, solo el año. Después haremos una en la que sí consideraremos el mes de nacimiento.

    Entrada

    La edad (entero positivo) de la persona y el año actual (entero positivo), en este orden.

    Salida

    El año (entero positivo) en el que la persona cumplirá 100 años.

    Ejemplo de ejecución del programa

    >>>15

    >>>2025

    2110
    """

    edad = int(input())
    agno_actual = int(input())
    
    agno_cumple_100 = agno_actual + (100 - edad)

    print(agno_cumple_100)   

    
if __name__=='__main__':
    main()
