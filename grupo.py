# -*- coding: utf-8 -*-

class Grupo:
    def __init__(self, limInferior, limSuperior, arestas):
        self.limInferior = limInferior
        self.limSuperior = limSuperior
        self.somaAptidao = 0
        self.somaArestas = 0
        self.qtdVertices = 2
        self.qtdArestas = 1
        self.arestas = arestas
