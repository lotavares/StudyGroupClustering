# -*- coding: utf-8 -*-

class Grupo:
    # construtor da classe grupo
    def __init__(self, limInferior, limSuperior, arestas):
        self.limInferior = limInferior
        self.limSuperior = limSuperior
        self.somaAptidao = 0
        self.somaArestas = 0
        self.qtdVertices = 2
        self.qtdArestas = 1
        # 'arestas' guarda as arestas de um grupo
        self.arestas = [1]
        # 'arestas' recebe a primeira aresta do grupo (uma de 'maioresArestas)
        self.arestas[0] = arestas
        self.vertices = []
        # 'vertices' recebe os vértices que ligam a primeira aresta do grupo
        self.vertices.append(arestas[0])
        self.vertices.append(arestas[1])
    
    # método que encontra os primeiros vértices do grafo que farão parte do grupo, tendo o 'limInferior' como limitante
    # algoritmo para a estrutura matriz de adjacência
    def matAdLimInf(self, grafo, matrizAdjacencia):
        # entramos no while se o somatório das aptidões dos vértices já pertencentes ao grupo for menor ou igual ao limite inferior
        while self.somaAptidao <= self.limInferior:
            maiorArestaAtual = 0
            vertice = -1
            # percorre os vértices do grupo atual
            for i in range(self.qtdVertices):
                # percorre todas as arestas do grafo ligadas ao vertices[i] do grupo
                for j in range(grafo.qtdVertices):
                    # se o vertice não estiver em nenhum outro grupo, então verificamos se alguma de suas arestas é maior que a 'maiorArestaAtual'
                    if not grafo.inseridos[j]:
                        if matrizAdjacencia[self.vertices[i]][j] > maiorArestaAtual:
                            # se for maior, verificamos se não ultrapassa o limite superior
                            # caso não ultrapasse, a 'maiorArestaAtual' recebe a maior aresta do vértice i
                            if (self.somaAptidao + grafo.aptidao[j]) < self.limSuperior:
                                maiorArestaAtual = matrizAdjacencia[self.vertices[i]][j];
                                vertice = j
            # atualizamos os atributos do grupo atual, adicionado o vértice que ligava a maior aresta em questão ao grupo
            if vertice != -1:
                grafo.inseridos[vertice] = True
                self.somaAptidao += grafo.aptidao[vertice]
                self.qtdArestas += self.qtdVertices
                # adicionamos ao grupo todas as arestas do vértice que está sendo inserido que têm ligação com os vértices já existentes
                for i in range(self.qtdVertices):
                    # somamos à 'somaArestas' a aresta que está sendo adicionada ao grupo
                    self.somaArestas += matrizAdjacencia[self.vertices[i]][vertice]
                    aux = []
                    # vertice 1
                    aux.append(vertice)
                    # vertice 2
                    aux.append(self.vertices[i])
                    # valor da aresta 1 - 2
                    aux.append(matrizAdjacencia[self.vertices[i]][vertice])
                    self.arestas.append(aux)
                self.qtdVertices += 1
                self.vertices.append(vertice)

    # método que armazena os vértices que não foram inseridos em 'matAdLimInf', tendo o 'limSuperior' como limitante
    # algoritmo para a estrutura matriz de adjacência
    def matAdLimSup(self, grafo, matrizAdjacencia):
        cont = 0
        # entramos no while se o somatório das aptidões dos vértices já pertencentes ao grupo for menor ou igual ao limite superior
        while self.somaAptidao <= self.limSuperior and cont != grafo.qtdVertices:
            maiorArestaAtual = 0
            vertice = -1
            # percorre os vértices do grupo atual
            for i in range(self.qtdVertices):
                # percorre todas as arestas do grafo ligadas ao vertices[i] do grupo
                for j in range(grafo.qtdVertices):
                    # se o vertice não estiver em nenhum outro grupo, então verificamos se alguma de suas arestas é maior que a 'maiorArestaAtual'
                    if not grafo.inseridos[j]:
                        if matrizAdjacencia[self.vertices[i]][j] > maiorArestaAtual:
                            # se for maior, verificamos se não ultrapassa o limite superior
                            # caso não ultrapasse, a 'maiorArestaAtual' recebe a maior aresta do vértice i
                            if (self.somaAptidao + grafo.aptidao[j]) < self.limSuperior:
                                maiorArestaAtual = matrizAdjacencia[self.vertices[i]][j];
                                vertice = j
            # atualizamos os atributos do grupo atual, adicionado o vértice que ligava a maior aresta em questão ao grupo
            if vertice != -1:
                grafo.inseridos[vertice] = True
                self.somaAptidao += grafo.aptidao[vertice]
                self.qtdArestas += self.qtdVertices
                # adicionamos ao grupo todas as arestas do vértice que está sendo inserido que têm ligação com os vértices já existentes
                for i in range(self.qtdVertices):
                    # somamos à 'somaArestas' a aresta que está sendo adicionada ao grupo
                    self.somaArestas += matrizAdjacencia[self.vertices[i]][vertice]
                    aux = []
                    # vertice 1
                    aux.append(vertice)
                    # vertice 2
                    aux.append(self.vertices[i])
                    # valor da aresta 1 - 2
                    aux.append(matrizAdjacencia[self.vertices[i]][vertice])
                    self.arestas.append(aux)
                self.qtdVertices += 1
                self.vertices.append(vertice)
            cont += 1
    
    # método que encontra os primeiros vértices do grafo que farão parte do grupo, tendo o 'limInferior' como limitante
    # algoritmo para a estrutura matriz de incidência
    def matIncLimInf(self, grafo, matrizIncidencia):
        cont = 0
        # entramos no while se o somatório das aptidões dos vértices já pertencentes ao grupo for menor ou igual ao limite inferior
        while self.somaAptidao <= self.limInferior and cont != grafo.qtdVertices:
            maiorArestaAtual = 0
            vertice = -1
            aresta = 0
            # percorre os vértices do grupo atual
            for i in range(self.qtdVertices):
                # percorre todas as arestas do grafo ligadas ao vertices[i] do grupo
                for j in range(grafo.qtdArestas):
                    # se o vertice não estiver em nenhum outro grupo, então verificamos se alguma de suas arestas é maior que a maiorArestaAtual 
                    # encontramos as arestas incidentes ao vértice i
                    if matrizIncidencia[j][self.vertices[i]] != 0:
                        # encontramos no for seguinte, a qual vértice se liga o vértice i
                        for k in range(grafo.qtdVertices):
                            # caso encontremos o outro vértice, verificamos se ele já está no grupo
                            if matrizIncidencia[j][k] != 0 and k != self.vertices[i] and not grafo.inseridos[k]:
                                # se a aresta que liga o vértice[i] ao vértice k for maior que a 'maiorArestaAtual', vamos para a próxima verificação
                                if matrizIncidencia[j][k] > maiorArestaAtual:
                                    # verificamos se não ultrapassa o limite superior
                                    if (self.somaAptidao + grafo.aptidao[k]) < self.limSuperior:
                                        maiorArestaAtual = matrizIncidencia[j][k]
                                        vertice = k
                                        aresta = j
            # atualizamos os atributos do grupo atual, adicionado o vértice que ligava a maior aresta em questão ao grupo, caso tenhamos encontrado o vértice
            if vertice != -1:
                # colocamos True no vértice que está sendo inserido no grupo, o que significa que ele não pode participar de nenhum outro grupo
                grafo.inseridos[vertice] = True
                # somamos a aptidão do vértice que está sendo adicionado à 'somaAptidao'
                self.somaAptidao += grafo.aptidao[vertice]
                self.qtdArestas += self.qtdVertices
                for i in range(self.qtdVertices):
                    j = 0
                    contador = 0
                    # adicionamos ao grupo todas as arestas do vértice que está sendo inserido que têm ligação com os vértices já existentes no grupo
                    while j < grafo.qtdArestas and contador != self.qtdVertices:
                        if matrizIncidencia[j][self.vertices[i]] != 0 and matrizIncidencia[j][vertice] != 0:
                            # somamos à 'somaArestas' a aresta que está sendo adicionada ao grupo
                            self.somaArestas += matrizIncidencia[j][vertice]
                            aux = []
                            # vertice 1
                            aux.append(vertice)
                            # vertice 2
                            aux.append(self.vertices[i])
                            # valor da aresta 1 - 2
                            aux.append(matrizIncidencia[j][vertice])
                            self.arestas.append(aux)
                            contador += 0
                        j += 1
                self.qtdVertices += 1
                self.vertices.append(vertice)
            cont += 1
    
    # método que armazena os vértices que não foram inseridos em 'matIncLimInf', tendo o 'limSuperior' como limitante
    # algoritmo para a estrutura matriz de incidência
    def matIncLimSup(self, grafo, matrizIncidencia):
        cont = 0
        # entramos no while se o somatório das aptidões dos vértices já pertencentes ao grupo for menor ou igual ao limite superior
        while self.somaAptidao <= self.limSuperior and cont != grafo.qtdVertices:
            maiorArestaAtual = 0
            vertice = -1
            aresta = 0
            # percorre os vértices do grupo atual
            for i in range(self.qtdVertices):
                # percorre todas as arestas do grafo ligadas ao vertices[i] do grupo
                for j in range(grafo.qtdArestas):
                    # se o vertice não estiver em nenhum outro grupo, então verificamos se alguma de suas arestas é maior que a maiorArestaAtual 
                    # encontramos as arestas incidentes ao vértice i
                    if matrizIncidencia[j][self.vertices[i]] != 0:
                        # encontramos no for seguinte, a qual vértice se liga o vértice i
                        for k in range(grafo.qtdVertices):
                            # caso encontremos o outro vértice, verificamos se ele já está no grupo
                            if matrizIncidencia[j][k] != 0 and k != self.vertices[i] and not grafo.inseridos[k]:
                                # se a aresta que liga o vértice[i] ao vértice k for maior que a 'maiorArestaAtual', vamos para a próxima verificação
                                if matrizIncidencia[j][k] > maiorArestaAtual:
                                    # verificamos se não ultrapassa o limite superior
                                    if (self.somaAptidao + grafo.aptidao[k]) < self.limSuperior:
                                        maiorArestaAtual = matrizIncidencia[j][k]
                                        vertice = k
                                        aresta = j
            # atualizamos os atributos do grupo atual, adicionado o vértice que ligava a maior aresta em questão ao grupo, caso tenhamos encontrado o vértice
            if vertice != -1:
                # colocamos True no vértice que está sendo inserido no grupo, o que significa que ele não pode participar de nenhum outro grupo
                grafo.inseridos[vertice] = True
                # somamos a aptidão do vértice que está sendo adicionado a 'somaAptidao'
                self.somaAptidao += grafo.aptidao[vertice]
                self.qtdArestas += self.qtdVertices
                for i in range(self.qtdVertices):
                    j = 0
                    contador = 0
                    # adicionamos ao grupo todas as arestas do vértice que está sendo inserido que têm ligação com os vértices já existentes no grupo
                    while j < grafo.qtdArestas and contador != self.qtdVertices:
                        if matrizIncidencia[j][self.vertices[i]] != 0 and matrizIncidencia[j][vertice] != 0:
                            # somamos à 'somaArestas' a aresta que está sendo adicionada ao grupo
                            self.somaArestas += matrizIncidencia[j][vertice]
                            aux = []
                            # vertice 1
                            aux.append(vertice)
                            # vertice 2
                            aux.append(self.vertices[i])
                            # valor da aresta 1 - 2
                            aux.append(matrizIncidencia[j][vertice])
                            self.arestas.append(aux)
                            contador += 0
                        j += 1
                self.qtdVertices += 1
                self.vertices.append(vertice)
            cont += 1

    # método que encontra os primeiros vértices do grafo que farão parte do grupo, tendo o 'limInferior' como limitante
    # algoritmo para a estrutura lista de adjacência
    def listAdLimInf(self, grafo, listaAdjacencia):
        # entramos no while se o somatório das aptidões dos vértices já pertencentes ao grupo for menor ou igual ao limite inferior
        while self.somaAptidao <= self.limInferior:
            maiorArestaAtual = 0
            vertice = -1
            # percorre os vértices do grupo atual
            for i in range(self.qtdVertices):
                # percorre todas as arestas do grafo ligadas ao vertices[i] do grupo
                for j in range(grafo.qtdVertices - 1):
                    # se o vertice não estiver em nenhum outro grupo, então verificamos se alguma de suas arestas é maior que a maiorArestaAtual 
                    if not(grafo.inseridos[listaAdjacencia[self.vertices[i]][j][0]]):
                        # caso seja maior, a verificação continua
                        if listaAdjacencia[self.vertices[i]][j][1] > maiorArestaAtual:
                            # verificamos se não ultrapassa o limite superior
                            if (self.somaAptidao + grafo.aptidao[j]) < self.limSuperior:
                                maiorArestaAtual = listaAdjacencia[self.vertices[i]][j][1];
                                vertice = listaAdjacencia[self.vertices[i]][j][0]
            # atualizamos os atributos do grupo atual, adicionado o vértice que ligava a maior aresta em questão ao grupo
            if vertice != -1:
                # colocamos True no vértice que está sendo inserido no grupo, o que significa que ele não pode participar de nenhum outro grupo
                grafo.inseridos[vertice] = True
                # somamos a aptidão do vértice que está sendo adicionado à 'somaAptidao'
                self.somaAptidao += grafo.aptidao[vertice]
                self.qtdArestas += self.qtdVertices
                # adicionamos ao grupo todas as arestas do vértice que está sendo inserido que têm ligação com os vértices já existentes no grupo
                for i in range(self.qtdVertices):
                    for j in range(grafo.qtdVertices - 1):
                        if listaAdjacencia[self.vertices[i]][j][0] == vertice:
                            # somamos à 'somaArestas' a aresta que está sendo adicionada ao grupo
                            self.somaArestas += listaAdjacencia[self.vertices[i]][j][1]
                            aux = []
                            # vertice 1
                            aux.append(vertice)
                            # vertice 2
                            aux.append(self.vertices[i])
                            # valor da aresta 1 - 2
                            aux.append(listaAdjacencia[self.vertices[i]][j][1])
                            self.arestas.append(aux)
                self.qtdVertices += 1
                self.vertices.append(vertice)

    # método que armazena os vértices que não foram inseridos em 'listAdLimInf', tendo o 'limSuperior' como limitante
    # algoritmo para a estrutura lista de adjacência
    def listAdLimSup(self, grafo, listaAdjacencia):
        cont = 0
        # entramos no while se o somatório das aptidões dos vértices já pertencentes ao grupo for menor ou igual ao limite superior
        while self.somaAptidao <= self.limSuperior and cont != grafo.qtdVertices:
            maiorArestaAtual = 0
            vertice = -1
            # percorre os vértices do grupo atual
            for i in range(self.qtdVertices):
                # percorre todas as arestas do grafo ligadas ao vertices[i] do grupo
                for j in range(grafo.qtdVertices - 1):
                    # se o vertice não estiver em nenhum outro grupo, então verificamos se alguma de suas arestas é maior que a maiorArestaAtual 
                    if not grafo.inseridos[listaAdjacencia[self.vertices[i]][j][0]]:
                        # caso seja maior, a verificação continua
                        if listaAdjacencia[self.vertices[i]][j][1] > maiorArestaAtual:
                            # se for maior, verificamos se não ultrapassa o limite superior
                            if (self.somaAptidao + grafo.aptidao[j]) < self.limSuperior:
                                maiorArestaAtual = listaAdjacencia[self.vertices[i]][j][1];
                                vertice = listaAdjacencia[self.vertices[i]][j][0]
            # atualizamos os atributos do grupo atual, adicionado o vértice que ligava a maior aresta em questão ao grupo
            if vertice != -1:
                # colocamos True no vértice que está sendo inserido no grupo, o que significa que ele não pode participar de nenhum outro grupo
                grafo.inseridos[vertice] = True
                # somamos a aptidão do vértice que está sendo adicionado à 'somaAptidao'
                self.somaAptidao += grafo.aptidao[vertice]
                self.qtdArestas += self.qtdVertices
                # adicionamos ao grupo todas as arestas do vértice que está sendo inserido que têm ligação com os vértices já existentes no grupo
                for i in range(self.qtdVertices):
                    for j in range(grafo.qtdVertices - 1):
                        if listaAdjacencia[self.vertices[i]][j][0] == vertice:
                            # somamos à 'somaArestas' a aresta que está sendo adicionada ao grupo
                            self.somaArestas += listaAdjacencia[self.vertices[i]][j][1]
                            aux = []
                            # vertice 1
                            aux.append(vertice)
                            # vertice 2
                            aux.append(self.vertices[i])
                            # valor da aresta 1 - 2
                            aux.append(listaAdjacencia[self.vertices[i]][j][1])
                            self.arestas.append(aux)
                self.qtdVertices += 1
                self.vertices.append(vertice)
            cont += 1
