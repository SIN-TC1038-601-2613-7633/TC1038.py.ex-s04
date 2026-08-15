def main():
    """
    En una universidad cada estudiante cursa 4 materias en el semestre. Desarrolla un programa que reciba la calificación de cada materia, calcula el promedio de las 4 materias y lo despliega.

    Entradas

    4 números enteros que representan las calificaciones de 4 materias, un número en cada renglón.

    Salidas

    Un número decimal correspondiente al promedio.

    Ejemplo de ejecución del programa

    >>> 90

    >>> 60

    >>> 100

    >>> 70

    80
    """

    calificación_parcial_1 = int(input())
    calificación_parcial_2 = int(input())
    calificación_parcial_3 = int(input())
    calificación_parcial_4 = int(input())
        
    promedio = (calificación_parcial_1+calificación_parcial_2+calificación_parcial_3+calificación_parcial_4) / 4

    print(f"{promedio:2}")    

    
if __name__=='__main__':
    main()
