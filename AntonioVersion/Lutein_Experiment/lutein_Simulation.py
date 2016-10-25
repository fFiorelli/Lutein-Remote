import numpy as np
import pandas as pd
from pybrain.datasets import SupervisedDataSet
from itertools import product
import math
from pybrain.structure import SigmoidLayer, LinearLayer
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
import pylab
from utilities import normalizer
import sys

lista_col=['Illumination umol/m2/s','Time (h)', 'DCW (mg/l)', 'nitrate (mg/l)', 'lutein content (mg/l)']
lista_col1=['Illumination','Time', 'DCW', 'nitrate', 'lutein']
#import as Pandas Data the excel file
mb2 = pd.read_excel('lutein_exp_data.xlsx', sheetname='Sheet1', header=None,usecols=range(5),columns=lista_col)
mb2.col=lista_col1
array_data=mb2.values[1:]#keep only the numbers and turn into numpy array
nEpochs=200
#We will do all 4 types, with data replication
noise_list=[0,0.03,0.05]

#add noise
length_data=len(array_data)

#the four sets are given separately
set_lengths=((0,13),(13,26),(26,39),(39,52))
#third set is separated
#an enchanced array that will contain the noisy data
enh_array=np.empty((1,5))#np.zeros((38,5))
cross_val_set=array_data[set_lengths[2][0]:set_lengths[2][1]]

for noise in noise_list:

    #augment the enhanced array
    for i,m in product([0,1,3],xrange(100)):
        #i is the dataset
        #for each dataset we produce a 100 noise_arrays
        uL=set_lengths[i]
        temp_data=array_data[uL[0]:uL[1]]
        #generate an array the size of the current sub array, to be added.
        noise_array=np.array([[temp_data[k,0]]+[temp_data[k,j]+np.random.uniform(-noise,noise) for j in xrange(1,5)] for k in xrange(len(temp_data))])
    
        #print noise_array
        #print enh_array
        enh_array=np.concatenate((enh_array,noise_array),axis=0)
        #print enh_array
        
    #Data normalization


    #print enh_array[:3]
    #print enh_array[1:3]
    #print 'its length',enh_array.shape
    # a custom built function normalizes along the column. The columns are then put back together
    enh_array=np.column_stack((normalizer(enh_array[1:,0]),normalizer(enh_array[1:,1]),normalizer(enh_array[1:,2]),normalizer(enh_array[1:,3]),normalizer(enh_array[1:,4])))

    #print enh_array[:2]
    #print 'its length once normalized',enh_array.shape
    #check later this is NOT DONE


    #build anbd populate datasets
    ds1 = SupervisedDataSet(5, 3)
    ds2 = SupervisedDataSet(4, 3)
    r_lengths=[[i,i+13] for i in xrange(0,13*100*3,13)]
    #print r_lengths

    for j in r_lengths:
        temp_data=enh_array[j[0]:j[1]]
        
        for k in xrange(len(temp_data)-1):

            for l in xrange(k+1,len(temp_data)):
                ds1.addSample((temp_data[k][0],temp_data[l][1]-temp_data[k][1],temp_data[k][2],temp_data[k][3],temp_data[k][4]), (temp_data[l][2]-temp_data[k][2],temp_data[l][3]-temp_data[k][3],temp_data[l][4]-temp_data[k][4]))
                #in this data set we add the illumination factor, the chemical concentrations at a certain time
                #one of the inputs is the difference between current time and the time at step we want as output
                #the output is only the chemical concentrations

    #dataset without time

    for j in r_lengths:
        temp_data=enh_array[j[0]:j[1]]
        
        for k in xrange(len(temp_data)-1):
            ds2.addSample((temp_data[k][0],temp_data[k][2],temp_data[k][3],temp_data[k][4]), (temp_data[k+1][2]-temp_data[k][2],temp_data[k+1][3]-temp_data[k][3],temp_data[k+1][4]-temp_data[k][4]))
            #in this one only 4 inputs.

    #both types of ANN will be run, and with 1 and 2 hidden layers

    net1 = buildNetwork(5,
                           10, #number of hidden units
                           3,
                           bias = True,
                           hiddenclass = SigmoidLayer,
                           outclass = LinearLayer
                        )

    net2 = buildNetwork(4,
                           20, # number of hidden units
                           3,
                           bias = True,
                           hiddenclass = SigmoidLayer,
                           outclass = LinearLayer
                        )

    net3 = buildNetwork(5,
                           15,
                           15, # number of hidden units
                           3,
                           bias = True,
                           hiddenclass = SigmoidLayer,
                           outclass = LinearLayer
                        )

    net4 = buildNetwork(4,
                           15, # number of hidden units
                           15, # number of hidden units
                           3,
                           bias = True,
                           hiddenclass = SigmoidLayer,
                           outclass = LinearLayer
                        )
    #initialize the structures
    net1.randomize()
    net1.sortModules()
    net2.randomize()
    net2.sortModules()
    net3.randomize()
    net3.sortModules()
    net4.randomize()
    net4.sortModules()
    #create trainers
    trainer1 = BackpropTrainer(net1, ds1, verbose = False)
    trainer2 = BackpropTrainer(net2, ds2, verbose = False)
    trainer3 = BackpropTrainer(net3, ds1, verbose = False)
    trainer4 = BackpropTrainer(net4, ds2, verbose = False)
    #train for set amount of epochs
    trainer1.trainEpochs(nEpochs)
    trainer2.trainEpochs(nEpochs)
    trainer3.trainEpochs(nEpochs)
    trainer4.trainEpochs(nEpochs)


    #test against the cross validation set

    sim_net1=[]
    sim_net2=[]
    sim_net3=[]
    sim_net4=[]
    #cross_val_set
    #Simulation for Network 1, 1 Hidden.
    '''
    for k in xrange(len(cross_val_set)-1):

        ansK=[]
        for l in xrange(k+1,len(temp_data)):
            ans=net1.activate((cross_val_set[k][0],cross_val_set[l][1]-cross_val_set[k][1],cross_val_set[k][2],cross_val_set[k][3],cross_val_set[k][4]))
            ansK.append([abs(cross_val_set[l][2]-(cross_val_set[k][2]+ans[0])),abs(temp_data[l][3]-(temp_data[k][3]+ans[1])),abs(temp_data[l][4]-(temp_data[k][4]+ans[2]))])
        sim_net1.append(np.mean(ansK,axis=0))

    print 'For network 1 at hidden layer strata ',nH,' run for ',nE,' epochs the error is ', error1

    #simulation for Network 2, 1 Hidden.

    for j in set_lengths:
        temp_data=array_data[j[0]:j[1]]
        #sim_net2.append((temp_data[0][2],temp_data[0][3],temp_data[0][4]))
        ansK=[]       
        for k in xrange(len(temp_data)-1):
            ans=net2.activate((temp_data[k][0],temp_data[k][2],temp_data[k][3],temp_data[k][4]))
            ansK.append([abs(temp_data[k+1][2]-(temp_data[k][2]+ans[0])),abs(temp_data[k+1][3]-(temp_data[k][3]+ans[1])),abs(temp_data[k+1][4]-(temp_data[k][4]+ans[2]))])
        sim_net2.append(np.mean(ansK,axis=0))

    #get  error for each variable difference. Since they are already all normalized, no std
    #maximum error

    arrays=[['Real','N1','N2','N3','N4'],['DCW', 'nitrate', 'lutein']]
    tuples=list(zip(*arrays))
    index = pd.MultiIndex.from_tuples(tuples, names=['Network', 'Conc'])
    alpha= pd.concat([pd.DataFrame(cross_val_set[:,2:]),pd.DataFrame(sim_net1),pd.DataFrame(sim_net2),pd.DataFrame(sim_net3),pd.DataFrame(sim_net4)], axis=1)
    #save to csv
    alpha.to_csv('Lutein_NN_simulation_'+str(noise)+'_noise'+'.csv') 
    '''
print 'Work completed. Check out the csv for best simulation'

