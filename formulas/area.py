#encoding=utf-8
from __future__ import division
from auxiliar.ajudantes import obter_pontos

def formula(x1, y1, x2, y2):
    """
    Função para cálculo da área.
    :param a: Calcula a área
    :return: Devolve o resultado
    """
    a = ((y1+y2)/2)*(x2-x1)
    return a
    
def area(lista_coordenadas, n):
    """
    Função para cálculo da área,
    de um determinado poligono.
    :param ax: Área do poligono segundo o eixo x
    :param ay: Área do poligono segundo o eixo y
    """
    ax, ay = 0, 0
    for ponto in range(0, n):
    
        x1, y1, x2, y2 = obter_pontos(lista_coordenadas, ponto, False)
        ax = ax + formula(x1, y1, x2, y2)
        
        x1, y1, x2, y2 = obter_pontos(lista_coordenadas, ponto, True)
        ay = ay + formula(x1, y1, x2, y2)
    return ax, ay