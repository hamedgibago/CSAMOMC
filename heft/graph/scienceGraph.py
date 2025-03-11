
import sys,math
sys.path.append("C:/heft-master/heft/graph")

import random
from graphBase import *
from graph import graphTool


#global communicateDic
#global computeDic

#Machine performance in GigaFlops:
# a 2
# b 7.1
# c 11.4
# d 3.9
# e 50

class scienceGraph(graphBase):
	def __init__(self,size=25,name='Montage'):
		self.communicateDic={}
		self.computeDic={}
		self.name=name
		#job sizes from montage_100.xml we summed 4 sized attribute and its about 12*10^6 12Mg Flops
		# 12,546,000		
		#self.jobSize=12546000
		#self.dag=graphTool.readXmlGraph('C:/heft-master/heft/graph/Montage_'+str(size)+'.xml')
		self.root=graphTool.loadXmlGraph('C:/heft-master/heft/graph/'+name+'_'+str(size)+'.xml')
		self.dag=graphTool.getDag(self.root)
		self.averageBandwidth=1000
		self.jobSizeList={}
		self.loadJobSize()
		self.succ=graphTool.reverse_dict(self.dag)
		self.loadCommCost()
		
		
	
	def loadCommCost(self):
		for nj in self.succ:
			#get output files from parent(ni)
			for ni in self.succ[nj]:
				outputFiles=graphTool.getFiles(self.root,ni,'output')
				sumFiles=graphTool.getSumFiles(self.root,nj,outputFiles,'input')
				
				#Based on sumFiles in bytes in workflowsim
				self.communicateDic[(ni,nj)]=((sumFiles/1000000)*8)/self.averageBandwidth										
		
	
	def loadJobSize(self):
		for job in self.dag.keys():
			self.jobSizeList[job]=graphTool.getJobSize(self.root,job)
			
	def compcost(self,job, agent):
		#for speed up and prevent from reading and parsing xml everytime,
		#we just load all job size at the begining of the class load
		
		if type(job) is int:
			jobSize= self.jobSizeList['ID{:05d}'.format(job-1)]			
		else:
			jobSize= self.jobSizeList[job]			
		
		if agent=='a':	
			res= jobSize / 2 
		elif agent=='b':
			res=jobSize / 7.1 
		elif agent=='c':
			res =jobSize / 11.4 
		elif agent=='d':
			res= jobSize / 3.9 
		elif agent=='e':
			res=jobSize / 50 		
		
		return jobSize
	
		#for converting job id to string in scientific graphs
		#if type(job) is int:
			#size=graphTool.getJobSize(self.root,'ID{:05d}'.format(job-1))
		#else:
			#size=graphTool.getJobSize(self.root,job)
						
		#return size
	
		#for generating random job size(has bugs always 10^-9)
		#giga=math.pow(10,9)
		##jobSize=randint(1*math.pow(10,9),1**math.pow(10,10))
		#key=str(job)+'-'+str(agent)
		#if key in self.computeDic.keys():
			#return self.computeDic[key]
		#else:		
			#jobSize=random.random()*math.pow(10,2)			
			#if agent=='a':	
				#res= jobSize / (2 * giga)
			#elif agent=='b':
				#res=jobSize / (7.1 * giga)
			#elif agent=='c':
				#res =jobSize / (11.4 * giga)
			#elif agent=='d':
				#res= jobSize / (3.9 * giga)
			#elif agent=='e':
				#res=jobSize / (50 * giga)
			
			#self.computeDic[key]=res	
			##rounding	
			##return round(res,6)
			#return res
		#End of for generating random job size
	
	layers={1:[1],
		    2:[2,3,4,5],
		    3:[6,7,8],
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
	
	def commcost(self,ni, nj, A, B):
		if(A==B):
			return 0
		else:
			
			return self.communicateDic[(ni,nj)]
			
			##check if ni is parent of nj
			#if nj in self.dag[ni]:
				##get output files from parent(ni)
				#outputFiles=graphTool.getFiles(self.root,ni,'output')
				#sumFiles=graphTool.getSumFiles(self.root,nj,outputFiles,'input')
				
				##Based on sumFiles in bytes in workflowsim
				#return ((sumFiles/1000000)*8)/self.averageBandwidth		
				##return sumFiles			
			#else:
				#return 0
			
			
			#for generating random job size(has bugs always 10^-9)
			#key=str(ni)+'-'+str(nj)+'-'+str(A)+'-'+str(B)
			#if key in self.communicateDic.keys():
				#return self.communicateDic[key]
			#else:		
			##return jobSize/(100 * math.pow(10,6))
				#res=random.random()*math.pow(10,3) * 1.6
				#self.communicateDic[key]=res
			#return res
			#End of for generating random job size
	
	def encost(self,job, agent):
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