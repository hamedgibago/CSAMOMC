from core import *
import math

class cpop(heftCore):
	
	def __init__(self):
		pass	
	def schedule(self,succ, agents, compcost, commcost):
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
		
		#initilize priority queue
		#pq=[entryTask]
		#TODO: Check if correct. When multiple entry task, I added all of theme to pq for
		#bug no more task will be added in pq after finishing one entry at line 133
		#TODO: Care about CP and setCP for critical path in lines 54, 56
		pq=entryTaskMultiple
		
		orders = {agent: [] for agent in agents}
		jobson = dict()		
		
		tasksDone=[]
		
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
				self.allocate(ni, orders, jobson, prec, compcost, commcost,criticalPathProcessor)
			else:
				super().allocate(ni, orders, jobson, prec, compcost, commcost)
			
			
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
			

		return orders, jobson	
	
	def rankd(self,ni, agents, prec,  compcost, commcost):		
		rank = partial(self.rankd, compcost=compcost, commcost=commcost,
			           prec=prec, agents=agents)
		w = partial(self.wbar, compcost=compcost, agents=agents)
		c = partial(self.cbar, agents=agents, commcost=commcost)
	
		#Is entry task
		if ni not in prec:
			#print('Rank {} = {}'.format(ni ,w(ni)))
			return 0			
		else:
			#print('Rank {} = {}'.format(ni ,w(ni) + max(c(ni, nj) + rank(nj) for nj in succ[ni])))
			#print('ni={} nj={} rank(nj)={} w(ni)={} c(nj,ni)={}'.format())
			return max(rank(nj) + w(nj) +  c(nj,ni) for nj in prec[ni])
	
	
	#TODO: overloading for calling grandparent, from TC3POP
	#def allocate(self,ni, orders, jobson, prec, compcost, commcost):
		#super().allocat(ni, orders, jobson, prec, compcost, commcost)
	
	
	def allocate(self,job, orders, jobson, prec, compcost, commcost,agent):
		""" Allocate job to the machine with earliest finish time

		Operates in place
		"""
		st = partial(self.start_time, job, orders, jobson, prec, commcost, compcost)
		ft = lambda machine: st(machine) + compcost(job, machine)
		
		#just commented because in the case of CP task we have calculated agent before
		#agent = min(orders.keys(), key=ft)
		start = st(agent)
		end = ft(agent)

		orders[agent].append(Event(job, start, end))
		orders[agent] = sorted(orders[agent], key=lambda e: e.start)
		# Might be better to use a different data structure to keep each
		# agent's orders sorted at a lower cost.

		jobson[job] = agent	