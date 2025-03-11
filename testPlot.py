import numpy as np
import matplotlib.pyplot as plt

taskLength=[100,200,300,400,500]


CsaRes=[377.87,790.6099999999999,1128.7600000000002,1542.9400000000003,1901.6600000000005]
cpopRes=[(413.6418545680001, 0.0, 0, 9.299999999999999),(834.5074027840001, 0.0, 0, 16.500000000000007),
 (1233.7833839759994, 0.0, 0, 20.500000000000014),
 (1640.3249406479995, 0.0, 0, 24.500000000000018),
 (2105.5109725679995, 0.0, 0, 29.400000000000023)]
tc3popRes=[(413.4816912720001, 0.0, 0, 9.9),
 (834.5074027840001, 0.0, 0, 16.500000000000007),
 (1233.7833839759994, 0.0, 0, 20.500000000000014),
 (1640.3281980639995, 0.0, 0, 24.30000000000002),
 (2105.5109725679995, 0.0, 0, 29.400000000000023)]


fig, ax = plt.subplots(1,2)

x= np.arange(100,505,100)   # the label locations
width = 10# the width of the bars
#bar graph
ax[0].bar(x-2*width,CsaRes,width+10,label='CSA',edgecolor='black')
ax[0].bar(x,[i[0] for i in cpopRes],width+10,label='Cpop',edgecolor='black')
ax[0].bar(x +2*width,[i[0] for i in tc3popRes],width+10,label='TC3pop',edgecolor='black')

#ax.bar([23,53],CsaRes,1.5,label='CSA',edgecolor='black')

#dim=np.arange(0.5,3.1,0.5)
#plt.xticks(dim)

#dim=np.arange(0,4100,1000)
#plt.yticks(dim)

#plt.xlabel('Number of Tasks')
#plt.ylabel('Makespan')

#ax[0].set(xlabel='Number of Tasks',ylabel='Makespan')

#ax[0].legend()
#ax[0].grid()







#plt.xlabel('Number of Tasks')
#plt.ylabel('Cost')

ax[1].set(xlabel='Number of Tasks',ylabel='Cost')


ax[1].bar(x-2*width,CsaRes,width+10,label='CSA',edgecolor='black')
ax[1].bar(x,[i[3] for i in cpopRes],width+10,label='Cpop',edgecolor='black')
ax[1].bar(x +2*width,[i[3] for i in tc3popRes],width+10,label='TC3pop',edgecolor='black')

plt.legend()
plt.grid()
plt.show()

#data from 100 to 500 tasks
#CsaRes=[377.87,
 #790.6099999999999,
 #1128.7600000000002,
 #1542.9400000000003,
 #1901.6600000000005]

#cpopRes
#[(413.6418545680001, 0.0, 0, 9.299999999999999),
 #(834.5074027840001, 0.0, 0, 16.500000000000007),
 #(1233.7833839759994, 0.0, 0, 20.500000000000014),
 #(1640.3249406479995, 0.0, 0, 24.500000000000018),
 #(2105.5109725679995, 0.0, 0, 29.400000000000023)]


#tc3popRes
#[(413.4816912720001, 0.0, 0, 9.9),
 #(834.5074027840001, 0.0, 0, 16.500000000000007),
 #(1233.7833839759994, 0.0, 0, 20.500000000000014),
 #(1640.3281980639995, 0.0, 0, 24.30000000000002),
 #(2105.5109725679995, 0.0, 0, 29.400000000000023)]
 
