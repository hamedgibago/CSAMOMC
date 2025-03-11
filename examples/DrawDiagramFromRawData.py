import sys,math,os
sys.path.append("C:/heft-master/heft")

import util
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mp

graphName='Ligo'

CsaRes=util.readData('rawdata/csa-500')
cpopRes=util.readData('rawdata/cpop-500')
tc3popRes=util.readData('rawdata/tc3cpop-500')


fig, ax = plt.subplots(1,2,figsize=(15,7))
#fig.suptitle(graphName,fontsize=20)

x= np.arange(100,505,100)  # the label locations

width = 10# the width of the bars

ax[0].bar(x-2*width,[float(i[0]) for i in CsaRes],width+10,label='CSAMOMC',edgecolor='black')
ax[0].bar(x,[float(i[0]) for i in cpopRes],width+10,label='Cpop',edgecolor='black')
ax[0].bar(x +2*width,[float(i[0]) for i in tc3popRes],width+10,label='TC3pop',edgecolor='black')


ax[0].set_xlabel(xlabel='',fontsize = 15) 
ax[0].set_ylabel(ylabel='',fontsize = 15) 

ax[0].set(xlabel='Number of Tasks',ylabel='Makespan(second)')

ax[0].set_ylim(ymin=0)

ax[0].grid()
ax[0].legend()



#cost
ax[1].bar(x-2*width,[float(i[1]) for i in CsaRes],width+10,label='CSAMOMC',edgecolor='black')
ax[1].bar(x,[float(i[3]) for i in cpopRes],width+10,label='Cpop',edgecolor='black')
ax[1].bar(x +2*width,[float(i[3]) for i in tc3popRes],width+10,label='TC3pop',edgecolor='black')


ax[1].set_xlabel(xlabel='',fontsize = 15) 
ax[1].set_ylabel(ylabel='',fontsize = 15) 

ax[1].set(xlabel='Number of Tasks',ylabel='Cost($)')

ax[1].set_ylim(ymin=0)

ax[1].grid()
ax[1].legend()

#plt.savefig('C:\\heft-master\\examples\\rawData\\'+graphName+'.eps', bbox_inches='tight')
plt.savefig('C:\\heft-master\\examples\\rawData\\'+graphName+'.jpg', bbox_inches='tight',dpi=300)
plt.show()