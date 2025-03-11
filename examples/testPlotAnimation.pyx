import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import sys
sys.path.append("C:/heft-master/heft")

import util as utl

fig, ax = plt.subplots()
#fig = plt.figure()

def setAxLables():
	dim=np.arange(0,max(x),5000)
	#dim=np.array([ 25,  50,  75, 100, 150])
	plt.xticks(dim)

	dim=np.arange(0,max(y),1)
	plt.yticks(dim)

	ax.set_ylim(ymin=0)
	ax.set_xlim(xmin=0)

	plt.xlabel('makspan')
	plt.ylabel('cost')

#def animate(i,k):
def animate(i):
	global frameNumber

	#scat.set_offsets((x[i], 0))		
	ax.plot(x[0:i],y[0:i],'*')
	#ax.plot(x[0:frameNumber],y[0:frameNumber],'*')

	#ax.clear()  
	#setAxLables()
	#ax.plot(x[frameNumber-7:frameNumber],y[frameNumber-7:frameNumber],'*')

	#title.set_text('{}/{} , makespan={} , cost={}'.format(str(frameNumber),totalFrames,x[i],y[i]))
	title.set_text('{}/{} , makespan={} , cost={}'.format(str(i),len(x),x[i],y[i]))
	#frameNumber=frameNumber+7
	#return scat,

data=utl.readData('../examples/ResultsCsv/csa-100all-makespan-and-cost')

x=[float(i[0]) for i in data]#[1,2,3,4,5]
y=[float(i[1]) for i in data]#[7,2,4,1,5]

#ax.plot(np.array(x),np.array(y),label='CSA',marker='o')

title = ax.set_title('')

setAxLables()

#plt.xticks(np.array(x))
#plt.yticks(np.array(y))

#totalFrames=int(len(x)/7)
#frameNumber=7
ani = animation.FuncAnimation(fig, animate, repeat=False,frames=len(x)+1 , interval=1)
#ani = animation.FuncAnimation(fig, animate, repeat=False,frames=totalFrames , interval=1,fargs=(frameNumber,))

plt.show()