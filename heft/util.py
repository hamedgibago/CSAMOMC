import math,csv
import itertools as it
from graph import graphBase,heftGraph,qlheftGraph,scienceGraph
from pymoo.problems.multi import *
from pymoo.vendor import hv as HV


def reverse_dict(d):
    """ Reverses direction of dependence dict

    >>> d = {'a': (1, 2), 'b': (2, 3), 'c':()}
    >>> reverse_dict(d)
    {1: ('a',), 2: ('a', 'b'), 3: ('b',)}
    """
    result = {}
    for key in d:
        for val in d[key]:
            result[val] = result.get(val, tuple()) + (key, )
    return result

def calc_hv(p1,p2,ref_point):
    ind=HV.HyperVolume(ref_point)
    hyper= ind.compute(np.array([[p1,p2]]))
    return hyper

def find_job_event(job_name, orders_dict):
    for event in it.chain.from_iterable(orders_dict.values()):
        if event.job == job_name:
            return event


def calculateResults(orders,jobson,graph):        
    makespan=0
    energy=0
    cost=0
    qos=0
    sigmaPeft=0

    for eachP in sorted(orders):
        tempOrders=[i for i in orders if i!=[]]
        tmpMakespan=max([i.end for i in orders[eachP] if orders[eachP]!=[]],default=0)
        if tmpMakespan>makespan:
            makespan=tmpMakespan
        #print(eachP,orders[eachP])
        x=[i for i in orders[eachP]]

        time=0
        subSetList=[]
        tempList=[]
        for i in range(len(x)):

            if i!=len(x)-1:
                if x[i].end==x[i+1].start:
                    tempList.append(x[i])
                else:
                    tempList.append(x[i])
                    subSetList.append(tempList)
                    tempList=[]
            else:
                if x[i-1].end==x[i].start:
                    tempList.append(x[i])
                    subSetList.append(tempList)
                    tempList=[]
                else:
                    subSetList.append([x[i]])

            #time=time+ x[i].end - x[i].start
            #if x[i].end==x[i+1].start:
                #time=time + x[i+1].end - x[i+1].start
            #else:
                #subSet=True                                        
        for subset in subSetList:
            time=subset[-1].end -subset[0].start
            #cost= cost+ heftGraph.cost(eachP) *  math.ceil(time/3600)
            cost= cost+ graph.cost(eachP) *  math.ceil(time/3600)

        #spentTimes= sum([abs(t.end-t.start) for t in x])
        #if x!=[]:
            #spentTimes=x[-1].end - x[0].start
            #cost=cost+ montageGraph.cost(eachP) *  math.ceil(spentTimes/3600)

        if type(graph) is qlheftGraph:
            #z= [qlheftGraph.encost(t.job,eachP)*(t.end-t.start) for t in x]
            z= [graph.encost(t.job,eachP) for t in x]
            #print(z)
            energy=energy+sum(filter(None,z))                
            sigmaPeft=graph.sigmaPeft()
        #TODO: check if this line and sigmaHeft should be in or outside for eachP loop
        if makespan!=0:
            qos=sigmaPeft/makespan
        
    return (makespan,qos,energy,cost)

def readData(datatype):    
    with open(datatype.lower()+'.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data


def writeData(datatype,row): 
    # open the file in the write mode
    with open(datatype.lower()+'.csv', 'a', newline='') as f:        
        writer = csv.writer(f)    
        # write a row to the csv file
        writer.writerows(row)
