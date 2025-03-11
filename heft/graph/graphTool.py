import sys
sys.path.append("C:/heft-master/heft/graph")

import networkx as nx
from random import randint
import networkx.generators.random_graphs as randg
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET

from lxml import etree

ns = {'n': 'http://pegasus.isi.edu/schema/DAX',
          'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
          }	

def random_dag(nodes, edges=0):
	"""Generate a random Directed Acyclic Graph (DAG) with a given number of nodes and edges."""
	G = nx.DiGraph()
	
	for i in range(nodes):
		weight=randint(10,50) #task computational volume (10^3 megacycles = gigacycles)		
		G.add_node(str(i),w=weight) #add wieght for node
	while edges > 0:
		a = randint(0,nodes-1)
		b=a
		while b==a:
			b = randint(0,nodes-1)
		G.add_edge(str(a),str(b))
		if nx.is_directed_acyclic_graph(G):
			edges -= 1
		else:
			# we closed a loop!
			G.remove_edge(str(a),str(b))
	return G

def drawGraph(G):
	plt.figure(figsize=(4, 4), dpi=150)
	
	#nx.draw_planar(
	nx.draw(
		G,
		arrowsize=8,
		with_labels=True,
		node_size=300,
		node_color="#ffff8f",
		linewidths=2.0,
		width=1.5,
		font_size=5,
	)
	plt.show()

def getEntrynodes(G):
	return [int(v) for v, d in G.in_degree() if d == 0]

def createGraph(task,edge):
	#dag=nx.DiGraph()
	#for i in range(task):
		#dag.add_node(i)
	
	#for i in range(edge):
		#v=u=0
		#while v==u:
			#v=randint(0, task)
			#u=randint(0, task)
		#if 
		#dag.add_edge(v, u)
	
	
	dag=randg.fast_gnp_random_graph(task, edge/(task*(task-1)), seed=None, directed=True)
		
	return dag
		
	#seed = 13648  # Seed random number generators for reproducibility
	#G = nx.random_k_out_graph(task, 1, 1,self_loops=False ,seed=seed)
	#while not nx.is_directed_acyclic_graph(G):
		#G = nx.random_k_out_graph(task, 2, 1,self_loops=False ,seed=seed)
	#return G

def cpm(G): #return Critical path of the graph	
	return nx.dag_longest_path(G)


def loadXmlGraph(path):		
	root= etree.parse(path)
	return root

def getDag(root):
	dag={}	
	#root= etree.parse(path)
	jobs=root.xpath('./n:job/@id',namespaces=ns)
	for i in jobs:
		dag[i]=[]
		
	childs=root.xpath('./n:child',namespaces=ns)
	for ch in childs:		
		#dag[ch.xpath('./@ref',namespaces=ns)[0]]=tuple(ch.xpath('./n:parent/@ref',namespaces=ns))
		for par in ch.xpath('./n:parent/@ref',namespaces=ns):
			temp=list(dag[par])
			temp.append(ch.xpath('./@ref',namespaces=ns)[0])
			dag[par]=temp
			
	for k,v in dag.items():
		dag[k]=tuple(v)			
	
	return dag
	
def getJobSize(root,jobId):
	size=root.xpath('./n:job[@id=\'{}\']/@runtime'.format(jobId),namespaces=ns)
	return float(size[0])

def getFiles(root,jobId,inout):
	files=root.xpath('./n:job[@id=\'{}\']/n:uses[@link=\'{}\']/@file'.format(jobId,inout),namespaces=ns)
	return files

def getSumFiles(root,jobId,outputFiles,inout):
	size=0
	for file in outputFiles:
		try:
			size+=int(root.xpath('./n:job[@id=\'{}\']/n:uses[@link=\'{}\' and @file=\'{}\']/@size'.format(jobId,inout,file),namespaces=ns)[0])
		except:
			pass
	return size

def reverse_dict(d):
	""" Reverses direction of dependence dict

	>>> d = {'a': (1, 2), 'b': (2, 3), 'c':()}
	>>> reverse_dict(d)
	{1: ('a',), 2: ('a', 'b'), 3: ('b',)}
	"""
	result = {}
	for key in d:
		for val in d[key]:
			result[val] = result.get(val, tuple()) + (key, )
	return result

#q=loadXmlGraph('C:/heft-master/heft/graph/Montage_25.xml')
#x=getJobSize(q,'ID00001')
#print(x)
