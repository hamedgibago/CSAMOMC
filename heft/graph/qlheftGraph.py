import sys

sys.path.append("C:/heft-master/heft")
from graph import graphBase


class qlHeftGraph(graphBase.graphBase):
	def __init__(self):
		self.dag={1:(2,5),
			 2:(3,4),
			 3:(9,),
			 4:(9,),
			 5:(6,7,8,),
			 6:(9,),
			 7:(9,),
			 8:(9,),
			 9:()
			 }
		self.layers={1:[1],
				2:[2,5],
				3:[3,4,6,7,8],
				4:[9]}		
	def getLayer(self,n):
		for key,value in layers.items():
			if n in value:
				return key
	
	def sigmaPeft(self):	
		sumPeft=0
		peft=sys.maxsize
		for i in dag.keys():
			for j in [k for k in 'abc']:		
				if compcost(i,j)<peft:
					peft=compcost(i,j)
			sumPeft=sumPeft+peft
			peft=sys.maxsize
		return sumPeft
	
	def compcost(self,job, agent):
		if(job==1):
			if(agent=='a'):
				return 10
			elif(agent=='b'):
				return 9
			else:
				return 8
	
		if(job==2):
			if(agent=='a'):
				return 12
			elif(agent=='b'):
				return 10
			else:
				return 9
		if(job==3):
			if(agent=='a'):
				return 21
			elif(agent=='b'):
				return 18
			else:
				return 16
		if(job==4):
			if(agent=='a'):
				return 23
			elif(agent=='b'):
				return 20
			else:
				return 18
		if(job==5):
			if(agent=='a'):
				return 39
			elif(agent=='b'):
				return 34
			else:
				return 29
		if(job==6):
			if(agent=='a'):
				return 25
			elif(agent=='b'):
				return 21
			else:
				return 19
		if(job==7):
			if(agent=='a'):
				return 16
			elif(agent=='b'):
				return 14
			else:
				return 13
		if(job==8):
			if(agent=='a'):
				return 33
			elif(agent=='b'):
				return 29
			else:
				return 25
		if(job==9):
			if(agent=='a'):
				return 19
			elif(agent=='b'):
				return 16
			else:
				return 14
	
	def commcost(self,ni, nj, A, B):
		if(A==B):
			return 0
		else:
			if(ni==1 and nj==2):
				return 7
			if(ni==1 and nj==5):
				return 8
			if(ni==2 and nj==3):
				return 4
			if(ni==2 and nj==4):
				return 5
			if(ni==5 and nj==6):
				return 9
			if(ni==5 and nj==7):
				return 8
			if(ni==5 and nj==8):
				return 9
			if(ni==3 and nj==9):
				return 9
			if(ni==4 and nj==9):
				return 10
			if(ni==6 and nj==9):
				return 9
			if(ni==5 and nj==9):
				return 13
			if(ni==7 and nj==9):
				return 10
			if(ni==8 and nj==9):
				return 8		
			else:
				return 0	
	
	def encost(job, agent):
		if(job==1):		
			if(agent=='a'):
				return 132
			elif(agent=='b'):
				return 98
			else:
				return 102			
			
	
		if(job==2):
			if(agent=='a'):
				return 165
			elif(agent=='b'):
				return 291
			else:
				return 201
		if(job==3):
			if(agent=='a'):
				return 146
			elif(agent=='b'):
				return 35
			else:
				return 192			
		if(job==4):
			if(agent=='a'):
				return 210
			elif(agent=='b'):
				return 180
			else:
				return 161
		if(job==5):
			if(agent=='a'):
				return 391
			elif(agent=='b'):
				return 340
			else:
				return 290
		if(job==6):
			if(agent=='a'):
				return 190
			elif(agent=='b'):
				return 160
			else:
				return 140
		if(job==7):
			if(agent=='a'):
				return 98
			elif(agent=='b'):
				return 81
			else:
				return 151			
		if(job==8):
			if(agent=='a'):
				return 41
			elif(agent=='b'):
				return 20
			else:
				return 69
		if(job==9):
			if(agent=='a'):
				return 193
			elif(agent=='b'):
				return 152
			else:
				return 201