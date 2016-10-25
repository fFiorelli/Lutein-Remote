import pylab
from pylab import*
import matplotlib.pyplot as plt
import pybrain
from pybrain.tools.xml.networkreader import NetworkReader
import ArrangeDataLuteinMultyDelta
import DataLuteinMultyDelta
import PredictionDataLutein

# HL_6 very bad
# HL_66 much better than HL_6 and HL_66_500 HL_666_300
# HL_666_500 looks promising...more epochs

# In this file a network that has been trained is exported the rest is simply to plot againts cross validation data
# The MULTY in this file means that the data is replicated by artificially creating 100 other experimental runs by adding noise.
# I also compute the deltas once the functions are normilized. Here we just calculate the delta of the function instead of the whole function value.

net1 = NetworkReader.readFrom('net_Lutein_Multyin_100_delta_86_epoch100.xml') 

# plotting and prediction

# List of results
x_result = []
n_result = []
lu_result = []

dx_result = []
dn_result = []
dlu_result = []
# DB is double blind
x_resultDB = []
n_resultDB = []
lu_resultDB = []

dx_resultDB = []
dn_resultDB = []
dlu_resultDB = []

for i in range(0,len(PredictionDataLutein.xtotal)):
	ans = net1.activate((PredictionDataLutein.xtotal[i],PredictionDataLutein.ntotal[i],PredictionDataLutein.lutotal[i],PredictionDataLutein.litotal[i]))
	dx_result.append(ans[0])
	dn_result.append(ans[1])
	dlu_result.append(ans[2])

	x_result.append(PredictionDataLutein.xtotal[i]+ans[0])
	n_result.append(PredictionDataLutein.ntotal[i]+ans[1])
	lu_result.append(PredictionDataLutein.lutotal[i]+ans[2])


		

for i in range(0,len(PredictionDataLutein.xtotal)):
	if (i == 0 or PredictionDataLutein.xtotal[i]<PredictionDataLutein.xtotal[i-1]):
		ans = net1.activate((PredictionDataLutein.xtotal[i],PredictionDataLutein.ntotal[i],PredictionDataLutein.lutotal[i],PredictionDataLutein.litotal[i]))

		#x_resultDB.append(PredictionDataLutein.xtotal[i])
		#n_resultDB.append(PredictionDataLutein.ntotal[i])
		#lu_resultDB.append(PredictionDataLutein.lutotal[i])


		x_resultDB.append(PredictionDataLutein.xtotal[i]+ans[0])
		n_resultDB.append(PredictionDataLutein.ntotal[i]+ans[1])
		lu_resultDB.append(PredictionDataLutein.lutotal[i]+ans[2])

	else:
		ans = net1.activate((x_resultDB[-1],n_resultDB[-1],lu_resultDB[-1],PredictionDataLutein.litotal[i]))

		x_resultDB.append(x_resultDB[-1]+ans[0])
		n_resultDB.append(n_resultDB[-1]+ans[1])
		lu_resultDB.append(lu_resultDB[-1]+ans[2])

#print "DB = ",len(x_resultDB)
#print "PC norm = ",len(ArrangeDataPCMultyDelta.x_norm[0][1:5])

x_mean =  1.28170725722
n_mean =  58.5920227288
lu_mean =  2.05715249394
li_mean =  310.102398847

x_std =  0.71163393916
n_std =  53.746066212
lu_std =  1.22195011761
li_std =  135.074901175

x_Exp = (PredictionDataLutein.xtotal[1:])[:]
n_Exp = (PredictionDataLutein.ntotal[1:])[:]
lu_Exp = (PredictionDataLutein.lutotal[1:])[:]

for data in range(0,len(x_result)):
  x_result[data] = x_result[data] * x_std + x_mean
  x_resultDB[data] = x_resultDB[data] * x_std + x_mean
  x_Exp[data] = x_Exp[data] * x_std + x_mean
  n_result[data] = n_result[data] * n_std + n_mean
  n_resultDB[data] = n_resultDB[data] * n_std + n_mean
  n_Exp[data] = n_Exp[data] * n_std + n_mean
  lu_result[data] = lu_result[data] * lu_std + lu_mean
  lu_resultDB[data] = lu_resultDB[data] * lu_std + lu_mean
  lu_Exp[data] = lu_Exp[data] * lu_std + lu_mean

print "x_result = ",x_result
print "n_result = ",n_result
print "lu_result = ",lu_result
print "x_resultDB = ",x_resultDB
print "n_resultDB = ",n_resultDB
print "lu_resultDB = ",lu_resultDB


fig=matplotlib.pyplot.figure(figsize=(18,4))

plt.subplot2grid((2,6),(0,0),colspan=2)
plt.plot(x_result)
plt.plot(x_Exp)
plt.ylabel('x',rotation= 360,fontsize=15)
plt.xlabel('time',fontsize=15)

plt.subplot2grid((2,6),(0,2),colspan=2)
plt.plot(n_result)
plt.plot(n_Exp)
plt.ylabel('n',rotation= 360,fontsize=15)
plt.xlabel('time',fontsize=15)

plt.subplot2grid((2,6),(0,4),colspan=2)
plt.plot(lu_result)
plt.plot(lu_Exp)
plt.ylabel('lu',rotation= 360,fontsize=15)
plt.xlabel('time',fontsize=15)

#

plt.subplot2grid((2,6),(1,0),colspan=2)
plt.plot(x_resultDB)
plt.plot(x_Exp)
plt.ylabel('x DB',rotation= 360,fontsize=15)
plt.xlabel('time',fontsize=15)

plt.subplot2grid((2,6),(1,2),colspan=2)
plt.plot(n_resultDB)
plt.plot(n_Exp)
plt.ylabel('n DB',rotation= 360,fontsize=15)
plt.xlabel('time',fontsize=15)

plt.subplot2grid((2,6),(1,4),colspan=2)
plt.plot(lu_resultDB)
plt.plot(lu_Exp)
plt.ylabel('lu DB',rotation= 360,fontsize=15)
plt.xlabel('time',fontsize=15)


subplots_adjust(left=0.05,right=0.95,top=0.9,bottom=0.14,wspace=0.7)

plt.show()
