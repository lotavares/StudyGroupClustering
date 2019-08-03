### Montagem de grupos de estudo

A implementação consistiu no desenvolvimento de uma forma de solucionar um problema de montagem de grupos de estudo. Nesse sentido, cada estudante *u* possui uma nota *pu* , que indica o grau de aptidão para a resolução do problema proposto. O total de grupos de estudantes a ser formado é igual a *g*. Os grupos possuem limites mínimos e máximos de aptidão dados por *L* e *U* , respectivamente. Cada estudante deve pertencer a apenas um grupo. A relação entre cada par de estudantes *u* e *v* é dado pelo valor *duv ∈ R*, que quantifica as diferenças das características entre os dois estudantes relativas à resolução do problema proposto. Nosso objetivo foi criar *g* grupos de estudantes que maximizasse o somatório das diferenças entre os estudantes escolhidos a pertencer a cada grupo.

#### Entrada e Execução

O programa recebe como entrada um arquivo texto. Os arquivos disponíveis para teste estão na pasta *arquivos_teste*, onde em *readme.txt* estão as especificações das instâncias de teste.

Foi utilizado o python 3 para a implementação.

Para executar, basta rodar o comando `python3 main.py` no terminal e entrar com o nome do arquivo de teste. Após, basta escolher entre as opções apresentadas para resolver o problema, as opções são:

	* executar o programa utilizando matriz de adjacência
	* executar o programa utilizando matriz de incidência
	* executar o programa utilizando lista de adjacência

#### Resultados

Os resultados são impressos ao final da execução na seguinte ordem:

	* quantidade de vértices pertencentes a algum grupo (total de vértices do grafo)
	* somatório total das arestas de todos os grupos
	* tempo de execução do programa em segundos

As informações individuais dos grupos podem ser impressas no terminal após a execução no seguinte formato:

	* índice do grupo
	* somatório das aptidões
	* somatório das arestas
	* somatório da quantidade de vértices
	* quantidade de arestas
	* vértices
	* arestas

Copyright (c) 2018 Felipe Ferreira Carvalho Silva, Lorena Kerollen Botelho Tavares, Rodrigo Pinto Herculano
