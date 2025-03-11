from pymoo.problems.multi import *
from pymoo.vendor import hv as HV


def calc_hv(p1,p2,ref_point):
	ind=HV.HyperVolume(ref_point)
	hyper= ind.compute(np.array([[p1,p2]]))
	return hyper

ref_point=np.array([3,3])

print(calc_hv(1,1,ref_point))
print(calc_hv(2,2,ref_point))
print(calc_hv(40,40,ref_point))