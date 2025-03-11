import numpy as np
from pymoo.problems.multi import *
from pymoo.visualization.scatter import Scatter

# The pareto front of a scaled zdt1 problem
#pf = get_problem("zdt1").pareto_front()
pf = ZDT1().pareto_front()

# The result found by an algorithm
A = pf[::10] * 1.1

# plot the result
#Scatter(legend=True).add(pf, label="Pareto-front").add(A, label="Result").show()


#import pymoo.indicators.hv as HV
#from pymoo.indicators import hv
from pymoo.vendor import hv as HH


ref_point = np.array([1.2, 1.2])

#ind = ind = HV(ref_point=ref_point)
#ind.do([])
ind=HH.HyperVolume(ref_point)
#print("HV", ind(A))
t= ind.compute(A)
print(t)