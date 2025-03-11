import csv, json, random
import machine as machine
import vm as vm
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def readData(datatype):    
	with open(datatype.lower()+'.csv', newline='') as f:
		reader = csv.reader(f)
		data = list(reader)
	return data


def writeData(datatype,row): 
	# open the file in the write mode
	with open(datatype.lower()+'.csv', 'a', newline='') as f:        
		writer = csv.writer(f)    
		# write a row to the csv file
		writer.writerows(row)

def saveMachines(M,caseNum):
	machineList=[]
	for m in M:
		machineList.append([m.epsilon,m.Bu,m.Cen,m.fr])
	
	writeData('case'+str(caseNum)+'machines',machineList)

def saveGraph(G,caseNum):
	graphData= nx.write_gexf(G,'case'+str(caseNum)+'graphs.xml')
	#with open('Case'+str(caseNum)+'graphs.json', 'w') as f:
		#json.dump(graphData, f)

def loadGraph(caseNum):
	#with open('Case'+str(caseNum)+'graphs.json') as f:
		#graphData = nx.read_gexf(f)	
	return nx.read_gexf('case'+str(caseNum)+'graphs.xml')

def loadMachines(caseNum):
	machineList=[]
	rows=readData(caseNum)
	i=0
	for r in rows:
		machineList.append(machine.machine(i,int(r[0]),int(r[1]),r[2],int(r[3])))
		i+=1
	return machineList

def createVmTypes(vmKinds,vmvCpu,vmMemory):	
	vmTypes=[]
	for i in range(vmKinds):
		vmTypes.append(vm.vm(random.choice(vmvCpu),random.randint(*vmMemory)))
		
	return vmTypes

def plotFromPreviousData(path):
		data=readData(path)		
		#func = [i for i in data]		
		function1 = [float(i[0]) for i in data]
		function2 = [float(i[1]) for i in data]
		function3 = [float(i[2]) for i in data]	
		
		fig = plt.figure()
		ax = fig.add_subplot(projection='3d')
		ax.set_xlabel('makespan', fontsize=15)
		ax.set_ylabel('load unbalance', fontsize=15)
		ax.set_zlabel('energy', fontsize=15)
		#plt.scatter(function1, function2,function3)
		
		ax.scatter(function1, function2, function3, cmap='Greens');
		
		#for i in range(len(function1)):
			#ax.scatter(function1[i], function2[i], function3[i], cmap='Greens');
		
		plt.show()

#plotFromPreviousData('tasks10,cloudhosts6,edgehosts3,ccr1,generations50,individuals10,crossover_param6,mutation_param5')

