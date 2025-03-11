dag={1:(2,3,4,5,6),
     2:(8,9),
     3:(7,),
     4:(8,9),
     5:(9,),
     6:(8,),
     7:(10,),
     8:(10,),
     9:(10,),
     10:()}

def Peft():	
	peft=0
	for i in dag.keys():
		for j in range(['a..b']):		
			if compcost(i,j)>peft:
				peft=compcost(i,j)
	return peft

def compcost(job, agent):
	if(job==1):
		if(agent=='a'):
			return 14
		elif(agent=='b'):
			return 16
		else:
			return 9

	if(job==2):
		if(agent=='a'):
			return 13
		elif(agent=='b'):
			return 19
		else:
			return 18
	if(job==3):
		if(agent=='a'):
			return 11
		elif(agent=='b'):
			return 13
		else:
			return 19
	if(job==4):
		if(agent=='a'):
			return 13
		elif(agent=='b'):
			return 8
		else:
			return 17
	if(job==5):
		if(agent=='a'):
			return 12
		elif(agent=='b'):
			return 13
		else:
			return 10
	if(job==6):
		if(agent=='a'):
			return 13
		elif(agent=='b'):
			return 16
		else:
			return 9
	if(job==7):
		if(agent=='a'):
			return 7
		elif(agent=='b'):
			return 15
		else:
			return 11
	if(job==8):
		if(agent=='a'):
			return 5
		elif(agent=='b'):
			return 11
		else:
			return 14
	if(job==9):
		if(agent=='a'):
			return 18
		elif(agent=='b'):
			return 12
		else:
			return 20
	if(job==10):
		if(agent=='a'):
			return 21
		elif(agent=='b'):
			return 7
		else:
			return 16



def commcost(ni, nj, A, B):
	if(A==B):
		return 0
	else:
		if(ni==1 and nj==2):
			return 18
		if(ni==1 and nj==3):
			return 12
		if(ni==1 and nj==4):
			return 9
		if(ni==1 and nj==5):
			return 11
		if(ni==1 and nj==6):
			return 14
		if(ni==2 and nj==8):
			return 19
		if(ni==2 and nj==9):
			return 16
		if(ni==3 and nj==7):
			return 23
		if(ni==4 and nj==8):
			return 27
		if(ni==4 and nj==9):
			return 23
		if(ni==5 and nj==9):
			return 13
		if(ni==6 and nj==8):
			return 15
		if(ni==7 and nj==10):
			return 17
		if(ni==8 and nj==10):
			return 11
		if(ni==9 and nj==10):
			return 13
		else:
			return 0	