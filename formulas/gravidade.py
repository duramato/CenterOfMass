#encoding=utf-8
from __future__ import division
def gravidade(mx, my, ax, ay):
    """
    Função para cálculo do centro de gravidade,
    de um determinado 
    :param xg: Coordenada do centro de gravidade segundo o eixo x
    :param yg: Coordenada do centro de gravidade segundo o eixo y
    """
    xg = my/ay
    yg = mx/ax
    
    return xg, yg