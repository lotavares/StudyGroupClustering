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
    
    # estrutura de dado: matriz de adjacência
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

    # estrutura de dado: matriz de incidência
    def matrizIncidencia(self):
        matriz = [0] * self.qtdArestas

        for lin in range(self.qtdArestas):
            matriz[lin] = [0] * self.qtdVertices
        
        # em "matriz" armazenamos as arestas que estão em "arestas"
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

        # em "listaAdjacencia" armazenamos as arestas que estão em "arestas"
        for i in range(self.qtdArestas):
            a = self.arestas[i][0]
            b = self.arestas[i][1]
            listaAdjacencia[a].append([b, self.arestas[i][2]])
            listaAdjacencia[b].append([a, self.arestas[i][2]])
            
        return listaAdjacencia
