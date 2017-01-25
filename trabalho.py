#encoding=utf-8
from builtins import input

from formulas.area import area
from formulas.perimetro import perimetro
from formulas.momento import momento
from formulas.gravidade import gravidade
from formulas.prodinercia import prodinercia
from auxiliar.ajudantes import inserir_dados
from auxiliar.ajudantes import gravar_dados
from auxiliar.ajudantes import viavel

while True:
    metodo = eval(input("Como deseja introduzir os dados?\n  1.Manualmente\n  2.A partir de ficheiro previamente criado\n(introduza o número correspondente):\n"))
    if metodo == 1:
        manualmente = True
    elif metodo == 2:
        manualmente = False
    else:
        print("\nResposta inválida!!!\n")
        continue
        
    n, lista_coordenadas = inserir_dados(manualmente)
    
    # Passamos a difinir o ultima coordenadas 
    # como sendo igual à primeira.
    # e inserimos um extra valor ao final "n+1"
    lista_coordenadas[0].insert(n+1, lista_coordenadas[0][0])
    lista_coordenadas[1].insert(n+1, lista_coordenadas[1][0])
    
    # Passamos a testar a viabilidade do poligono
    if not viavel(lista_coordenadas, n):
        print("Figura não viavel\nRedefina as suas coordenadas.\n\n")
        continue    
    ax, ay = area(lista_coordenadas, n)
    p = perimetro(lista_coordenadas, n)
    mx, my = momento(lista_coordenadas, n)
    xg, yg = gravidade(mx, my, ax, ay)
    pxy = prodinercia(ax, xg, yg)
    import math
    print("{0:^40}".format("\n\nRESULTADOS\n"))
    print("Area:\n {0:<10.1f}".format(abs(ax)))
    print("Perimetro:\n {0:<10.1f}".format(p))
    print("Momento de x:\n {0:<10.1f}".format(mx))
    print("Momento de y:\n {0:<10.1f}".format(my))
    print("Centro de gravidade em x:\n {0:<10.1f}".format(xg))
    print("Centro de gravidade em y:\n {0:<10.1f}".format(yg))
    print("Produto de inércia:\n {0:<10.1f}".format(pxy))
    
    
    pergunta = input("\n\nDeseja gravar os resultados em ficheiro? (s/n): ")
    if pergunta.lower() == "s":
        resultados = []
        resultados.append(ax)
        resultados.append(ay)
        resultados.append(p)
        resultados.append(mx)
        resultados.append(my)
        resultados.append(xg)
        resultados.append(yg)
        resultados.append(pxy)
        nome_de_ficheiro = str((input("\nIndique o nome do ficheiro de saída: \n(O ficheiro será guardado em .txt)\n")))
        gravar_dados(resultados, "{}.txt".format(nome_de_ficheiro))
    elif pergunta.lower() == "n":
        pass
    else:
        print("\nResposta inválida!!!")
        pass
    pergunta = input("\nDeseja guardar as coordenadas para representação gráfica? (s/n): ")
    if pergunta.lower() =="s":
        resultados = []
        for ponto in range(0,n+1):
            x = lista_coordenadas[0][ponto]
            y = lista_coordenadas[1][ponto]
            pontos = "{},{}".format(x, y)
            if ponto == 0:
                pontos = "{},{},{},{}".format(x, y, xg, yg)
            resultados.append(pontos)
        nome_de_ficheiro = str((input("\nIndique o nome do ficheiro de saída: \n(O ficheiro será guardado em .txt)\n")))
        gravar_dados(resultados, "{}.txt".format(nome_de_ficheiro))
    elif pergunta.lower() == "n":
        pass
    else:
        print("\nResposta inválida!!!")
        pass
        
        
    pergunta = input("\n\nDeseja terminar? (s/n): ")
    if pergunta.lower() == "s":
        break
    elif pergunta.lower() == "n":
        continue
    else:
        print("\nResposta inválida!!!")
        pass