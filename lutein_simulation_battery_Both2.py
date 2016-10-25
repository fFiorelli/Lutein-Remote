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
from utilities import de_normalizer
from utilities import standardizer
from utilities import de_standardizer
import sys

#columns tags
lista_col=['Illumination umol/m2/s','Time (h)', 'DCW (mg/l)', 'nitrate (mg/l)', 'lutein content (mg/l)']
lista_col1=['Illumination','Time', 'DCW', 'nitrate', 'lutein']
lista_col2=['Illumination','Time', 'DCW', 'nitrate', 'lutein','NFlowrate']
lista_col3=['Illumination', 'DCW', 'nitrate', 'lutein','NFlowrate']
#folders from which to pick saved networks and save data files
net_fold='networks/'
save_fold='data/'
#import as Pandas Data the excel file
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
arr_temp=np.concatenate((arr_test,arr_val),axis=0)

arr_tempA=np.column_stack((normalizer(standardizer(arr_temp[:,0])),normalizer(standardizer(arr_temp[:,1])),normalizer(standardizer(arr_temp[:,2])),normalizer(standardizer(arr_temp[:,3])),normalizer(standardizer(arr_temp[:,4])),normalizer(standardizer(arr_temp[:,5]))))

arr_testT,arr_valT=arr_tempA[:len(arr_test)], arr_tempA[len(arr_test):]

#the four sets of experiments are given separately. These are their start and end points
sLht=12
#third set is separated
#an enchanced array that will contain the noisy data

#debug. Functions for scaling and rescaling seem to work fine
#print arr_temp[:,2]
#print de_standardizer(de_normalizer(arr_tempA[:,2],standardizer(arr_temp[:,2])),arr_temp[:,2])
#sys.exit()
#different deltaT.Normalized. Should be 12,24,36,72
#print cross_val


#Open networks

network_2=NetworkReader.readFrom(net_fold+ 'network_Type2H1_Both.xml')
network_4=NetworkReader.readFrom(net_fold+ 'network_Type2H2_Both.xml')
#normalize the cross validation set

#normalize the other data with custom function. Remove cross validation and rearrange


#print pd.DataFrame(array_data,columns=lista_col1)


#------------------------------------------Test on  cross validation set 3--------------------------------------------------------------------
#Use arr_val
#beta is the standardized-normalized dataframe
beta=pd.DataFrame(arr_valT,columns=lista_col2)
beta.drop('Time',axis=1, inplace=True)
#theta is the pre-treatment dataframe
theta=pd.DataFrame(arr_val,columns=lista_col2)
theta.drop('Time',axis=1, inplace=True)
#for each network do the round
#do the k
#this takes out the cross validation set for ease of use.
beta_Val=beta.values
theta_Val=theta.values
sim_net2=[beta_Val[0]]

#Predict from Experimental point
#simulation for Network 2, 1 Hidden.
for j in xrange(11):
    ans=network_2.activate((beta_Val[j]))
    ansK=[beta_Val[j,0],beta_Val[j][1]+ans[0],beta_Val[j][2]+ans[1],beta_Val[j][3]+ans[2],beta_Val[j+1][4]]
    sim_net2=np.append(sim_net2,[ansK],axis=0)

sim_net2=np.append(sim_net2,[beta_Val[12]],axis=0)
for j in xrange(12,23):
    ans=network_2.activate((beta_Val[j]))
    ansK=[beta_Val[j,0],beta_Val[j][1]+ans[0],beta_Val[j][2]+ans[1],beta_Val[j][3]+ans[2],beta_Val[j+1][4]]
    sim_net2=np.append(sim_net2,[ansK],axis=0)

#denormalize and rescale to real size
print sim_net2[:,3]
print standardizer(theta_Val[:,3])
print de_normalizer(sim_net2[:,3],standardizer(theta_Val[:,3]))
print de_standardizer(de_normalizer(sim_net2[:,3],standardizer(theta_Val[:,3])),theta_Val[:,3])
print theta_Val[:,3]
#sys.exit()

sim_deNorm2=np.column_stack((
sim_net2[:,0]
,de_standardizer(de_normalizer(sim_net2[:,1],standardizer(theta_Val[:,1])),theta_Val[:,1])
,de_standardizer(de_normalizer(sim_net2[:,2],standardizer(theta_Val[:,2])),theta_Val[:,2])
,de_standardizer(de_normalizer(sim_net2[:,3],standardizer(theta_Val[:,3])),theta_Val[:,3])
,de_standardizer(de_normalizer(sim_net2[:,4],standardizer(theta_Val[:,4])),theta_Val[:,4])))

#de_standardizer(de_normalizer(arr_tempA[:,2],standardizer(arr_temp[:,2])),arr_temp[:,2])

temp2=pd.DataFrame(sim_net2,columns=lista_col3)
temp2a=pd.DataFrame(sim_deNorm2,columns=lista_col3)

beta=pd.concat([beta,temp2],axis=1,keys=['Experimental','Simulated']) 
theta=pd.concat([theta,temp2a],axis=1,keys=['Experimental','Simulated']) 
#save
beta.to_csv(save_fold+'Lutein_NN_Type2H1_CrossVal_Both_ExpTraj.csv')
theta.to_csv(save_fold+'Lutein_NN_Type2H1_CrossVal_Both_ExpTraj_Rescale.csv')
#overwrite
beta=pd.DataFrame(arr_valT,columns=lista_col2)
beta.drop('Time',axis=1, inplace=True)
theta=pd.DataFrame(arr_val,columns=lista_col2)
theta.drop('Time',axis=1, inplace=True)

#simulation for Network 2, 2 Hidden.
sim_net4=[beta_Val[0]]
for j in xrange(11):
    ans=network_4.activate((beta_Val[j]))
    ansK=[beta_Val[j,0],beta_Val[j][1]+ans[0],beta_Val[j][2]+ans[1],beta_Val[j][3]+ans[2],beta_Val[j+1][4]]
    sim_net4=np.append(sim_net4,[ansK],axis=0)

sim_net4=np.append(sim_net4,[beta_Val[12]],axis=0)
for j in xrange(12,23):
    ans=network_4.activate((beta_Val[j]))
    ansK=[beta_Val[j,0],beta_Val[j][1]+ans[0],beta_Val[j][2]+ans[1],beta_Val[j][3]+ans[2],beta_Val[j+1][4]]
    sim_net4=np.append(sim_net4,[ansK],axis=0)

#denormalize and rescale to real size
#Have to do it in two pieces
sim_deNorm4=np.column_stack((
sim_net4[:,0]
,de_standardizer(de_normalizer(sim_net4[:,1],standardizer(theta_Val[:,1])),theta_Val[:,1])
,de_standardizer(de_normalizer(sim_net4[:,2],standardizer(theta_Val[:,2])),theta_Val[:,2])
,de_standardizer(de_normalizer(sim_net4[:,3],standardizer(theta_Val[:,3])),theta_Val[:,3])
,de_standardizer(de_normalizer(sim_net4[:,4],standardizer(theta_Val[:,4])),theta_Val[:,4])))


temp4=pd.DataFrame(sim_net4,columns=lista_col3)
temp4a=pd.DataFrame(sim_deNorm4,columns=lista_col3)

beta=pd.concat([beta,temp4],axis=1,keys=['Experimental','Simulated'])  
theta=pd.concat([theta,temp4a],axis=1,keys=['Experimental','Simulated'])   
#save
beta.to_csv(save_fold+'Lutein_NN_Type2H2_CrossVal_Both_ExpTraj.csv')
theta.to_csv(save_fold+'Lutein_NN_Type2H2_CrossVal_Both_ExpTraj_Rescale.csv')
#overwrite
beta=pd.DataFrame(arr_valT,columns=lista_col2)
beta.drop('Time',axis=1, inplace=True)
theta=pd.DataFrame(arr_val,columns=lista_col2)
theta.drop('Time',axis=1, inplace=True)

#Predict from Simulation point
#simulation for Network 2, 1 Hidden.
sim_net2=[beta_Val[0]]
for j in xrange(11):
    ans=network_2.activate((sim_net2[j]))
    ansK=[beta_Val[j,0],sim_net2[j][1]+ans[0],sim_net2[j][2]+ans[1],sim_net2[j][3]+ans[2],beta_Val[j+1][4]]
    sim_net2=np.append(sim_net2,[ansK],axis=0)

sim_net2=np.append(sim_net2,[beta_Val[12]],axis=0)
for j in xrange(12,23):
    ans=network_2.activate((sim_net2[j]))
    ansK=[beta_Val[j,0],sim_net2[j][1]+ans[0],sim_net2[j][2]+ans[1],sim_net2[j][3]+ans[2],beta_Val[j+1][4]]
    sim_net2=np.append(sim_net2,[ansK],axis=0)

#denormalize and rescale to real size
#Have to do it in two pieces
sim_deNorm2=np.column_stack((
sim_net2[:,0]
,de_standardizer(de_normalizer(sim_net2[:,1],standardizer(theta_Val[:,1])),theta_Val[:,1])
,de_standardizer(de_normalizer(sim_net2[:,2],standardizer(theta_Val[:,2])),theta_Val[:,2])
,de_standardizer(de_normalizer(sim_net2[:,3],standardizer(theta_Val[:,3])),theta_Val[:,3])
,de_standardizer(de_normalizer(sim_net2[:,4],standardizer(theta_Val[:,4])),theta_Val[:,4])))

temp2=pd.DataFrame(sim_net2,columns=lista_col3)
temp2a=pd.DataFrame(sim_deNorm2,columns=lista_col3)

beta=pd.concat([beta,temp2],axis=1,keys=['Experimental','Simulated'])
theta=pd.concat([theta,temp2a],axis=1,keys=['Experimental','Simulated'])     
#save
beta.to_csv(save_fold+'Lutein_NN_Type2H1_CrossVal_Both_SimTraj.csv')
theta.to_csv(save_fold+'Lutein_NN_Type2H1_CrossVal_Both_SimTraj_Rescale.csv')
#overwrite
beta=pd.DataFrame(arr_valT,columns=lista_col2)
beta.drop('Time',axis=1, inplace=True)
theta=pd.DataFrame(arr_val,columns=lista_col2)
theta.drop('Time',axis=1, inplace=True)

#simulation for Network 2, 2 Hidden.
sim_net4=[beta_Val[0]]
for j in xrange(11):
    ans=network_4.activate((sim_net4[j]))
    ansK=[beta_Val[j,0],sim_net4[j][1]+ans[0],sim_net4[j][2]+ans[1],sim_net4[j][3]+ans[2],beta_Val[j+1][4]]
    sim_net4=np.append(sim_net4,[ansK],axis=0)

sim_net4=np.append(sim_net4,[beta_Val[12]],axis=0)
for j in xrange(12,23):
    ans=network_4.activate((sim_net4[j]))
    ansK=[beta_Val[j,0],sim_net4[j][1]+ans[0],sim_net4[j][2]+ans[1],sim_net4[j][3]+ans[2],beta_Val[j+1][4]]
    sim_net4=np.append(sim_net4,[ansK],axis=0)

#denormalize and rescale to real size
#Have to do it in two pieces
sim_deNorm4=np.column_stack((
sim_net4[:,0]
,de_standardizer(de_normalizer(sim_net4[:,1],standardizer(theta_Val[:,1])),theta_Val[:,1])
,de_standardizer(de_normalizer(sim_net4[:,2],standardizer(theta_Val[:,2])),theta_Val[:,2])
,de_standardizer(de_normalizer(sim_net4[:,3],standardizer(theta_Val[:,3])),theta_Val[:,3])
,de_standardizer(de_normalizer(sim_net4[:,4],standardizer(theta_Val[:,4])),theta_Val[:,4])))



temp4=pd.DataFrame(sim_net4,columns=lista_col3)
temp4a=pd.DataFrame(sim_deNorm4,columns=lista_col3)

beta=pd.concat([beta,temp4],axis=1,keys=['Experimental','Simulated'])
theta=pd.concat([theta,temp4a],axis=1,keys=['Experimental','Simulated'])   
#save
beta.to_csv(save_fold+'Lutein_NN_Type2H2_CrossVal_Both_SimTraj.csv')
theta.to_csv(save_fold+'Lutein_NN_Type2H2_CrossVal_Both_SimTraj_Rescale.csv')
#overwrite
beta=pd.DataFrame(arr_valT,columns=lista_col2)
beta.drop('Time',axis=1, inplace=True)
theta=pd.DataFrame(arr_val,columns=lista_col2)
theta.drop('Time',axis=1, inplace=True)

