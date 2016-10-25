import pylab
from pylab import*
import matplotlib.pyplot as plt
import pybrain
from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import TanhLayer
from pybrain.structure import LinearLayer
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
import ArrangeDataLuteinMultyDelta
import DataLuteinMultyDelta # needed for DB initial values
from pybrain.tools.xml.networkwriter import NetworkWriter
from pybrain.tools.xml.networkreader import NetworkReader

# here the ANN is built and stored half this file is simply to plot the trainning vs its data
# The MULTY in this file means that the data is replicated by artificially creating 100 (or so) other experimental runs by adding noise.
# I also compute the deltas once the functions are normilized. Here we just calculate the delta of the function instead of the whole function value.

# small deviation but might become large as time passes by

# Build network:

net1 = buildNetwork(4, 8,6, 3, hiddenclass=TanhLayer, bias=True)
net1.randomize()
net1.sortModules()

# hidden layer is TanhLayer function type
# has bias

# Say the number of inputs and outputs of data set
ds = SupervisedDataSet(4,3)
# Input the data sets
for sample in range(0,(len(ArrangeDataLuteinMultyDelta.InLuteinMultyDelta))):
	ds.addSample(ArrangeDataLuteinMultyDelta.InLuteinMultyDelta[sample],ArrangeDataLuteinMultyDelta.OutLuteinMultyDelta[sample])
print "trainning data ..."
# Train the data
trainer = BackpropTrainer(net1,ds)
#trainer.trainUntilConvergence()
trainer.trainEpochs(100)
#trainer.train()

NetworkWriter.writeToFile(net1, 'net_Lutein_Multyin_100_delta_86_epoch100.xml')

# Loop to train in a loop until best quality is obtained

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

for i in range(0,len(ArrangeDataLuteinMultyDelta.x_norm[0])-1):
	ans = net1.activate(ArrangeDataLuteinMultyDelta.InLuteinMultyDelta[i])
	dx_result.append(ans[0])
	dn_result.append(ans[1])
	dlu_result.append(ans[2])

	x_result.append(ArrangeDataLuteinMultyDelta.InLuteinMultyDelta[i][0]+ans[0])
	n_result.append(ArrangeDataLuteinMultyDelta.InLuteinMultyDelta[i][1]+ans[1])
	lu_result.append(ArrangeDataLuteinMultyDelta.InLuteinMultyDelta[i][2]+ans[2])

for i in range(0,4):

  if i == 0:
    ans = net1.activate((ArrangeDataLuteinMultyDelta.x_norm[0][i],ArrangeDataLuteinMultyDelta.n_norm[0][i],ArrangeDataLuteinMultyDelta.lu_norm[0][i],ArrangeDataLuteinMultyDelta.li_norm[0][i]))
    dx_resultDB.append(ans[0])
    dn_resultDB.append(ans[1])
    dlu_resultDB.append(ans[2])

    x_resultDB.append(ArrangeDataLuteinMultyDelta.x_norm[0][i]+ans[0])
    n_resultDB.append(ArrangeDataLuteinMultyDelta.n_norm[0][i]+ans[1])
    lu_resultDB.append(ArrangeDataLuteinMultyDelta.lu_norm[0][i]+ans[2])

  else:
    ans = net1.activate((x_resultDB[-1],n_resultDB[-1],lu_resultDB[-1],ArrangeDataLuteinMultyDelta.InLuteinMultyDelta[i][3]))
    dx_resultDB.append(ans[0])
    dn_resultDB.append(ans[1])
    dlu_resultDB.append(ans[2])

    x_resultDB.append(x_resultDB[-1]+ans[0])
    n_resultDB.append(n_resultDB[-1]+ans[1])
    lu_resultDB.append(lu_resultDB[-1]+ans[2])

#print "DB = ",len(x_resultDB)
#print "PC norm = ",len(ArrangeDataLuteinMultyDelta.x_norm[0][1:5])


