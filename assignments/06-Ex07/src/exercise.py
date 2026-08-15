def main():
    """
    Un caracol de un terrario de una primaria pública corre a 5.7 mm/s. Realiza un programa para indicar cuántos centímetros recorrerá el caracol en una cantidad de minutos dada por el usuario.

    Entradas

    Un número decimal que representa los minutos.

    Salidas

    Un número decimal que indica los centímetros recorridos.

    Ejemplo de ejecución

    >>> 1

    34.2
    """

    minutos = float(input())

    velocidad_caracol = 5.7 # mm/s
    segundos = minutos * 60 # s
    distancia_recorrida = velocidad_caracol * segundos # mm
    distancia_recorrida_cm = distancia_recorrida / 10 # cm

    print(f"{distancia_recorrida_cm:.1f}")
    
if __name__=='__main__':
    main()
