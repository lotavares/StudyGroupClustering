# -*- coding: utf-8 -*-

from grafo import Grafo
from grupo import Grupo

def leArquivo(nomeArq, tipoEstrutura):
    arquivo = open(nomeArq)
    
    # leitura da primeira linha, qtdVertices e qtdGrupos
    qtds = arquivo.readline()
    qtds = qtds.split(' ')
    qtdVertices = int(qtds[0])
    qtdGrupos = int(qtds[1])
    print("qtdVertices: ", qtdVertices)
    print("qtdGrupos: ", qtdGrupos)

    # leitura da segunda linha, Li e Ui, limite inferior e superior
    limitesAux = arquivo.readline()
    limitesAux = limitesAux.split(' ')
    limites = [0] * qtdGrupos
    posAux = 0
    for i in range(qtdGrupos):
        limites[i] = [0] * 2
        # [i][0] é o limite inferior
        # [i][1] é o limite superior
        limites[i][0] = int(limitesAux[posAux])
        limites[i][1] = int(limitesAux[posAux + 1])
        posAux += 2
    for i in range(qtdGrupos):
        print limites[i]
    
    # leitura da terceira linha, pesos dos vértices
    aptidao = arquivo.readline()
    aptidao = list(map(int, aptidao.split(' ')))
    print aptidao
    
    # leitura do restante do arquivo, arestas
    qtdArestas = (qtdVertices * (qtdVertices - 1)) / 2
    arestas = [0] * qtdArestas
    
    for i in range(qtdArestas):
        arestas[i] = [0] * 3
    
    # "arestas" é uma matriz, em que cada linha tem 3 colunas que guardam u, v e duv, respectivamente
    
    # maioresArestas
    maioresArestas = [0] * qtdGrupos
    for i in range(qtdGrupos):
        maioresArestas[i] = [0] * 3
    # lista que define vertices que ja foram inseridos em um determinado grupo
    inseridos = [False] * qtdVertices
    print inseridos
    #leitura dos vertices do arquivo
    for i in range(qtdArestas):
        linha = arquivo.readline()
        valores = linha.split(' ')
        arestas[i][0] = (int(valores[0]))
        arestas[i][1] = (int(valores[1]))
        arestas[i][2] = (float(valores[2]))
        
        # (menorDoMaior) é o valor da aresta de menor peso da matriz (maioresArestas)
        menorDoMaior = maioresArestas[0][2]
        # posicao referente a aresta de menor valor(menorDoMaior)
        posMenor = 0
        for j in range(qtdGrupos):
            #verifica se o valor a ser inserido é menor que o menor valor da matriz 
            if maioresArestas[j][2] <= menorDoMaior:
                menorDoMaior = maioresArestas[j][2]
                posMenor = j
        #
        if inseridos[arestas[i][0]] or inseridos[arestas[i][1]]:
            for j in range(qtdGrupos):
                if inseridos[arestas[i][0]]:
                    if maioresArestas[j][0] == arestas[i][0] or maioresArestas[j][0] == arestas[i][1]:
                        if arestas[i][2] > maioresArestas[j][2]:
                            inseridos[maioresArestas[j][1]] = False
                            maioresArestas[j][0] = arestas[i][0]
                            maioresArestas[j][1] = arestas[i][1]
                            maioresArestas[j][2] = arestas[i][2]
                            inseridos[arestas[i][0]] = True
                            inseridos[arestas[i][1]] = True
                else:
                    if maioresArestas[j][1] == arestas[i][0] or maioresArestas[j][1] == arestas[i][1]:
                        if arestas[i][2] > maioresArestas[j][2]:
                            inseridos[maioresArestas[j][0]] = False
                            maioresArestas[j][0] = arestas[i][0]
                            maioresArestas[j][1] = arestas[i][1]
                            maioresArestas[j][2] = arestas[i][2]
                            inseridos[arestas[i][0]] = True
                            inseridos[arestas[i][1]] = True
        elif arestas[i][2] > menorDoMaior:
            inseridos[arestas[i][0]] = True
            inseridos[arestas[i][1]] = True
            inseridos[maioresArestas[posMenor][0]] = False
            inseridos[maioresArestas[posMenor][1]] = False
            maioresArestas[posMenor][0] = arestas[i][0]
            maioresArestas[posMenor][1] = arestas[i][1]
            maioresArestas[posMenor][2] = arestas[i][2]
            
    print inseridos
    for i in range(qtdGrupos):
        print maioresArestas[i]

    # chama o construtor do grafo
    grafo = Grafo(nomeArq, qtdVertices, qtdArestas, arestas, tipoEstrutura, aptidao, inseridos, maioresArestas, limites, qtdGrupos)
    
    return grafo

def montaGrupos(grafo):
    grupos = [Grupo] * grafo.qtdGrupos
    for i in range(grafo.qtdGrupos):
        grupos[i] = Grupo(grafo.limites[i][0], grafo.limites[i][1], grafo.maioresArestas[i])
        grupos[i].somaAptidao = grafo.aptidao[grafo.maioresArestas[i][0]] + grafo.aptidao[grafo.maioresArestas[i][1]]
        grupos[i].somaArestas = grafo.maioresArestas[i][2]
        print grupos[i].limInferior
        print grupos[i].limSuperior
        print grupos[i].somaAptidao
        print grupos[i].somaArestas
        print grupos[i].qtdVertices
        print grupos[i].qtdArestas
        print i, ": " , grupos[i].arestas , "\n"


def main():
    nomeArq = raw_input("Nome do arquivo: ")
    arquivo = open(nomeArq)

    print('''--> Escolha sua forma de armazenamento do grafo:
    -Digite A para Matriz de Adjacencia
    -Digite I para Matriz de Incidencia
    -Digite L para Lista de Adjacencia''')
    
    opcaoEscolhida = False
    while not(opcaoEscolhida):
        tipoEstrutura = raw_input("Tipo de estrutura: ")
        if tipoEstrutura == "A" or tipoEstrutura == "L" or tipoEstrutura == "I":
            opcaoEscolhida = True
        else:
            print("\nTipo de estrutura invalida\n")
    
    grafo = leArquivo(nomeArq, tipoEstrutura)

    if grafo.tipoEstrutura == "A":
        estrutura = grafo.matrizAdjacencia()
        #~ grafo.imprimeMatrizAdjacencia(estrutura)
    elif grafo.tipoEstrutura == "I":
        estrutura = grafo.matrizIncidencia()
        #~ grafo.imprimeMatrizIncidencia(estrutura)
    else:
        estrutura = grafo.listaAdjacencia()
        #~ grafo.imprimeListaAdjacencia(estrutura)

    
    montaGrupos(grafo)
    
    

    #~ menu = True
    #~ print('''--> Escolha uma acao, digite:
    #~ -1 para obter vizinhos de u
    #~ -2 para obter predecessores de u
    #~ -3 para obter sucessores de u
    #~ -4 para verificar se u e v sao vizinhos
    #~ -5 para verificar se v eh predecessor de u
    #~ -6 para verificar se v eh sucessor de u
    #~ -7 para deletar um vertice u
    #~ -8 para deletar uma aresta u v
    #~ -9 para gerar um subgrafo induzido por vertices
    #~ -10 para gerar um suggrafo induzido por arestas
    #~ -11 para imprimir o grafo na estrutura atual
    #~ -12 para converter estrutura atual para matriz de adjacencia
    #~ -13 para converter estrutura atual para matriz de incidencia
    #~ -14 para converter estrutura atual para lista de adjacencia
    #~ -SAIR para encerrar o programa''')

    #~ while menu:
        #~ opcao = int(input("Sua escolha eh: "))

        #~ imprime o menu novamente
        #~ elif opcao == 15:
            #~ print('''--> Escolha uma acao, digite:
            #~ -1 para obter vizinhos de u
            #~ -2 para obter predecessores de u
            #~ -3 para obter sucessores de u
            #~ -4 para verificar se u e v sao vizinhos
            #~ -5 para verificar se v eh predecessor de u
            #~ -6 para verificar se v eh sucessor de u
            #~ -7 para deletar um vertice u
            #~ -8 para deletar uma aresta u v
            #~ -9 para gerar um subgrafo induzido por vertices
            #~ -10 para gerar um suggrafo induzido por arestas
            #~ -11 para imprimir o grafo na estrutura atual
            #~ -12 para converter estrutura atual para matriz de adjacencia
            #~ -13 para converter estrutura atual para matriz de incidencia
            #~ -14 para converter estrutura atual para lista de adjacencia
            #~ -15 para imprimir o menu de opcoes
            #~ -SAIR para encerrar o programa''')
        #~ elif opcao == "SAIR":
            #~ menu = False
        #~ else:
            #~ print("->Opcao invalida, tente novamente\n")
        

if __name__ == "__main__":
    main()
