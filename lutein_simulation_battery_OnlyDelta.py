import numpy as np
import pandas as pd
from pybrain.datasets import SupervisedDataSet
from itertools import product
import math
from pybrain.structure import SigmoidLayer, LinearLayer
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.xml.networkwriter import NetworkWriter
from pybrain.tools.xml.networkreader import NetworkReader
import pylab
from utilities import normalizer
import sys

#columns tags
lista_col=['Illumination umol/m2/s','Time (h)', 'DCW (mg/l)', 'nitrate (mg/l)', 'lutein content (mg/l)']
lista_col1=['Illumination','Time', 'DCW', 'nitrate', 'lutein']
lista_col2=['Illumination', 'DCW', 'nitrate', 'lutein']
#folders from which to pick saved networks and save data files
net_fold='networks/'
save_fold='data/'
#import as Pandas Data the excel file
mb2 = pd.read_excel('lutein_exp_data.xlsx', sheetname='Sheet1', header=None,usecols=range(5),columns=lista_col)
mb2.col=lista_col1
array_data=mb2.values[1:]#keep only the numbers and turn into numpy array

length_data=len(array_data)

#the four sets of experiments are given separately. These are their start and end points
set_lengths=((0,13),(13,26),(26,39),(39,52))
#third set is separated
#an enchanced array that will contain the noisy data

cross_val=array_data[set_lengths[2][0]:set_lengths[2][1]]
times=normalizer(cross_val[:,1])
#different deltaT.Normalized. Should be 12,24,36,72
#print cross_val

deltaT=np.append(times[1:4],[times[6]])
#sys.exit()

intrv=[1,2,3,6]

#Open networks

network_2=NetworkReader.readFrom(net_fold+ 'network_Type2H1STD.xml')
network_4=NetworkReader.readFrom(net_fold+ 'network_Type2H2STD.xml')
#normalize the cross validation set

#normalize the other data with custom function. Remove cross validation and rearrange
array_data=np.column_stack((normalizer(array_data[:,0]),normalizer(array_data[:,1]),normalizer(array_data[:,2]),normalizer(array_data[:,3]),normalizer(array_data[:,4])))
array_data=np.concatenate((array_data[:set_lengths[0][1],:],array_data[set_lengths[1][0]:set_lengths[1][1],:],array_data[set_lengths[3][0]:set_lengths[3][1],:],array_data[set_lengths[2][0]:set_lengths[2][1],:]))
#print pd.DataFrame(array_data,columns=lista_col1)


#------------------------------------------Test on set 1,2 and 4--------------------------------------------------------------------
#NEED to add cross validation set, first let's finish
#this will be used for export
alpha=pd.DataFrame(array_data,columns=lista_col1)
#print alpha.head
alpha.drop('Time',axis=1, inplace=True)

#for each network do the round
#This tests it against each set. K represents the starting point within the array of data

#simulation for Network 2, 1 Hidden.
#This type of network only takes 4 inputs, and does not take the time interval
#This one has 1 hidden layer
for k in [0,13,26]:
    sim_net2=np.array([np.append([array_data[k,0]],array_data[k,2:])])
    #This simulates for  for 12 points
    for j in xrange(12):

        ans=network_2.activate((sim_net2[j][0],sim_net2[j][1],sim_net2[j][2],sim_net2[j][3]))
        ansK=[array_data[k,0],sim_net2[j][1]+ans[0],sim_net2[j][2]+ans[1],sim_net2[j][3]+ans[2]]
        sim_net2=np.append(sim_net2,[ansK],axis=0)
    if k==0 :

        temp2=pd.DataFrame(sim_net2,columns=lista_col2)
    else:
        temp2=pd.concat([temp2,pd.DataFrame(sim_net2,columns=lista_col2)],axis=0,ignore_index=True)



alpha=pd.concat([alpha,temp2],axis=1,keys=['Experimental','Simulated'])    
#save
alpha.to_csv(save_fold+'Lutein_NN_Type2H1_TestCrossSTD.csv')
#overwrite so that it can be used again
alpha=pd.DataFrame(array_data,columns=lista_col1)
alpha.drop('Time',axis=1, inplace=True)

#simulation for Network 2, 2 Hidden.
#This type of network only takes 4 inputs, and does not take the time interval
#This one has 2 hidden layers
for k in [0,13,26]:
    sim_net4=np.array([np.append([array_data[k,0]],array_data[k,2:])])
    for j in xrange(12):
        ans=network_4.activate((sim_net4[j][0],sim_net4[j][1],sim_net4[j][2],sim_net4[j][3]))
        ansK=[array_data[k,0],sim_net4[j][1]+ans[0],sim_net4[j][2]+ans[1],sim_net4[j][3]+ans[2]]
        sim_net4=np.append(sim_net4,[ansK],axis=0)
    if k==0 :
        temp4=pd.DataFrame(sim_net4,columns=lista_col2)
    else:
        temp4=pd.concat([temp4,pd.DataFrame(sim_net4,columns=lista_col2)],axis=0,ignore_index=True)

alpha=pd.concat([alpha,temp4],axis=1,keys=['Experimental','Simulated'])    
#save
alpha.to_csv(save_fold+'Lutein_NN_Type2H2_TestCrossSTD.csv')
#overwrite
alpha=pd.DataFrame(array_data,columns=lista_col1)
alpha.drop('Time',axis=1, inplace=True)



#------------------------------------------Test on  cross validation set 3--------------------------------------------------------------------
#this will be used for export
beta=pd.DataFrame(array_data,columns=lista_col1)
beta.drop('Time',axis=1, inplace=True)
#for each network do the round
#do the k
#this takes out the cross validation set for ease of use.
cross_arr=array_data[39:,:]
sim_net2=np.array([np.append([cross_arr[0,0]],cross_arr[0,2:])])
#simulation for Network 2, 1 Hidden.
for j in xrange(12):
    ans=network_2.activate((cross_arr[j][0],cross_arr[j][1],cross_arr[j][2],cross_arr[j][3]))
    ansK=[cross_arr[0,0],cross_arr[j][1]+ans[0],cross_arr[j][2]+ans[1],cross_arr[j][3]+ans[2]]
    sim_net2=np.append(sim_net2,[ansK],axis=0)

temp2=pd.DataFrame(sim_net2,columns=lista_col2)
beta=pd.concat([beta,temp2],axis=1,keys=['Experimental','Simulated'])    
#save
beta.to_csv(save_fold+'Lutein_NN_Type2H1_CrossValSTD.csv')
#overwrite
beta=pd.DataFrame(array_data,columns=lista_col1)
beta.drop('Time',axis=1, inplace=True)

#simulation for Network 2, 2 Hidden.
sim_net4=np.array([np.append([cross_arr[0,0]],cross_arr[0,2:])])
for j in xrange(12):
    ans=network_4.activate((cross_arr[j][0],cross_arr[j][1],cross_arr[j][2],cross_arr[j][3]))
    ansK=[cross_arr[0,0],cross_arr[j][1]+ans[0],cross_arr[j][2]+ans[1],cross_arr[j][3]+ans[2]]
    sim_net4=np.append(sim_net4,[ansK],axis=0)

temp4=pd.DataFrame(sim_net4,columns=lista_col2)
beta=pd.concat([beta,temp4],axis=1,keys=['Experimental','Simulated'])    
#save
beta.to_csv(save_fold+'Lutein_NN_Type2H2_CrossValSTD.csv')
#overwrite
beta=pd.DataFrame(array_data,columns=lista_col1)
beta.drop('Time',axis=1, inplace=True)

