import DataLuteinMultyDelta
import numpy
# This file normilized the data and puts it in a format suitable to input in the neural network
# The MULTY in this file means that the data is replicated by artificially creating 100 other experimental runs by adding noise.
# I also compute the deltas once the functions are normilized. Here we just calculate the delta of the function instead of the whole function value.
#import matplotlib.pyplot as plt

# -- mean and std -- #
# get the      # 
# mean and std #
x_mean = 0;x_std = 0;
n_mean = 0;n_std = 0;
lu_mean = 0;lu_std = 0;
li_mean = 0;li_std = 0;

x_big_list = []
n_big_list = []
lu_big_list = []
li_big_list = []

# Given that we replicated the lists in the last Data page, now we need to create a big list to create a mean and an std from all of them

for run in range(0,len(DataLuteinMultyDelta.x)):
	x_big_list = x_big_list + DataLuteinMultyDelta.x[run]
	n_big_list = n_big_list + DataLuteinMultyDelta.n[run]
	lu_big_list = lu_big_list + DataLuteinMultyDelta.lu[run]
	li_big_list = li_big_list + DataLuteinMultyDelta.li[run]

# mean and std of all the lists

x_mean = sum(x_big_list)/float(len(x_big_list))
n_mean = sum(n_big_list)/float(len(n_big_list))
lu_mean = sum(lu_big_list)/float(len(lu_big_list))
li_mean = sum(li_big_list)/float(len(li_big_list))

x_std = numpy.std(x_big_list)
n_std = numpy.std(n_big_list)
lu_std = numpy.std(lu_big_list)
li_std = numpy.std(li_big_list)

# Measures we are using

x_mean =  1.28170725722
n_mean =  58.5920227288
lu_mean =  2.05715249394
li_mean =  310.102398847

x_std =  0.71163393916
n_std =  53.746066212
lu_std =  1.22195011761
li_std =  135.074901175


# -- normaliZe -- #
# normaliZe # 
# the data  #

x_norm = []
n_norm = []
lu_norm = []
li_norm = []
for run in range(0,len(DataLuteinMultyDelta.x)):
	x_norm_temp = []
	n_norm_temp = []
	lu_norm_temp = []
	li_norm_temp = []
	for var in range(0,len(DataLuteinMultyDelta.x[run])):
		x_norm_temp.append((DataLuteinMultyDelta.x[run][var]-x_mean)/float(x_std))
		n_norm_temp.append((DataLuteinMultyDelta.n[run][var]-n_mean)/float(n_std))
		lu_norm_temp.append((DataLuteinMultyDelta.lu[run][var]-lu_mean)/float(lu_std))
		li_norm_temp.append((DataLuteinMultyDelta.li[run][var]-li_mean)/float(li_std))
	x_norm.append(x_norm_temp)
	n_norm.append(n_norm_temp)
	lu_norm.append(lu_norm_temp)
	li_norm.append(li_norm_temp)

# -- compute deltas -- #

dlu_norm = []
dx_norm = []
dn_norm = []

for run in range(0,len(lu_norm)):
	dlu_norm_temp = []
	dn_norm_temp = []
	dx_norm_temp = []

	for var in range(0,len(lu_norm[run])-1):
		dlu_norm_temp.append(float(lu_norm[run][var+1]-lu_norm[run][var]))
		dx_norm_temp.append(float(x_norm[run][var+1]-x_norm[run][var]))
		dn_norm_temp.append(float(n_norm[run][var+1]-n_norm[run][var]))

	dlu_norm.append(dlu_norm_temp)
	dx_norm.append(dx_norm_temp)
	dn_norm.append(dn_norm_temp)


# So that each x_norm has same size as dx_norm 
for run in range(0,len(lu_norm)):
  x_norm[run] = x_norm[run][:-1]
  n_norm[run] = n_norm[run][:-1]
  lu_norm[run] = lu_norm[run][:-1]
  li_norm[run] = li_norm[run][:-1]

# -- arrange data -- #
# arrange data        #
# for neural networks #
# 1 in 1 out :(       # 

InLuteinMultyDelta = []
OutLuteinMultyDelta = []
# 1 in 1 out
for run in range(0,len(n_norm)):
	for v in range(0,len(n_norm[run])-1):
		if  x_norm[run][v] <= x_norm[run][v+1]:
			InLuteinMultyDelta.append((x_norm[run][v],n_norm[run][v],lu_norm[run][v],li_norm[run][v]))
			OutLuteinMultyDelta.append((dx_norm[run][v],dn_norm[run][v],dlu_norm[run][v]))

#print "x_mean = ",x_mean
#print "n_mean = ",n_mean
#print "lu_mean = ",lu_mean
#print "li_mean = ",li_mean
#print ""
#print "x_std = ",x_std
#print "n_std = ",n_std
#print "lu_std = ",lu_std
#print "li_std = ",li_std






