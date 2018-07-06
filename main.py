# -*- coding: utf-8 -*-

from grafo import Grafo
from grupo import Grupo
import time

# método de ordenação quick-sort, utilizado para ordenar as arestas em forma decrescente
def quickSortAux(vetor, esquerda, direita):
    i = esquerda
    j = direita
    pivo = vetor[int((j + i) / 2)][2]
    while i <= j:
        while vetor[i][2] > pivo:
            i += 1
        while (vetor[j][2] < pivo):
            j -= 1
        if i <= j:
            aux = vetor[i]
            vetor[i] = vetor[j]
            vetor[j] = aux
            i += 1
            j -= 1
    if esquerda < j:
        quickSortAux(vetor, esquerda, j)
    if i < direita:
        quickSortAux(vetor, i, direita)

def quickSort(vetor, tam):
    quickSortAux(vetor, 0, tam - 1)

# leitura do arquivo, o construtor do grafo é chamado nessa função
def leArquivo(nomeArq):
    arquivo = open(nomeArq)
    
    # leitura da primeira linha, qtdVertices e qtdGrupos
    qtds = arquivo.readline()
    qtds = qtds.split(' ')
    qtdVertices = int(qtds[0])
    qtdGrupos = int(qtds[1])

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
    
    # leitura da terceira linha, pesos dos vértices
    aptidao = arquivo.readline()
    aptidao = list(map(int, aptidao.split(' ')))
    
    # leitura do restante do arquivo, arestas
    qtdArestas = int((qtdVertices * (qtdVertices - 1)) / 2)
    arestas = [0] * qtdArestas
    
    for i in range(qtdArestas):
        arestas[i] = [0] * 3
    
    # 'arestas' é uma lista de arestas, cada aresta contendo dois vértices e o peso da aresta que os liga
    
    # lista que define quais vertices já fazem parte de um grupo, todos recebem false inicialmente
    inseridos = [False] * qtdVertices
   
    #leitura das arestas do arquivo
    for i in range(qtdArestas):
        linha = arquivo.readline()
        valores = linha.split(' ')
        arestas[i][0] = (int(valores[0]))
        arestas[i][1] = (int(valores[1]))
        arestas[i][2] = (float(valores[2]))

    # colocamos em 'listaAux' todas as arestas do grafo e a ordenamos
    listaAux = arestas
    quickSort(listaAux, qtdArestas)
    
    # 'maioresArestas' guarda as maiores arestas do grafo
    maioresArestas = []
    qtdInseridos = 0
    i = 0
    
    # 'maioresArestas' recebe as maiores arestas, o tamanho de 'maioresArestas' é determinado pela quantidade de grupos exigidos
    while i < qtdArestas and qtdInseridos < qtdGrupos:
        jaExiste = False
        # vemos se a aresta atual pode ser inserida, ela poderá se nenhum vertice já fizer parte de 'maioresArestas'
        for j in range(len(maioresArestas)):
            if listaAux[i][0] == maioresArestas[j][0] or listaAux[i][0] == maioresArestas[j][1]:
                jaExiste = True
            if listaAux[i][1] == maioresArestas[j][0] or listaAux[i][1] == maioresArestas[j][1]:
                jaExiste = True
        # caso a aresta possa ser inserida, a inserimos, caso não, continuamos verificando qual pode
        if not(jaExiste):
            aux = listaAux[i]
            maioresArestas.append(aux)
            qtdInseridos += 1
        i += 1

    # 'inseridos' recebe true nas posições dos vértices que estãos em 'maioresArestas'
    for i in range(qtdGrupos):
        inseridos[maioresArestas[i][0]] = True
        inseridos[maioresArestas[i][1]] = True

    # chamada do construtor do grafo
    grafo = Grafo(nomeArq, qtdVertices, qtdArestas, arestas, aptidao, inseridos, maioresArestas, limites, qtdGrupos)
    
    return grafo

def montaGrupos(grafo):
    # cria uma lista de grupos contendo inicialmente dois vertices e uma aresta, cada grupo recebe uma das 'maioresArestas'
    # dessa forma, iniciamos todos os grupos
    grupos = [Grupo] * grafo.qtdGrupos
    for i in range(grafo.qtdGrupos):
        grupos[i] = Grupo(grafo.limites[i][0], grafo.limites[i][1], grafo.maioresArestas[i])
        grupos[i].somaAptidao = grafo.aptidao[grafo.maioresArestas[i][0]] + grafo.aptidao[grafo.maioresArestas[i][1]]
        grupos[i].somaArestas = grafo.maioresArestas[i][2]
    
    return grupos

def main():
    # 'executando' é uma variável auxiliar para indicar se o usuário deseja rodar o programa mais vezes
    executando = True
    while executando:
        nomeArq = input("\nNome do arquivo: ")
        arquivo = open(nomeArq)
        
        print('''\n--> Escolha sua forma de armazenamento do grafo:
        -Digite 1 para Matriz de Adjacencia
        -Digite 2 para Matriz de Incidencia
        -Digite 3 para Lista de Adjacencia
        -Digite 4 para encerrar o programa''')
    
        opcao = int(input("\nSua escolha e': "))
        
        opcaoEscolhida = False
        while not(opcaoEscolhida):
            if opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4:
                opcaoEscolhida = True
            else:
                print("\nEscolha invalida\n")
                opcao = int(input("\nSua escolha e': "))
        
        grafo = leArquivo(nomeArq)
        
        # iniciamos a execução do programa nesse ponto
        # escolhemos essa linha para não incluir a escolha do usuário na soma do tempo
        inicio = time.time()
        grupos = montaGrupos(grafo)
        somaQtdVertices = 0
        somaArestas = 0
        opcaoInvalida = False
        
        # executa o programa utilizando matriz de adjacência
        if opcao == 1:
            # criação da matriz de adjacência
            estrutura = grafo.matrizAdjacencia()
            
            # chamada do método que calcula quais vértices devem fazer parte de 'grupos[i]' com o limitante inferior
            for i in range(grafo.qtdGrupos):
                grupos[i].matAdLimInf(grafo, estrutura)
                somaQtdVertices += grupos[i].qtdVertices
                somaArestas += grupos[i].somaArestas

            somaQtdVertices = 0
            
            # chamada do método que calcula quais vértices devem fazer parte de 'grupos[i]' com o limitante superior
            for i in range(grafo.qtdGrupos):
                grupos[i].matAdLimSup(grafo, estrutura)
                somaQtdVertices += grupos[i].qtdVertices
                somaArestas += grupos[i].somaArestas
            
            # encerramos o tempo nessa linha, pois a partir dela, temos apenas prints
            fim = time.time()
            
            # imprimimos as informações gerais
            print("\nQuantidade de vértices pertencentes a algum grupo: ", somaQtdVertices)
            print("Somatorio total das arestas de todos os grupos: ", somaArestas)
            print("Tempo de execucao em segundos: ", fim - inicio)
            
            print('''\n--> Para mais informacoes de cada grupo:
            -Digite 1 para SIM
            -Digite 2 para NAO''')
            escolha = int(input("\nSua escolha e': "))
            
            # caso o usuário opte por obter as informações individuais dos grupos, as imprimimos
            if escolha == 1:
                for i in range(grafo.qtdGrupos):
                    print("\nGrupo: ", (i + 1))
                    print("Somatorio das aptidoes: ", grupos[i].somaAptidao)
                    print("Somatorio das arestas: ", grupos[i].somaArestas)
                    print("Somatorio da quantidade de vertices: ", grupos[i].qtdVertices)
                    print("Quantidade de arestas: ", grupos[i].qtdArestas)
                    print("Vertices: ", grupos[i].vertices)
                    print("Arestas: ", grupos[i].arestas)
        
        # executa o programa utilizando matriz de incidencia
        elif opcao == 2:
            # criação da matriz de incidência
            estrutura = grafo.matrizIncidencia()
            
            # chamada do método que calcula quais vértices devem fazer parte de 'grupos[i]' com o limitante inferior
            for i in range(grafo.qtdGrupos):
                grupos[i].matIncLimInf(grafo, estrutura)
                somaQtdVertices += grupos[i].qtdVertices
                somaArestas += grupos[i].somaArestas
            
            somaQtdVertices = 0
            
            # chamada do método que calcula quais vértices devem fazer parte de 'grupos[i]' com o limitante superior
            for i in range(grafo.qtdGrupos):
                grupos[i].matIncLimSup(grafo, estrutura)
                somaQtdVertices += grupos[i].qtdVertices
                somaArestas += grupos[i].somaArestas
                
            # encerramos o tempo nessa linha, pois a partir dela, temos apenas prints
            fim = time.time()

            # imprimimos as informações gerais
            print("\nQuantidade de vértices pertencentes a algum grupo: ", somaQtdVertices)
            print("Somatorio total das arestas de todos os grupos: ", somaArestas)
            print("Tempo de execucao em segundos: ", fim - inicio)
            
            print('''\n--> Para mais informacoes de cada grupo:
            -Digite 1 para SIM
            -Digite 2 para NAO''')
            escolha = int(input("\nSua escolha e': "))
            
            # caso o usuário opte por obter as informações individuais dos grupos, as imprimimos
            if escolha == 1:
                for i in range(grafo.qtdGrupos):
                    print("\nGrupo: ", (i + 1))
                    print("Somatorio das aptidoes: ", grupos[i].somaAptidao)
                    print("Somatorio das arestas: ", grupos[i].somaArestas)
                    print("Somatorio da quantidade de vertices: ", grupos[i].qtdVertices)
                    print("Quantidade de arestas: ", grupos[i].qtdArestas)
                    print("Vertices: ", grupos[i].vertices)
                    print("Arestas: ", grupos[i].arestas)
        
        # executa o programa utilizando lista de adjacencia
        elif opcao == 3:
            # criação da lista de adjacência
            estrutura = grafo.listaAdjacencia()
            
            # chamada do método que calcula quais vértices devem fazer parte de 'grupos[i]' com o limitante inferior
            for i in range(grafo.qtdGrupos):
                grupos[i].listAdLimInf(grafo, estrutura)
                somaQtdVertices += grupos[i].qtdVertices
                somaArestas += grupos[i].somaArestas
                
            somaQtdVertices = 0
            
            # chamada do método que calcula quais vértices devem fazer parte de 'grupos[i]' com o limitante superior
            for i in range(grafo.qtdGrupos):
                grupos[i].listAdLimSup(grafo, estrutura)
                somaQtdVertices += grupos[i].qtdVertices
                somaArestas += grupos[i].somaArestas
                
            # encerramos o tempo nessa linha, pois a partir dela, temos apenas prints
            fim = time.time()

            # imprimimos as informações gerais
            print("\nQuantidade de vértices pertencentes a algum grupo: ", somaQtdVertices)
            print("Somatorio total das arestas de todos os grupos: ", somaArestas)
            print("Tempo de execucao em segundos: ", fim - inicio)
            
            print('''\n--> Para mais informacoes de cada grupo:
            -Digite 1 para SIM
            -Digite 2 para NAO''')
            escolha = int(input("\nSua escolha e': "))
            
            # caso o usuário opte por obter as informações individuais dos grupos, as imprimimos
            if escolha == 1:
                for i in range(grafo.qtdGrupos):
                    print("\nGrupo: ", (i + 1))
                    print("Somatorio das aptidoes: ", grupos[i].somaAptidao)
                    print("Somatorio das arestas: ", grupos[i].somaArestas)
                    print("Somatorio da quantidade de vertices: ", grupos[i].qtdVertices)
                    print("Quantidade de arestas: ", grupos[i].qtdArestas)
                    print("Vertices: ", grupos[i].vertices)
                    print("Arestas: ", grupos[i].arestas)
        
        # o usuário optou por terminar a execução do programa
        elif opcao == 4:
            executando = False
        
        # o usuário entrou com um caractere inválido
        else:
            print("\n->Opcao invalida, tente novamente\n")
            opcaoInvalida = True
        
        # caso o usuário não tenha entrado com um caractere inválido, e não optou por encerrar o programa, ele tem a opção de executar novamente o programa
        if not(opcaoInvalida) and opcao != 4:
            print('''\n--> Para executar novamente:
                -Digite 1 para SIM
                -Digite 2 para NAO''')
            escolha = int(input("\nSua escolha e': "))
            
            if escolha == 2:
                executando = False
    

if __name__ == "__main__":
    main()
