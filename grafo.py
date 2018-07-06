# -*- coding: utf-8 -*-

class Grafo:
    # construtor da classe grafo
    def __init__(self, nomeArq, qtdVertices, qtdArestas, arestas, aptidao, inseridos, maioresArestas, limites, qtdGrupos):
        self.qtdVertices = qtdVertices
        self.qtdArestas = qtdArestas
        self.arestas = arestas
        self.aptidao = aptidao
        self.inseridos = inseridos
        self.maioresArestas = maioresArestas
        self.limites = limites
        self.qtdGrupos = qtdGrupos
    
    # estrutura de dado: matriz de adjacencia
    def matrizAdjacencia(self):
        matriz = [0] * self.qtdVertices
        
        for lin in range(self.qtdVertices):
            matriz[lin] = [0] * self.qtdVertices
        
        # em "matriz" armazenamos as arestas que estão em "arestas"
        for i in range(self.qtdArestas):
            a = self.arestas[i][0]
            b = self.arestas[i][1]
            matriz[a][b] = self.arestas[i][2]
            matriz[b][a] = self.arestas[i][2]
                
        return matriz

    # estrutura de dado: matriz de incidencia
    def matrizIncidencia(self):
        matriz = [0] * self.qtdArestas

        for lin in range(self.qtdArestas):
            matriz[lin] = [0] * self.qtdVertices
            
        for i in range(self.qtdArestas):
            a = self.arestas[i][0]
            b = self.arestas[i][1]
            matriz[i][a] = self.arestas[i][2]
            matriz[i][b] = self.arestas[i][2]

        return matriz
        
    # estrutura de dados: lista de adjacencia
    def listaAdjacencia(self):
        listaAdjacencia = [0] * self.qtdVertices

        for lin in range(self.qtdVertices):
            listaAdjacencia[lin] = []

        for i in range(self.qtdArestas):
            a = self.arestas[i][0]
            b = self.arestas[i][1]
            listaAdjacencia[a].append([b, self.arestas[i][2]])
            listaAdjacencia[b].append([a, self.arestas[i][2]])
            
        return listaAdjacencia

    # imprime matriz de adjacencia
    def imprimeMatrizAdjacencia(self, matriz):
        print("\nMatriz de Adjacencia: \n")
        for lin in range(len(matriz)):
            print(matriz[lin])

    # imprime matriz de incidencia
    def imprimeMatrizIncidencia(self, matriz):
        print("\nMatriz de Incidencia: \n")
        for lin in range(self.qtdArestas):
            print(matriz[lin])

    # imnprime lista de incidencia
    def imprimeListaAdjacencia(self, lista):
        print("\nLista de Adjacencias: \n")
        for i in range(len(lista)):
            print(i, "->", lista[i])
