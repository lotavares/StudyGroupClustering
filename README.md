### Study Group Clustering

The implementation consisted of developing a method to solve a study group clustering problem. In this context, each student *u* has a score *pu*, which indicates their aptitude level for solving the proposed problem. The total number of student groups to be formed is *g*. The groups have minimum and maximum aptitude limits given by *L* and *U*, respectively. Each student must belong to only one group. The relationship between each pair of students *u* and *v* is given by the value *duv ∈ R*, which quantifies the differences in characteristics between the two students relative to solving the proposed problem. Our goal was to create *g* student groups that maximize the sum of differences among the students chosen to belong to each group.

#### Input and Execution

The program receives a text file as input. The files available for testing are in the *arquivos_teste* folder, where the specifications of the test instances are in *readme.txt*.

Python 3 was used for the implementation.

To run, simply execute the command `python3 main.py` in the terminal and enter the name of the test file. Then, choose one of the options presented to solve the problem. The options are:

	* run the program using an adjacency matrix
	* run the program using an incidence matrix
	* run the program using an adjacency list

#### Results

The results are printed at the end of execution in the following order:

	* number of vertices belonging to any group (total vertices in the graph)
	* total sum of the edges of all groups
	* program execution time in seconds

The individual information of the groups can be printed in the terminal after execution in the following format:

	* group index
	* sum of aptitudes
	* sum of edges
	* sum of the number of vertices
	* number of edges
	* vertices
	* edges

Copyright (c) 2018 Felipe Ferreira Carvalho Silva, Lorena Kerollen Botelho Tavares, Rodrigo Pinto Herculano
