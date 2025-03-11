from core import *
import cpop,util
import math
import numpy as np
from pymoo.problems.multi import *
from pymoo.vendor import hv as HV
import util


class tc3pop(cpop.cpop):
	def __init__(self):
		pass
	def __getrefpoint__(self,results):
		max_makespan=0
		max_cost=0		
		for r in results:
			if r[2]>max_makespan:
				max_makespan=r[2]

			if r[3]>max_cost:
				max_cost=r[3]
		return np.array([max_cost,max_makespan])	

	def __solWithMaxHV__(self,results,ref_point):
		maxhV=-1
		selectedSol=[]
		for res in results:
			#ind=HV.HyperVolume(ref_point)
			#hyper1= ind.compute(np.array([[res[3],res[2]]]))
			hyper=util.calc_hv(res[3],res[2],ref_point)
			print(res[2],res[3],hyper)
			if hyper>maxhV:
				maxhV=hyper
				selectedSol=res
		
		return selectedSol
		
	def schedule(self,succ, agents, compcost, commcost,graph):
		results=[]
		#ref_point=[]
		""" Schedule computation dag onto worker agents

		inputs:

		succ - DAG of tasks {a: (b, c)} where b, and c follow a
		agents - set of agents that can perform work
		compcost - function :: job, agent -> runtime
		commcost - function :: j1, j2, a1, a2 -> communication time
		"""
		rank = partial(self.ranku, agents=agents, succ=succ,
		               compcost=compcost, commcost=commcost)

		prec = reverse_dict(succ)
		#rankd
		rd = partial(self.rankd, agents=agents, prec=prec,
		             compcost=compcost, commcost=commcost)		

		entryTask=[i for i in succ if i not in prec][0]

		entryTaskMultiple=[i for i in succ if i not in prec]




		def rankcpop(ni):
			return rank(ni)+rd(ni)

		jobs = set(succ.keys()) | set(x for xx in succ.values() for x in xx)

		downwardranks=dict([(i,rd(i)) for i in jobs])

		#rounding
		#for k,v in downwardranks.items():
			#downwardranks[k]=round(v,6)


		mixedrank=dict([(i,rankcpop(i)) for i in jobs])

		#rounding
		#for k,v in mixedrank.items():
			#mixedrank[k]=round(v,6)

		#check if we have multiple entry tasks, then we set entryTask, a task which
		#has greater mixedRank value
		if len(entryTaskMultiple)>1:			
			selected={k:v for k,v in mixedrank.items() if k in entryTaskMultiple}
			t={k:v for k,v in selected.items() if v == max(selected.values())}			
			if len(t)==1:
				entryTask=list(t.keys())[0]
			else:
				raise 'Multiple same max items'

		jobs = sorted(jobs, key=rankcpop)

		reversedJobs=list(reversed(jobs))

		#TODO: If in other examples wrong results, should be studied more (in the main paper): 
		#(is the sum of the computation costs of the tasks on the path and intertask communication costs along path)
		#set length of critical path to priority of entry task
		#CP=[i for i in reversedJobs].index(1)+1
		CP=mixedrank[entryTask]		

		setCP={entryTask}

		nk=entryTask

		#exitTask=[i[0] for i in succ.items() if not i[1]][0]
		exitTaskList=[i[0] for i in succ.items() if not i[1]]
		
		#while nk != exitTask:
		while nk not in exitTaskList:
			nj=succ[nk]
			y=[i for i in nj if mixedrank[i]==CP]
			if y!=[]:
				setCP= setCP.union(y)
				nk=y[0]
			#select item with minimum difference
			else:
				nextItem=''
				minDiff=math.pow(10,9)
				for i in range(len(nj)):
					if abs(mixedrank[nj[i]]-mixedrank[nk]) < minDiff :
					#if abs(mixedrank[nj[i]]-mixedrank[nk]) < minDiff and (mixedrank[nj[i]]-mixedrank[nk])>0:
					#if mixedrank[nk]-mixedrank[nj[i]] < minDiff :
						#if mixedrank[nk]-mixedrank[nj[i]]<0:
							#raise Exception('fault')					
						minDiff=abs(mixedrank[nj[i]]-mixedrank[nk])
						nextItem=nj[i]
				#if minDiff==math.pow(10,9):

				setCP= setCP.union([nextItem])
				nk=nextItem


		#sorting setCP. I don't think it may cause any problem
		setCP=sorted(setCP)

		minPcp=1e+9

		criticalPathProcessor=''

		for ag in list(agents):
			temp=0
			temp=temp + sum([compcost(i,ag) for i in setCP])
			if temp<minPcp:
				minPcp=temp
				criticalPathProcessor=ag
								
		
		for ag in list(agents):
			tasksDone=[]
		
			orders = {agent: [] for agent in agents}
			jobson = dict()				
			
			#initilize priority queue
			#pq=[entryTask]
			#TODO: Check if correct. When multiple entry task, I added all of theme to pq for
			#bug no more task will be added in pq after finishing one entry at line 133
			#TODO: Care about CP and setCP for critical path in lines 54, 56
			pq=entryTaskMultiple.copy()
			
			while pq!= [] :
				#t=[mixedrank[i] for i in [4,5,6,7]]
				#z=[mixedrank[p] for p in pq]
				highValue=1e-8
				#Remember, Task names should start from 1 and continue upward
				ni=-1
				for t in pq:
					if mixedrank[t]>highValue:
						highValue=mixedrank[t]
						ni=t
	
				if ni in setCP:
					#self.allocate(ni, orders, jobson, prec, compcost, commcost,criticalPathProcessor)
					self.allocate(ni, orders, jobson, prec, compcost, commcost,ag)
				else:
					heftCore().allocate(ni, orders, jobson, prec, compcost, commcost)
	
	
				def checkPrecsNotInPq(prec,pq):
					for i in prec:
						if i in pq:
							return True
					return False			
	
				def checkIfReady(prec,pq):
					for i in prec:
						if i not in pq: 
							pass
						else:
							return False
					return True
	
	
				#update priority queue if they become ready tasks
				pq.remove(ni)
				tasksDone.append(ni)
				for s in succ[ni]:
					#if not checkPrecsNotInPq(prec[s],pq) and s not in pq:
					#check if s is ready task (all prec tasks s are done), then add it to priority queue
					if set(prec[s]).issubset(tasksDone):
						pq.append(s)		
				#pq=succ[ni]
				
				
			(makespan,qos,energy,cost)=util.calculateResults(orders, jobson,graph)					
			print(makespan,cost)
			
			results.append([orders.copy(),jobson,makespan,cost])
			
		
		ref_point=self.__getrefpoint__(results)
		
		bestSol= self.__solWithMaxHV__(results,ref_point)
		
		#return orders, jobson
		return bestSol[0], bestSol[1]
	
	