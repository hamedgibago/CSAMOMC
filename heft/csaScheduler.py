from core import *
import cpop,util,sys
import math,string,numpy as np


class csa_scheduler(cpop.cpop):
		
	def __init__(self,dag, machines, compcost,commcost,graph):
		self.succ=dag
		self.agents=machines
		self.compcost=compcost
		self.commcost=commcost
		self.graph=graph
		self.makespan=sys.float_info.max
		self.cost=sys.float_info.max
		self.energy=0
		self.qos=0
		self.jobson=dict()
		self.orders = {agent: [] for agent in self.agents}
		#self.ref_point=np.array([sys.maxsize,sys.maxsize])
		self.ref_point=np.array([10000000.0,30000.0])
		self.ref_point_rect=self.ref_point[0]*self.ref_point[1]
		#self.schedules={}
		self.iterations={}
		self.data=[]
		self.__tempResult__=1
		
		#use this dict for converting machine numbers to letters "a to z".
		#It just supports 26 machines.
		#TODO: In future converter should be created for this to support machines by numbers
		#which will support any number of machines
		#not just "a to z" letters.
		self.cn_dict=dict(zip(range(1,27),string.ascii_lowercase))
	
	def schedule_function(self,variables_values = [0, 0],iteration=0,popNum=0):
		
		selectedSchedule=[int(i) for i in variables_values]						
		
		prec = reverse_dict(self.succ)
		
		self.jobson=dict()
		self.orders = {agent: [] for agent in self.agents}
						
		#Added 1 for starting jobs from 1 not 0, because of dheft and heft graph eror
		#for ni in range(len(selectedSchedule)+1):
			#super().allocate(ni, self.orders, self.jobson, prec, self.compcost, self.commcost,self.cn_dict[selectedSchedule[ni]])
		for ni in range(1,len(selectedSchedule)+1):
			super().allocate(ni, self.orders, self.jobson, prec, self.compcost, self.commcost,self.cn_dict[selectedSchedule[ni-1]])
		
		(makespan,qos,energy,cost)=util.calculateResults(self.orders, self.jobson,self.graph)
		
		
		#if (makespan*cost) > self.ref_point_rect:
			#self.ref_point_rect=makespan*cost
			
		#if self.ref_point_rect<0:
			#print('Negave ref_point_rect in csaScheduler. (overflow)')
			#exit()
		
		#result=abs(makespan-cost)	
		#if result< tempResult:
			#self.makespan=makespan
			#self.qos=qos
			#self.energy=energy
			#self.cost=cost
			#tempResult=result
		
		
		#print('makespan={} cost={}'.format(makespan,cost))
		
		
		#return self.makespan*self.cost
		#print('makespan={} cost={}'.format(self.makespan,self.cost))
		
		makespan=round(makespan,2)
		cost=round(cost,2)
		print('makespan={} cost={}'.format(makespan,cost))
		self.data.append((makespan,cost))
		
		#if makespan < self.makespan:
		##if abs(makespan-cost) < abs(self.makespan-self.cost):
			#self.makespan=makespan
			#self.qos=qos
			#self.energy=energy
			#self.cost=cost			
		
		#return makespan
		#return abs(self.makespan-self.cost)

		#hypervalue results calculation
		result=util.calc_hv(makespan, cost, self.ref_point)
		
		if result<=0:
			print('Hyper volume 0')
			exit()		
		
		if result > self.__tempResult__:
			self.makespan=makespan
			self.qos=qos
			self.energy=energy
			self.cost=cost
			self.__tempResult__=result
		return result
	
	