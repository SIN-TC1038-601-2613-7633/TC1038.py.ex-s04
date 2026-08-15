def main():
    """
    A inicio de año, las personas están preocupadas por su peso por lo que acuden a nutriólogos, gimnasios y cualquier otra cosa que les ayude en el proceso. Realiza un programa que ayude a las personas a indicar cuántos kilos debe bajar por mes una persona dados el peso inicial, el peso final y el número de meses que una persona estará en un programa integral para bajar de peso.

    Entradas

    Peso inicial (número decimal), peso final (número decimal), meses (número entero). Un dato en cada línea en ese orden.

    Salida

    Un número decimal que indique cuánto debe bajar por mes.

    Ejemplo de ejecución del programa:

    >>>60

    >>>55

    >>>4

    1.25
    """
    
    peso_inicial = float(input())
    peso_final = float(input())
    meses = int(input())

    kilos_a_bajar = peso_inicial - peso_final
    kilos_por_mes = kilos_a_bajar / meses

    print(f"{kilos_por_mes:.2f}")

if __name__=='__main__':
    main()
