from core import *
from graph import qlheftGraph
class EHeftR(heftCore):
	def __init__(self):
		self.alpha=5.2
		self.beta=100
		self.gamma=6.3
	def schedule(self,succ, agents, compcost, commcost,encost):
		""" Schedule computation dag onto worker agents

		inputs:

		succ - DAG of tasks {a: (b, c)} where b, and c follow a
		agents - set of agents that can perform work
		compcost - function :: job, agent -> runtime
		commcost - function :: j1, j2, a1, a2 -> communication time
		"""
		rank = partial(self.ranku, agents=agents, succ=succ,
		               compcost=compcost, commcost=commcost,encost=encost)
		prec = reverse_dict(succ)

		jobs = set(succ.keys()) | set(x for xx in succ.values() for x in xx)
		jobs = sorted(jobs, key=rank)

		orders = {agent: [] for agent in agents}
		jobson = dict()
		jobReversed=reversed(jobs)
		for job in jobReversed:
			#SPT-EFT-R should be implemented here		
			#if len(orders)>0:
				#t=[x for x in ev for ev in orders.values() if ev!=[]]
			
			self.allocate(job, orders, jobson, prec, compcost, commcost)
			
			#t=[x for x in orders.values() if x!=[]]
			#if t==[]:
				#self.allocate(job, orders, jobson, prec, compcost, commcost)
			#elif job not in [y.job for y in t[0]]:
				#self.allocate(job, orders, jobson, prec, compcost, commcost)
		
		
		return orders, jobson
		
	
	def ranku(self,ni, agents, succ,  compcost, commcost,encost):		
		rank = partial(self.ranku, compcost=compcost, commcost=commcost,
		               succ=succ, agents=agents,encost=encost)
		w = partial(self.wbar, compcost=compcost, agents=agents)
		c = partial(self.cbar, agents=agents, commcost=commcost)

		if ni in succ and succ[ni]:
			return self.alpha * w(ni) + self.beta * max(c(ni, nj) + rank(nj) for nj in succ[ni]) + self.gamma * encost(ni,1)
		else:
			return w(ni)	
		
	def allocate(self,job, orders, jobson, prec, compcost, commcost):
		""" Allocate job to the machine with earliest finish time

		Operates in place
		"""		
		st = partial(self.start_time, job, orders, jobson, prec, commcost, compcost)
		ft = lambda machine: st(machine) + compcost(job, machine)

		agent = min(orders.keys(), key=ft)
		start = st(agent)
		end = ft(agent)
		
		reschedule=False

		if len(jobson)>1:
			for i in range(len(jobson)):        
				if i+1 in prec.keys() and i+2 in prec.keys() and i+1 in jobson and i+2 in jobson:
					#check if the are in same layer and same machine
					#if prec[i+1]==prec[i+2] and jobson[i+1]==jobson[i+2]:
					if qlheftGraph.getLayer(i+1)==qlheftGraph.getLayer(i+2) and jobson[i+1]==jobson[i+2]:
						jb1=i+1
						jb2=i+2
						machin=jobson[i+1]

						x= [ev for ev in orders[machin] if ev.job==jb1]						
						
						orders[agent].remove(x[0])
						del jobson[jb1]
						
						st2 = partial(self.start_time, jb1, orders, jobson, prec, commcost, compcost)
						ft2 = lambda machine: st2(machine) + compcost(jb1, machine)					
						agent = min([key for key in orders.keys() if key!=agent], key=ft2)
						start = st2(agent)
						end = ft2(agent)
						orders[agent].append(Event(jb1, start, end))
						
						jobson[jb1]=agent
						reschedule=True
						#print('x')
						self.allocate(job, orders, jobson, prec, compcost, commcost)
						
		if not reschedule:
			orders[agent].append(Event(job, start, end))
			orders[agent] = sorted(orders[agent], key=lambda e: e.start)
		# Might be better to use a different data structure to keep each
		# agent's orders sorted at a lower cost.

			jobson[job] = agent
			