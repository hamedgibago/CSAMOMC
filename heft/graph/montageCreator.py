import math
import networkx as nx
import graphTool
from random import randint
import batUtil as utl

case=100

layers={1:[1],
        2:[2,3,4,5],
        3:[6,7,8],
        4:[9]}

numTasks=100
#27
#40
#1
#1
#27
#1
#1
#1
#1

createGraph=True
drawGraph=True

numOfTasks=20

G = nx.DiGraph()

w={}
dag={}

for i in range(1,20):
	if i<=4:
		dag[i]=randint(5,10)
		G.add_edge(i, randint(5,10))
		dag[i]= randint(5,10)
		G.add_edge(i,randint(25,40))
		dag[i]= i+13 #one for attaching to layer 5
		G.add_edge(i,i+13)
	elif i>4 and i <=10:
		dag[i]= 11
		G.add_edge(i,11)
	elif i==11:
		dag[i]= 12
		G.add_edge(i,70)
	elif i==12:
		for j in range(4):
			dag[i]=j
			G.add_edge(i,j)
	elif i>=13 and i<=16:
		dag[i]= 17
		G.add_edge(i,17)
	elif i in (17,18,19,20) :
		dag[i]= i+1
		G.add_edge(i,i+1)

print('x')

#for i in range(1,100):
	#if i<=27:
		#dag[i]= randint(28,35)
		#G.add_edge(i, randint(28,35))
		#dag[i]= randint(25,40)
		#G.add_edge(i,randint(25,40))
		#dag[i]= i+70 #one for attaching to layer 5
		#G.add_edge(i,i+70)
	#elif i>27 and i <=68:
		#dag[i]= 69
		#G.add_edge(i,79)
	#elif i==69:
		#dag[i]= 70
		#G.add_edge(i,70)
	#elif i>=70 and i<=96:
		#dag[i]= 97
		#G.add_edge(i,97)
	#elif i in (97,98,99,100) :
		#dag[i]= i+1
		#G.add_edge(i,i+1)
		
		
#if createGraph:
	##maxmum number of edges in DAG is n*(n-1)/2 : we use a random value between this
	##minumum number of edges we consider n-1
	##https://stackoverflow.com/questions/11699095/how-many-edges-can-there-be-in-a-dag
	#G=graphTool.random_dag(numOfTasks,edges=randint(numOfTasks-1, numOfTasks*(numOfTasks-1)/2))

	#CP=graphTool.cpm(G)
	#utl.saveGraph(G, case)
#else:
	#G=utl.loadGraph(case)
	#CP=graphTool.cpm(G)

if drawGraph:
	graphTool.drawGraph(G)

def CreateTaskSizes():
	for i in range(1,100):
		w[i]=randint(1000,1000000)

#def CreateEdgeSizes():