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
from utilities import standardizer
import sys

lista_col=['Illumination umol/m2/s','Time (h)', 'DCW (mg/l)', 'nitrate (mg/l)', 'lutein content (mg/l)']
lista_col1=['Illumination','Time', 'DCW', 'nitrate', 'lutein']
lista_col2=['Illumination','Time', 'DCW', 'nitrate', 'lutein','NFlowrate']
net_fold='networks/'
el_fold='elbow_rule/'
#import as Pandas Data the excel file
exp_1 = pd.read_excel('Second/First_Exp.xlsx', sheetname='Sheet1', header=None,usecols=range(5),columns=lista_col)
exp_2 = pd.read_excel('Second/Second_Exp.xlsx', sheetname='Sheet1', header=None,usecols=range(5),columns=lista_col)

flow1=np.array([(4*[0]+8*[127.5])*3])
flow2=np.array([(4*[0]+8*[25.5])*4])

arr1=np.concatenate((exp_1.values[1:],flow1.T),axis=1)
arr2=np.concatenate((exp_2.values[1:],flow2.T),axis=1)

arr_test=np.concatenate((arr1[0:12],arr1[24:36],arr2[0:12],arr2[24:36],arr2[36:48]),axis=0)
arr_val=np.concatenate((arr1[12:24],arr2[12:24]),axis=0)

beta=pd.DataFrame(arr_test,columns=lista_col2)
beta.drop('Time',axis=1, inplace=True)
beta_Val=beta.values

#the four sets are given separately
set_lengths=((0,12),(12,24),(24,36),(36,48),(48,60))

enh_array=np.empty((1,5))#np.zeros((38,5))

n_hidden=[5,10,15,20,30,50]#to become a list
n_Epochs=[15,50,100,200,300,400,600] #
#print mb2
#print mb2.head
error_storage=[]


#----------
# build the datasets
#----------

ds2 = SupervisedDataSet(5, 3)

#Data normalization
# a custom built function normalizes along the column. The columns are then put back together
#Illumination DCW nitrate Lutein n-Flowrate
enh_array=np.column_stack((standardizer(beta_Val[:,0]),standardizer(beta_Val[:,1]),standardizer(beta_Val[:,2]),standardizer(beta_Val[:,3]),standardizer(beta_Val[:,4])))

#dataset with flow

for j in set_lengths:
    temp_data=enh_array[j[0]:j[1]]    
    for k in xrange(len(temp_data)-1):
        ds2.addSample(temp_data[k], (temp_data[k+1][1]-temp_data[k][1],temp_data[k+1][2]-temp_data[k][2],temp_data[k+1][3]-temp_data[k][3]))

for nH,nE in product(n_hidden,n_Epochs):
    #----------
    # build the network in variable 
    #----------

    net2 = buildNetwork(5,
                       nH, # number of hidden units
                       nH, # number of hidden units
                       3,
                       bias = True,
                       hiddenclass = SigmoidLayer,
                       outclass = LinearLayer
                       )


    #----------
    # train until convergence
    #----------
    net2.randomize()
    net2.sortModules()
    trainer2 = BackpropTrainer(net2, ds2, verbose = False)
    trainer2.trainEpochs(nE)

    #----------
    # evaluate
    #----------

    #simulation for Network 2.
    sim_net2=[]
    for j in set_lengths:
        temp_data=enh_array[j[0]:j[1]]
        ansK=[]       
        for k in xrange(len(temp_data)-1):
            ans=net2.activate(temp_data[k])
            ansK.append([abs(temp_data[k+1][1]-(temp_data[k][1]+ans[0])),abs(temp_data[k+1][2]-(temp_data[k][2]+ans[1])),abs(temp_data[k+1][3]-(temp_data[k][3]+ans[2]))])
        sim_net2.append(np.mean(ansK,axis=0))

    #get  error for each variable difference. Since they are already all normalized, no std
    #maximum error
    error2=max(np.mean(sim_net2,axis=0))
    print 'For network 2 at hidden layer strata ',nH,' the error is ', error2
    error_storage.append([nH,nE,error2])

alpha=pd.DataFrame(error_storage,columns=['Num_Neuron_Hidden','Num_Epochs','Network_Struc_2'])
#save to csv
alpha.to_csv(el_fold+'nHidden_test_New2.csv') 
print 'Work completed. Check out the csv to select the best structure'
