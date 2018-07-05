# -*- coding: utf-8 -*-

class Grupo:
    def __init__(self, limInferior, limSuperior, arestas):
        self.limInferior = limInferior
        self.limSuperior = limSuperior
        self.somaAptidao = 0
        self.somaArestas = 0
        self.qtdVertices = 2
        self.qtdArestas = 1
        self.arestas = [1]
        self.arestas[0] = arestas
        self.vertices = []
        self.vertices.append(arestas[0])
        self.vertices.append(arestas[1])
        self.listaArestasOrd = []
    
    def quickSortAux(self, vetor, esquerda, direita):
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
            self.quickSortAux(vetor, esquerda, j)
        if i < direita:
            self.quickSortAux(vetor, i, direita)

    def quickSort(self, vetor, tam):
        self.quickSortAux(vetor, 0, tam - 1)

    def listaArestasDoVertice(self, grafo):
        listaAux = []
        for j in range(grafo.qtdArestas):
            if self.vertices[-1] == grafo.arestas[j][0] or self.vertices[-1] == grafo.arestas[j][1]:
                listaAux.append(grafo.arestas[j])
        
        self.quickSort(listaAux, len(listaAux))
        self.listaArestasOrd.append(listaAux)

    def matrizAd(self):
        print(self.arestas)
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
        
    def imprimeMatrizAdjacenci(self, matriz):
        print("\nMatriz de Adjacencia: \n")
        for lin in range(len(matriz)):
            print(matriz[lin])
    
    def matAdLimInf(self, grafo, matrizAdjacencia):
        while self.somaAptidao <= self.limInferior:
            maiorArestaAtual = 0
            vertice = -1
            # percorre os vértices do grupo atual
            for i in range(self.qtdVertices):
                # percorre todas as arestas do grafo ligadas a algum vertice do grupo
                for j in range(grafo.qtdVertices):
                    # se o vertice não estiver em nenhum outro grupo, então verificamos se alguma de suas arestas é maior que a maiorArestaAtual 
                    if not grafo.inseridos[j]:
                        if matrizAdjacencia[self.vertices[i]][j] > maiorArestaAtual:
                            # se for maior, verificamos se não ultrapassa o limite superior
                            if (self.somaAptidao + grafo.aptidao[j]) < self.limSuperior:
                                maiorArestaAtual = matrizAdjacencia[self.vertices[i]][j];
                                vertice = j
            # atualizamos os atributos do grupo atual, adicionado o vértice que ligava a maior aresta em questão ao grupo
            if vertice != -1:
                grafo.inseridos[vertice] = True
                self.somaAptidao += grafo.aptidao[vertice]
                self.qtdArestas += self.qtdVertices
                for i in range(self.qtdVertices):
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
                self.quickSort(grafo.arestas)

        print(self.somaAptidao)
        print(self.somaArestas)
        print(self.qtdVertices)
        print(self.qtdArestas)
        print(self.vertices)

    def matAdLimSup(self, grafo, matrizAdjacencia):
        cont = 0
        while self.somaAptidao <= self.limSuperior and cont != grafo.qtdVertices:
            maiorArestaAtual = 0
            vertice = -1
            # percorre os vértices do grupo atual
            for i in range(self.qtdVertices):
                # percorre todas as arestas do grafo ligadas a algum vertice do grupo
                for j in range(grafo.qtdVertices):
                    # se o vertice não tiver em nenhum outro grupo, então fazemos isso
                    if not grafo.inseridos[j]:
                        if matrizAdjacencia[self.vertices[i]][j] > maiorArestaAtual:
                            if (self.somaAptidao + grafo.aptidao[j]) < self.limSuperior:
                                maiorArestaAtual = matrizAdjacencia[self.vertices[i]][j];
                                vertice = j
            if vertice != -1:
                grafo.inseridos[vertice] = True
                self.somaAptidao += grafo.aptidao[vertice]
                self.qtdArestas += self.qtdVertices
                for i in range(self.qtdVertices):
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

        print(self.somaAptidao)
        print(self.somaArestas)
        print(self.qtdVertices)
        print(self.qtdArestas)
        print(self.vertices)
    
    def matIncLimInf(self, grafo, matrizIncidencia):
        cont = 0
        while self.somaAptidao <= self.limInferior and cont != grafo.qtdVertices:
            maiorArestaAtual = 0
            vertice = -1
            aresta = 0
            # percorre os vértices do grupo atual
            for i in range(self.qtdVertices):
                #~ print "CHEGUEEEI"
                # percorre todas as arestas do grafo ligadas a algum vertice do grupo
                for j in range(grafo.qtdArestas):
                    # se o vertice não estiver em nenhum outro grupo, então verificamos se alguma de suas arestas é maior que a maiorArestaAtual 
                        if matrizIncidencia[j][self.vertices[i]] != 0:
                            for k in range(grafo.qtdVertices):
                                if matrizIncidencia[j][k] != 0 and k != self.vertices[i] and not grafo.inseridos[k]:
                                    if matrizIncidencia[j][k] > maiorArestaAtual:
                                        # se for maior, verificamos se não ultrapassa o limite superior
                                        if (self.somaAptidao + grafo.aptidao[k]) < self.limSuperior:
                                            maiorArestaAtual = matrizIncidencia[j][k]
                                            vertice = k
                                            aresta = j
            # atualizamos os atributos do grupo atual, adicionado o vértice que ligava a maior aresta em questão ao grupo
            if vertice != -1:
                #~ print "MANOOO DO CEEEU"
                grafo.inseridos[vertice] = True
                self.somaAptidao += grafo.aptidao[vertice]
                self.qtdArestas += self.qtdVertices
                for i in range(self.qtdVertices):
                    j = 0
                    contador = 0
                    while j < grafo.qtdArestas and contador != self.qtdVertices:
                        if matrizIncidencia[j][self.vertices[i]] != 0 and matrizIncidencia[j][vertice] != 0:
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
                            del(matrizIncidencia[j])
                            grafo.qtdArestas -= 1
                        j += 1
                self.qtdVertices += 1
                self.vertices.append(vertice)
            cont += 1

        for i in range(self.qtdVertices):
            j = 0
            while j < grafo.qtdArestas:
                if matrizIncidencia[j][i] != 0:
                    del(matrizIncidencia[j])
                    grafo.qtdArestas -= 1
                j += 1
    
    def matIncLimSup(self, grafo, matrizIncidencia):
        cont = 0
        while self.somaAptidao <= self.limSuperior and cont != grafo.qtdVertices:
            maiorArestaAtual = 0
            vertice = -1
            aresta = 0
            # percorre os vértices do grupo atual
            for i in range(self.qtdVertices):
                #~ print "CHEGUEEEI"
                # percorre todas as arestas do grafo ligadas a algum vertice do grupo
                for j in range(grafo.qtdArestas):
                    # se o vertice não estiver em nenhum outro grupo, então verificamos se alguma de suas arestas é maior que a maiorArestaAtual 
                        if matrizIncidencia[j][self.vertices[i]] != 0:
                            for k in range(grafo.qtdVertices):
                                if matrizIncidencia[j][k] != 0 and k != self.vertices[i] and not grafo.inseridos[k]:
                                    if matrizIncidencia[j][k] > maiorArestaAtual:
                                        # se for maior, verificamos se não ultrapassa o limite superior
                                        if (self.somaAptidao + grafo.aptidao[k]) < self.limSuperior:
                                            maiorArestaAtual = matrizIncidencia[j][k]
                                            vertice = k
                                            aresta = j
            # atualizamos os atributos do grupo atual, adicionado o vértice que ligava a maior aresta em questão ao grupo
            if vertice != -1:
                #~ print "MANOOO DO CEEEU"
                grafo.inseridos[vertice] = True
                self.somaAptidao += grafo.aptidao[vertice]
                self.qtdArestas += self.qtdVertices
                for i in range(self.qtdVertices):
                    j = 0
                    contador = 0
                    while j < grafo.qtdArestas and contador != self.qtdVertices:
                        if matrizIncidencia[j][self.vertices[i]] != 0 and matrizIncidencia[j][vertice] != 0:
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
                            del(matrizIncidencia[j])
                            grafo.qtdArestas -= 1
                        j += 1
                self.qtdVertices += 1
                self.vertices.append(vertice)
            cont += 1
        
        for i in range(self.qtdVertices):
            j = 0
            while j < grafo.qtdArestas:
                if matrizIncidencia[j][i] != 0:
                    del(matrizIncidencia[j])
                    grafo.qtdArestas -= 1
                j += 1
        
        print(self.somaAptidao)
        print(self.somaArestas)
        print(self.qtdVertices)
        print(self.qtdArestas)
        print(self.vertices)
        
    def listAdLimInf(self, grafo, listaAdjacencia):   
        while self.somaAptidao <= self.limInferior:
            maiorArestaAtual = 0
            vertice = -1
            # percorre os vértices do grupo atual
            for i in range(self.qtdVertices):
                # percorre todas as arestas do grafo ligadas a algum vertice do grupo
                for j in range(grafo.qtdVertices - 1):
                    # se o vertice não estiver em nenhum outro grupo, então verificamos se alguma de suas arestas é maior que a maiorArestaAtual 
                    if not grafo.inseridos[listaAdjacencia[self.vertices[i]][j][0]]:
                        if listaAdjacencia[self.vertices[i]][j][1] > maiorArestaAtual:
                            # se for maior, verificamos se não ultrapassa o limite superior
                            if (self.somaAptidao + grafo.aptidao[j]) < self.limSuperior:
                                maiorArestaAtual = listaAdjacencia[self.vertices[i]][j][1];
                                vertice = listaAdjacencia[self.vertices[i]][j][0]
            # atualizamos os atributos do grupo atual, adicionado o vértice que ligava a maior aresta em questão ao grupo
            if vertice != -1:
                grafo.inseridos[vertice] = True
                self.somaAptidao += grafo.aptidao[vertice]
                self.qtdArestas += self.qtdVertices
                for i in range(self.qtdVertices):
                    for j in range(grafo.qtdVertices - 1):
                        if listaAdjacencia[self.vertices[i]][j][0] == vertice:
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
       
        print(self.somaAptidao)
        print(self.somaArestas)
        print(self.qtdVertices)
        print(self.qtdArestas)
        print(self.vertices)
                
    def listAdLimSup(self, grafo, listaAdjacencia):
        cont = 0
        while self.somaAptidao <= self.limSuperior and cont != grafo.qtdVertices:
            maiorArestaAtual = 0
            vertice = -1
            # percorre os vértices do grupo atual
            for i in range(self.qtdVertices):
                # percorre todas as arestas do grafo ligadas a algum vertice do grupo
                for j in range(grafo.qtdVertices - 1):
                    # se o vertice não estiver em nenhum outro grupo, então verificamos se alguma de suas arestas é maior que a maiorArestaAtual 
                    if not grafo.inseridos[listaAdjacencia[self.vertices[i]][j][0]]:
                        if listaAdjacencia[self.vertices[i]][j][1] > maiorArestaAtual:
                            # se for maior, verificamos se não ultrapassa o limite superior
                            if (self.somaAptidao + grafo.aptidao[j]) < self.limSuperior:
                                maiorArestaAtual = listaAdjacencia[self.vertices[i]][j][1];
                                vertice = listaAdjacencia[self.vertices[i]][j][0]
            # atualizamos os atributos do grupo atual, adicionado o vértice que ligava a maior aresta em questão ao grupo
            if vertice != -1:
                grafo.inseridos[vertice] = True
                self.somaAptidao += grafo.aptidao[vertice]
                self.qtdArestas += self.qtdVertices
                for i in range(self.qtdVertices):
                    for j in range(grafo.qtdVertices - 1):
                        if listaAdjacencia[self.vertices[i]][j][0] == vertice:
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
        
        print(self.somaAptidao)
        print(self.somaArestas)
        print(self.qtdVertices)
        print(self.qtdArestas)
        print(self.vertices)
