import sys,math,os
sys.path.append("C:/heft-master/heft")

import EHeftR
import cpop,TC3PoP
from graph import heftGraph,qlheftGraph,heftDGraph,scienceGraph,graphTool
from core import *
import util
import CSA
import csaScheduler
import numpy as np
import matplotlib.pyplot as plt



def printResults(makespan,qos,energy,cost):
	print(jobson)
	print('makespan= {} secs - {} minutes'.format(str(makespan) ,str(makespan/60)))			
	print('Qos= '+str(qos))	
	print('Energy= '+ str(energy))	
	print('Cost= '+ str(cost))
	print('##########################################################################')	



heft= heftCore()

Rheft= EHeftR.EHeftR()
cpop = cpop.cpop()
tc3pop=TC3PoP.tc3pop()



cpopRes=[]
tc3popRes=[]
CsaRes=[]

machines='abcde'

graphName='CyberShake'
taskLength=[100,200,300,400,500]
#taskLength=[100,200]
#taskLength=[25,50]
#taskLength=[500]


population_size=40
ap=0.06
fL=0.08
iterations=300

#orders, jobson = heft.schedule(heftGraph.dag, 'abc', heftGraph.compcost,heftGraph.commcost)
#orders, jobson = heft.schedule(qlheftGraph.dag, 'abc', qlheftGraph.compcost,qlheftGraph.commcost)
#orders, jobson = Rheft.schedule(qlheftGraph.dag, 'abc', qlheftGraph.compcost,qlheftGraph.commcost,qlheftGraph.encost)
#orders, jobson = heft.schedule(heftDGraph.dag, 'abc', heftDGraph.compcost,heftDGraph.commcost)

# ** for cost test
#TODO: in these two methods, compconst and commcost are static, but whit montageGraph, 
#commcost and compcost in each call return random values, so when calling two montageGraph
#at the same type for two diffrent algorithms, random values should be saved for the second
#and after that time, or results should not be random

#orders, jobson = cpop.schedule(heftGraph.dag, 'abc', heftGraph.compcost,heftGraph.commcost)
#(makespan,qos,energy,cost)=util.calculateResults(orders,jobson)
#printResults(makespan,qos,energy,cost)

#orders, jobson = tc3pop.schedule(heftGraph.dag, 'abc', heftGraph.compcost,heftGraph.commcost)
#print("===================================================")
#(makespan,qos,energy,cost)=util.calculateResults(orders,jobson)
#print('makespan={}\nqos={}\nenergy={}\ncost={} '.format(makespan,qos,energy,cost))
#printResults(makespan,qos,energy,cost)

gr=None

for leng in taskLength:
	gr=scienceGraph.scienceGraph(size=leng,name=graphName)
	#graphTool.drawGraph(gr)
	#gr=qlheftGraph.qlHeftGraph()
	l=len(gr.dag.keys())



	orders, jobson = cpop.schedule(gr.dag, machines, gr.compcost,gr.commcost)
	(makespan,qos,energy,cost)=util.calculateResults(orders,jobson,gr)
	cpopRes.append((makespan,qos,energy,cost))
	printResults(makespan,qos,energy,cost)

	#save results to csv file
	#util.writeData("-".join(map(str, taskLength)),cpopRes)	
	util.writeData('ResultsCsv/cpop-'+str(leng),cpopRes)

	print("***************************************************")

	#For tc3pop we pass gr because we need calculate results multiple times in it
	orders, jobson = tc3pop.schedule(gr.dag, machines, gr.compcost,gr.commcost,gr)
	(makespan,qos,energy,cost)=util.calculateResults(orders,jobson,gr)
	tc3popRes.append((makespan,qos,energy,cost))
	print('makespan={}\nqos={}\nenergy={}\ncost={} '.format(makespan,qos,energy,cost))
	printResults(makespan,qos,energy,cost)
	util.writeData('ResultsCsv/tc3cpop-'+str(leng),cpopRes)

	print("***************************************************")

	ones=np.ones(l, dtype=np.uint, order='C')


	#minvalues = minimum index of vm (a=1)
	#maxvalues = maximum index of vm (e=5)
	#remember: for number of vms or machines, we should create them dynamically

	csa_sch=csaScheduler.csa_scheduler(gr.dag, machines, gr.compcost,gr.commcost,gr)
	#commented for selecting wrong values of multiple jobson in target function
	CSA.crow_search_algorithm(population_size=population_size,ap=ap,fL=fL,
	                          min_values=ones,
	                                    max_values=[i*(len(machines)+1) for i in ones],
	                                    iterations=iterations,target_function=csa_sch.schedule_function,verbose=True)

	#CSA.crow_search_algorithm(population_size=5,ap=0.02,fL=0.02,
		#min_values=[1,1],
		#max_values=[3,3],
		#iterations=100,target_function=csa_sch.schedule_function,verbose=True)

	jobson=csa_sch.jobson
	orders=csa_sch.orders
	for eachP in sorted(orders):
		print(eachP,orders[eachP])
	printResults(csa_sch.makespan,csa_sch.qos,csa_sch.energy,csa_sch.cost)
	CsaRes.append((csa_sch.makespan,csa_sch.cost,csa_sch.makespan))
	util.writeData('ResultsCsv/Csa-'+str(leng),CsaRes)

	util.writeData('ResultsCsv/Csa-'+str(leng)+'All-Makespan-and-cost',csa_sch.data)






#fig, ax = plt.subplots()
fig, ax = plt.subplots(1,2,figsize=(15,7))
fig.suptitle(gr.name)


#line graph
#ax.plot(taskLength,CsaRes,label='CSA',marker='o')
#ax.plot(taskLength,[i[0] for i in cpopRes],label='Cpop',marker='*')
#ax.plot(taskLength,[i[0] for i in tc3popRes],label='TC3pop',marker='x')


x= np.arange(100,505,100)  # the label locations
#for range 100-200
#x= np.arange(100,205,100)  # the label locations
width = 10# the width of the bars
#bar graph
ax[0].bar(x-2*width,[i[0] for i in CsaRes],width+10,label='CSAMOMC',edgecolor='black')
ax[0].bar(x,[i[0] for i in cpopRes],width+10,label='Cpop',edgecolor='black')
ax[0].bar(x +2*width,[i[0] for i in tc3popRes],width+10,label='TC3pop',edgecolor='black')

ax[0].set(xlabel='Number of Tasks',ylabel='Makespan(second)')

ax[0].grid()
ax[0].legend()


#cost
ax[1].bar(x-2*width,[i[1] for i in CsaRes],width+10,label='CSAMOMC',edgecolor='black')
ax[1].bar(x,[i[3] for i in cpopRes],width+10,label='Cpop',edgecolor='black')
ax[1].bar(x +2*width,[i[3] for i in tc3popRes],width+10,label='TC3pop',edgecolor='black')

ax[1].set(xlabel='Number of Tasks',ylabel='Cost($)')

plt.grid()
plt.legend()



plt.savefig(os.getcwd()+'\\figs\\{}-population_Size={},ap={},fL={},iterations={}.eps'.format(graphName,population_size,ap,fL,iterations), bbox_inches='tight')
plt.show()