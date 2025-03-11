from enum import Enum

class Layer(Enum):
	CLOUD=1
	EDGE=2
	
class machine:
	def __init__(self,number,epsilon,Bu,Cen,fr):
		self.number=number
		self.epsilon=epsilon
		self.Bu=Bu
		self.Cen=Cen
		self.fr=fr
	
	def __init__(self,cores,fr,mem,bandwith,layer,index):
		self.index=index
		self.cores=cores
		self.fr=fr
		self.mem=mem
		self.bandwith=bandwith
		self.layer=layer
		self.Uvcpu=0
		self.OL=0
		self.Fp=0
		
		#can find and search powers here:
		#https://www.spec.org/cgi-bin/osgresults?conf=power_ssj2008&op=form		
		
		#https://www.spec.org/power_ssj2008/results/res2010q4/power_ssj2008-20101019-00304.html
		if fr>=1.7 and fr<= 1.8: 
			self.idle=32
			self.full=70
		#https://www.spec.org/power_ssj2008/results/res2007q4/power_ssj2008-20071128-00001.html	
		if fr>1.8 and fr<= 2: 
			self.idle=180
			self.full=260 
		
		#https://www.spec.org/power_ssj2008/results/res2009q2/power_ssj2008-20090316-00131.html
		if fr>=3 and fr< 3.2: 
			self.idle=213
			self.full=353
			
		#https://www.spec.org/power_ssj2008/results/res2007q4/power_ssj2008-20071129-00015.html
		if fr>=3.2 and fr<= 3.6: 
			self.idle =159
			self.full=336						
			
	#def createVms():
		#for i 
	