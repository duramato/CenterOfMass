#encoding=utf-8
from builtins import input
def obter_pontos(lista_coordenadas, ponto, inverter):
    """
    Função auxiliar para obter,
    as coordenadas do "ponto" atual.
    :param x1: Coordenada x
    :param y1: Coordenada y 
    :param x2: Coordenada x do ponto seguinte.
    :param y2: Coordenada x do ponto seguinte.
    """
    if not inverter:
        x1 = lista_coordenadas[0][ponto]
        y1 = lista_coordenadas[1][ponto]
        x2 = lista_coordenadas[0][ponto+1]
        y2 = lista_coordenadas[1][ponto+1]
    else:
        x1 = lista_coordenadas[1][ponto]
        y1 = lista_coordenadas[0][ponto]
        x2 = lista_coordenadas[1][ponto+1]
        y2 = lista_coordenadas[0][ponto+1]
    return x1, y1, x2, y2
    
def inserir_dados(manualmente):
    if manualmente:
        while True:
            mensagem = "Tem de ser um número inteiro maior que 2\n"
            # Tentamos apanhar o erro, 
            # ou seja, se o utilizador digitar que não for um nº inteiro.
            try:
                n = int(input("Digite o numero de vertices do poligono, \no numero de vertices tem de ser maior que 2: "))
            except NameError:
                print(mensagem)
                continue
            
            if n <2:
                print(mensagem)
                continue
            lista_coordenadas = [[0 for i in range(0, n)] for j in range(0, 2)]
            for ponto in range(0, n):
                x = eval(input("Digite a {}ª coordenada x: ".format(ponto+1)))
                y = eval(input("Digite a {}ª coordenada y: ".format(ponto+1)))
                lista_coordenadas[0][ponto] = x
                lista_coordenadas[1][ponto] = y
            return n, lista_coordenadas
    else:
        nome_de_ficheiro = input("\nIndique o nome do ficheiro de entrada: \n(Inclua a extensão do ficheiro)\n")
        ficheiro = open(nome_de_ficheiro,"r")
        n = int(ficheiro.readline())
        ficheiro = ficheiro.readlines()

        lista_coordenadas = [[0 for i in range(0, n)] for j in range(0, 2)]
        for ponto in range(0, n):
            coordenadas = ficheiro[ponto]
            xy = coordenadas.split()
            lista_coordenadas[0][ponto] = int(xy[0])
            lista_coordenadas[1][ponto] = int(xy[1])
        return n, lista_coordenadas
        
def gravar_dados(resultados, nome_de_ficheiro):
    ficheiro = open(nome_de_ficheiro, "w")
    for dado in resultados:
        dado = "{0}\n".format(dado)
        ficheiro.write(str(dado))
    
def viavel(lista_coordenadas, n):
    import auxiliar.interseccoes as interseccao
    viabilidade = True
    for reta in range(0,n):
        x = lista_coordenadas[0][reta]
        y = lista_coordenadas[1][reta]
        x1 = lista_coordenadas[0][reta+1]
        y1 = lista_coordenadas[1][reta+1]
        pt1 = [x,y]
        pt2 = [x1,y1]
        for reta2 in range(0,n):
            x = lista_coordenadas[0][reta2]
            y = lista_coordenadas[1][reta2]
            x1 = lista_coordenadas[0][reta2+1]
            y1 = lista_coordenadas[1][reta2+1]
            ptA = [x,y]
            ptB = [x1,y1]
            if not reta == reta2:
                coord_intersec = interseccao.interseccoes(pt1, pt2, ptA, ptB)
                if (pt1[0] != coord_intersec[0] and pt2[0] != coord_intersec[0]\
                        and ptA[0] != coord_intersec[0] and ptB[0] != coord_intersec[0]) or \
                        (pt1[1] != coord_intersec[1] and pt2[1] != coord_intersec[1]\
                        and ptA[1] != coord_intersec[1] and ptB[1] != coord_intersec[1]):
                    viabilidade = False
    return viabilidade