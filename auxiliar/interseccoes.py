import math
def interseccoes(A, B, C, D): 
    tolerancia_determinante = 0.00000001
    ponto_interseccao = [0,0]
    a, b = A
    c, d = B
    e, f = C
    g, h = D
    determinante = ((-(c - a)) * (h - f) + (d - b) * (g - e))
    if math.fabs(determinante) < tolerancia_determinante:
        return ponto_interseccao
    else:
        tolerancia_determinante = 1.0/determinante
        r = tolerancia_determinante * ((-(h - f)) * (e-a) + (g - e) * (f-b))
        s = tolerancia_determinante * ((-(d - b)) * (e-a) + (c - a) * (f-b))
        xi = (a + r*(c - a) + e + s*(g - e))/2.0
        yi = (b + r*(d - b) + f + s*(h - f))/2.0
        ponto_interseccao = [xi,yi]
    return ponto_interseccao