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

net_fold='networks/'
#import as Pandas Data the excel file
exp_1 = pd.read_excel('Second/First_Exp.xlsx', sheetname='Sheet1', header=None,usecols=range(5),columns=lista_col)
exp_2 = pd.read_excel('Second/Second_Exp.xlsx', sheetname='Sheet1', header=None,usecols=range(5),columns=lista_col)
exp_1.col=lista_col1
exp_2.col=lista_col1
flow1=np.array([(4*[0]+8*[127.5])*3])
flow2=np.array([(4*[0]+8*[25.5])*4])

arr1=np.concatenate((exp_1.values[1:],flow1.T),axis=1)
arr2=np.concatenate((exp_2.values[1:],flow2.T),axis=1)


arr_test=np.concatenate((arr1[0:12],arr1[24:36],arr2[0:12],arr2[24:36],arr2[36:48]),axis=0)
arr_val=np.concatenate((arr1[12:24],arr2[12:24]),axis=0)

nEpochs=300
#We will do all 4 types, with data replication
noise_list=[0.03,0.05]

#add noise
length_data=len(arr_test)

#the four sets are given separately
set_lengths=((0,12),(12,24),(24,36),(36,48),(48,60))
#third set is separated
#an enchanced array that will contain the noisy data
enh_array=np.empty((1,6))#np.zeros((38,5))

ds2 = SupervisedDataSet(5, 3)
for noise in noise_list:
    enh_array=np.empty((1,6))#np.zeros((38,5))
    #augment the enhanced array
    for i,m in product(set_lengths,xrange(100)):
        #i is the dataset
        #for each dataset we produce a 100 noise_arrays
        temp_data=arr_test[i[0]:i[1]]
        #generate an array the size of the current sub array, to be added.
        noise_array=np.array([[temp_data[k,0]]+[temp_data[k,1]]+[temp_data[k,j]+temp_data[k,j]*np.random.uniform(-noise,noise) for j in xrange(2,6)] for k in xrange(len(temp_data))])
        enh_array=np.concatenate((enh_array,noise_array),axis=0)

    #Data normalization
    #print noise_array
    # a custom built function normalizes along the column. The columns are then put back together
    #TIME REMOVED
    #now we have in order
    #Illumination DCW nitrate Lutein n-Flowrate
    enh_array=np.column_stack((normalizer(enh_array[1:,0]),normalizer(enh_array[1:,2]),normalizer(enh_array[1:,3]),normalizer(enh_array[1:,4]),normalizer(enh_array[1:,5])))


        #build and populate datasets

        #this is meant to 
    r_lengths=[[i,i+12] for i in xrange(0,12*100*5,12)]
        #print r_lengths[-1]
        #print len(enh_array)
        #dataset without time
        #print enh_array

    for j in r_lengths:
        temp_data=enh_array[j[0]:j[1]]        
        for k in xrange(len(temp_data)-1):
            ds2.addSample((temp_data[k][0],temp_data[k][1],temp_data[k][2],temp_data[k][3],temp_data[k][4]), (temp_data[k+1][1]-temp_data[k][1],temp_data[k+1][2]-temp_data[k][2],temp_data[k+1][3]-temp_data[k][3]))
            #in this one only 4 inputs.

    #both types of ANN will be run, and with 1 and 2 hidden layers


net2 = buildNetwork(5,
                           20, # number of hidden units
                           3,
                           bias = True,
                           hiddenclass = SigmoidLayer,
                           outclass = LinearLayer
                        )



net4 = buildNetwork(5,
                           15, # number of hidden units
                           15, # number of hidden units
                           3,
                           bias = True,
                           hiddenclass = SigmoidLayer,
                           outclass = LinearLayer
                        )
    #initialize the structures
net2.randomize()
net2.sortModules()
net4.randomize()
net4.sortModules()
    #create trainers
    #train for set amount of epochs
    #save networks to disc
trainer2 = BackpropTrainer(net2, ds2, verbose = True)
trainer2.trainEpochs(nEpochs)
NetworkWriter.writeToFile(net2,net_fold+ 'network_Type2H1New_less.xml')
trainer4 = BackpropTrainer(net4, ds2, verbose = True)
trainer4.trainEpochs(nEpochs)
NetworkWriter.writeToFile(net4,net_fold+ 'network_Type2H2New_less.xml')

print 'Work completed. Check out the networks have been saved'

