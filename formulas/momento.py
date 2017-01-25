#encoding=utf-8
from __future__ import division
from auxiliar.ajudantes import obter_pontos

def formula(x1, y1, x2, y2):
    """
    Função para cálculo do momento estático.
    :param m: Calcula o momento estático
    :return: Devolve o resultado
    """
    m = ((1/2)*(((y2)**2)*(x2-x1)+(y1-y2)*(x2-x1)*(((2*y2)+y1)/3)))
    return m

def momento(lista_coordenadas, n):
    """
    Função para cálculo do momento estático,
    de um determinado poligono.
    :param mx: Momento estático segundo o eixo de x
    :param my: Momento estático segundo o eixo de y
    """
    mx = 0
    my = 0
    for ponto in range(0, n):
        x1, y1, x2, y2 = obter_pontos(lista_coordenadas, ponto, False)
        mx = mx + formula(x1, y1, x2, y2)
        x1, y1, x2, y2 = obter_pontos(lista_coordenadas, ponto, True)
        my = my + formula(x1, y1, x2, y2)
    return mx, my