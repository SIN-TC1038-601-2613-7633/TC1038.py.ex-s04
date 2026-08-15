def main():
    """
    Realiza un programa que reciba las coordenadas de dos puntos y que calcule la pendiente de la recta que une esos dos puntos.

    La fórmula para calcular la pendiente es:

    m = (y2 - y1) / (x2 - x1)

    Entradas

    Cuatro números con punto decimal que representan las coordenadas x1, y1, x2, y2. Uno en cada línea y en el orden que se especifica.

    Salidas

    Un número decimal que representa la pendiente.

    Ejemplo de ejecución del programa:

    >>>3.6                                                                                                                                                       

    >>>-1.3                                                                                                                                                     

    >>>8.6                                                                                                                                                       

    >>>2.5                                                                                                                                                       

    0.76
    """
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())

    pendiente = (y2 - y1) / (x2 - x1)

    print(f"{pendiente:.2f}")

if __name__=='__main__':
    main()
