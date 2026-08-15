def main():
    """
    Una compañía de telefonía celular cobra $0.80 por mensaje, por mega o por minuto. Realiza un programa que calcule el costo total mensual de un usuario según estos datos.

    Entradas:

    El número de mensajes (número entero), el número de megas (número flotante) y el número de minutos (número entero). Un dato por línea y en ese orden.

    Salidas:

    Un número que representa el costo mensual.

    Ejemplo de ejecución del programa:

    >>38

    >>3.1

    >>78

    95.28
    """

    mensajes = int(input())
    megas = float(input())
    minutos = int(input())

    costo_mensajes = mensajes * 0.80
    costo_megas = megas * 0.80
    costo_minutos = minutos * 0.80

    costo_total = costo_mensajes + costo_megas + costo_minutos

    print(f"{costo_total:.2f}")


if __name__=='__main__':
    main()
