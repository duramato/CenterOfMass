#encoding=utf-8
def perimetro(lista_coordenadas, n):
    """
    Função para cálculo do perimetro,
    de um determinado poligono
    """
    p = 0
    # importamos a função interna math
    from math import sqrt
    for ponto in range(0, n):
        x1 = int(lista_coordenadas[0][ponto])
        y1 = int(lista_coordenadas[1][ponto])
        
        x2 = int(lista_coordenadas[0][ponto+1])
        y2 = int(lista_coordenadas[1][ponto+1])
        calculo = sqrt((x2-x1)**2+(y2-y1)**2)
        try:
            p = p + calculo
        except ValueError:
            print("Cálculo impossivel.")
    return p