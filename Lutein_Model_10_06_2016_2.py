import numpy as np
import pylab
from pylab import*
from coopr.pyomo import *
#from coopr.opt import SolverFactory
import matplotlib.pyplot as plt

# we can add piece-wise initial conditions to make it better approx.

model=ConcreteModel()

scalar = 5
Elements=12 * scalar # I will add an Element 0
CollocationPoints=3
Final_time = 144.0
time_list=[i*Final_time/(Elements+1) for i in range(0,Elements+1)]
Indexing=[[i for i in range(0,CollocationPoints+1)] for i in range(1,Elements+1)]
ListElem=range(0,Elements+1)
ListPoints=range(1,CollocationPoints+1)
A=[[0.19681543373107852, -0.06553540256509917, 0.023770968834020696], [0.3944242884670843, 0.2920734924941083, -0.04154878096119264], [0.3764030427860929, 0.5124858834390942, 0.11111107377481302]]# esto esta escrito como columna1, columna2...

# Input Fin
Fin = [[] for i in range(0,Elements+1)]

for i in range(0,(5*scalar)+1):
  for j in range(0,CollocationPoints+1):
    Fin[i].append(0.0)

for i in range((5*scalar)+1,Elements+1):
  for j in range(0,CollocationPoints+1):
    Fin[i].append(42.5/1.0)

# x_150dot ----------
x_150lb= 0.1757
x_150ub= 1.44
x_150innit = {}

for i in range(0,Elements+1):
  for j in range(0,CollocationPoints+1):
    x_150innit[(i,j)]= x_150lb + (i+0.25*j)*(x_150ub-x_150lb)/float(Elements+1)

x_150dotinnit = (x_150ub-x_150lb)/float(Elements+1)

# x_300dot ----------
x_300lb= 0.077
x_300ub= 2.21
x_300innit = {}

for i in range(0,Elements+1):
  for j in range(0,CollocationPoints+1):
    x_300innit[(i,j)]= x_300lb + (i+0.25*j)*(x_300ub-x_300lb)/float(Elements+1)

x_300dotinnit = (x_300ub-x_300lb)/float(Elements+1)

# x_450dot ----------
x_450lb= 0.077
x_450ub= 2.28
x_450innit = {}

for i in range(0,Elements+1):
  for j in range(0,CollocationPoints+1):
    x_450innit[(i,j)]= x_450lb + (i+0.25*j)*(x_450ub-x_450lb)/float(Elements+1) # el + 1 viene por el 0.25*j

x_450dotinnit = (x_450ub-x_450lb)/float(Elements+1)

# x_600dot ----------
x_600lb= 0.077
x_600ub= 2.69
x_600innit = {}

for i in range(0,Elements+1):
  for j in range(0,CollocationPoints+1):
    x_600innit[(i,j)]= x_600lb + (i+0.25*j)*(x_600ub-x_600lb)/float(Elements+1) # el + 1 viene por el 0.25*j

x_600dotinnit = (x_600ub-x_600lb)/float(Elements+1)

# n_150dot ----------
n_150innit = {}
n_150dotinnit = {}
# decrease
n_150lb= 783.2
n_150ub= 460.4


for i in range(0,6* scalar + 1):
  for j in range(0,CollocationPoints+1):
    n_150innit[(i,j)]= n_150lb + (i+0.25*j)*(n_150ub-n_150lb)/float(6* scalar + 1)
    n_150dotinnit [(i,j)]= (n_150ub-n_150lb)/float(6* scalar + 1)

# increase
n_150lb= 460.4
n_150ub= 2614.3

for i in range(6* scalar + 1, Elements + 1):
  for j in range(0,CollocationPoints+1):
    n_150innit[(i,j)]= n_150lb + (i+0.25*j)*(n_150ub-n_150lb)/float(Elements+ 1)
    n_150dotinnit[(i,j)]= (n_150ub-n_150lb)/float(Elements + 1)


# n_300dot ----------
n_300innit = {}
n_300dotinnit = {}

# decrease
n_300lb= 783.5
n_300ub= 517.7

for i in range(0,6* scalar + 1):
  for j in range(0,CollocationPoints+1):
    n_300innit[(i,j)]= n_300lb + (i+0.25*j)*(n_300ub-n_300lb)/float(6* scalar + 1)
    n_300dotinnit[(i,j)] = (n_300ub-n_300lb)/float(6* scalar + 1)

# increase
n_300lb= 517.7
n_300ub= 2608.9

for i in range(6* scalar + 1, Elements + 1):
  for j in range(0,CollocationPoints+1):
    n_300innit[(i,j)]= n_300lb + (i+0.25*j)*(n_300ub-n_300lb)/float(Elements + 1)
    n_300dotinnit[(i,j)] = (n_300ub-n_300lb)/float(Elements + 1)

# n_450dot ----------
n_450innit = {}
n_450dotinnit = {}

# decrease
n_450lb= 784.4
n_450ub= 335.8

for i in range(0,6* scalar + 1):
  for j in range(0,CollocationPoints+1):
    n_450innit[(i,j)]= n_450lb + (i+0.25*j)*(n_450ub-n_450lb)/float(6* scalar + 1) # el + 1 viene por el 0.25*j
    n_450dotinnit[(i,j)] = (n_450ub-n_450lb)/float(6* scalar + 1)

# increase
n_450lb= 335.8
n_450ub= 1885.1

for i in range(6* scalar + 1,Elements + 1):
  for j in range(0,CollocationPoints+1):
    n_450innit[(i,j)]= n_450lb + (i+0.25*j)*(n_450ub-n_450lb)/float(Elements + 1) 
    n_450dotinnit[(i,j)] = (n_450ub-n_450lb)/float(Elements + 1)

# n_600dot ----------
n_600innit = {}
n_600dotinnit = {}

# decrease
n_600lb= 783.3
n_600ub= 215.0

for i in range(0,6* scalar + 1):
  for j in range(0,CollocationPoints+1):
    n_600innit[(i,j)]= n_600lb + (i+0.25*j)*(n_600ub-n_600lb)/float(6* scalar + 1) 
    n_600dotinnit[(i,j)] = (n_600ub-n_600lb)/float(6* scalar + 1)

# increase
n_600lb= 215.0
n_600ub= 1753.6

for i in range(6* scalar + 1,Elements + 1):
  for j in range(0,CollocationPoints+1):
    n_600innit[(i,j)]= n_600lb + (i+0.25*j)*(n_600ub-n_600lb)/float(Elements + 1) 
    n_600dotinnit[(i,j)] = (n_600ub-n_600lb)/float(Elements + 1)

# lu_150dot ----------
lu_150innit = {}
lu_150dotinnit = {}

# increase 1
lu_150lb= 0.0
lu_150ub= 0.92

for i in range(0 ,2* scalar + 1):
  for j in range(0,CollocationPoints+1):
    lu_150innit[(i,j)]= lu_150lb + (i+0.25*j)*(lu_150ub-lu_150lb)/float(2* scalar + 1)
    lu_150dotinnit[(i,j)] = (lu_150ub-lu_150lb)/float(2* scalar + 1)

# decrease 1
lu_150lb= 0.92
lu_150ub= 0.153

for i in range(2* scalar + 1,Elements + 1):
  for j in range(0,CollocationPoints+1):
    lu_150innit[(i,j)]= lu_150lb + (i+0.25*j)*(lu_150ub-lu_150lb)/float(Elements + 1)
    lu_150dotinnit[(i,j)] = (lu_150ub-lu_150lb)/float(Elements + 1)

# lu_300dot ----------
lu_300innit = {}
lu_300dotinnit = {}

# increase 1
lu_300lb= 0.0
lu_300ub= 2.11

for i in range(0, 2* scalar + 1):
  for j in range(0,CollocationPoints+1):
    lu_300innit[(i,j)]= lu_300lb + (i+0.25*j)*(lu_300ub-lu_300lb)/float(2* scalar + 1)
    lu_300dotinnit[(i,j)] = (lu_300ub-lu_300lb)/float(1* scalar + 1)

# decrease 1
lu_300lb= 2.11
lu_300ub= 1.25

for i in range(2* scalar + 1, Elements + 1):
  for j in range(0,CollocationPoints+1):
    lu_300innit[(i,j)]= lu_300lb + (i+0.25*j)*(lu_300ub-lu_300lb)/float(Elements + 1)
    lu_300dotinnit[(i,j)] = (lu_300ub-lu_300lb)/float(Elements + 1)

# lu_450dot ----------
lu_450innit = {}
lu_450dotinnit = {}

# increase 1
lu_450lb= 0.0
lu_450ub= 1.076

for i in range(0, 2* scalar + 1):
  for j in range(0,CollocationPoints+1):
    lu_450innit[(i,j)]= lu_450lb + (i+0.25*j)*(lu_450ub-lu_450lb)/float(2* scalar + 1)
    lu_450dotinnit = (lu_450ub-lu_450lb)/float(1* scalar + 1)

# decrease 1
lu_450lb= 1.076
lu_450ub= 0.906

for i in range(2* scalar + 1, Elements + 1):
  for j in range(0,CollocationPoints+1):
    lu_450innit[(i,j)]= lu_450lb + (i+0.25*j)*(lu_450ub-lu_450lb)/float(Elements + 1)
    lu_450dotinnit = (lu_450ub-lu_450lb)/float(Elements + 1)

# lu_600dot ----------
lu_600innit = {}
lu_600dotinnit = {}

# increasing 1
lu_600lb= 0.0
lu_600ub= 0.673


for i in range(0, 2* scalar + 1):
  for j in range(0,CollocationPoints+1):
    lu_600innit[(i,j)] = lu_600lb + (i+0.25*j)*(lu_600ub-lu_600lb)/float(2* scalar + 1)
    lu_600dotinnit[(i,j)] = (lu_600ub-lu_600lb)/float(1* scalar + 1)

# decreasing 1
lu_600lb= 0.673
lu_600ub= 0.49


for i in range(2* scalar + 1, Elements + 1):
  for j in range(0,CollocationPoints+1):
    lu_600innit[(i,j)] = lu_600lb + (i+0.25*j)*(lu_600ub-lu_600lb)/float(Elements + 1)
    lu_600dotinnit[(i,j)] = (lu_600ub-lu_600lb)/float(Elements + 1)


# f(I)      ----------

# define model parameters for f(I) and g(I) functions

ksL_I = (300.0 - 10.0)/4.0 
kiL_I = (1000.0 - 30.0)/4.0 
k_I = (100.0 - 0.001)/4.0 

kd_I = (10.0 - 0.0)/4.0 
km_I = (10.0 - 0.0)/4.0 

# define the dictionary
fI_150innit = {}
fI_300innit = {}
fI_450innit = {}
fI_600innit = {}

for i in range(0, Elements + 1):
  for j in range(0,CollocationPoints+1):
    fI_150innit[(i,j)] =( ( (150.0 * (np.exp(-0.084*(62.60700 * x_150innit[(i,j)] + 0.00))+1))/((150.0 * (np.exp(-0.084*(62.60700 * x_150innit[(i,j)] + 0.00))+1))+76.00+((150.0 * (np.exp(-0.084*(62.60700 * x_150innit[(i,j)] + 0.00))+1)))**2/2124.1800) * 2
+
(150.0 * (np.exp(-0.063*(62.60700 * x_150innit[(i,j)] + 0.00))+np.exp(-0.021 * (62.60700 * x_150innit[(i,j)] + 0.00))))/((150.0 * (np.exp(-0.063*(62.60700 * x_150innit[(i,j)] + 0.00))+np.exp(-0.021 * (62.60700 * x_150innit[(i,j)] + 0.00))))+76.00+(150.0 * (np.exp(-0.063*(62.60700 * x_150innit[(i,j)] + 0.00))+np.exp(-0.021 * (62.60700 * x_150innit[(i,j)] + 0.00))))**2/2124.1800) * 4
+
(150.0 * (np.exp(-0.0525*(62.60700 * x_150innit[(i,j)] + 0.00))+np.exp(-0.0315 * (62.60700 * x_150innit[(i,j)] + 0.00))))/((150.0 * (np.exp(-0.0525*(62.60700 * x_150innit[(i,j)] + 0.00))+np.exp(-0.0315 * (62.60700 * x_150innit[(i,j)] + 0.00))))+76.00+(150.0 * (np.exp(-0.0525*(62.60700 * x_150innit[(i,j)] + 0.00))+np.exp(-0.0315 * (62.60700 * x_150innit[(i,j)] + 0.00))))**2/2124.1800) * 4
+
(150.0 * (np.exp(-0.0735*(62.60700 * x_150innit[(i,j)] + 0.00))+np.exp(-0.0105* (62.60700 * x_150innit[(i,j)] + 0.00))))/((150.0 * (np.exp(-0.0735*(62.60700 * x_150innit[(i,j)] + 0.00))+np.exp(-0.0105 * (62.60700 * x_150innit[(i,j)] + 0.00))))+76.00+(150.0 * (np.exp(-0.0735*(62.60700 * x_150innit[(i,j)] + 0.00))+np.exp(-0.0105 * (62.60700 * x_150innit[(i,j)] + 0.00))))**2/2124.1800) * 4
+
(150.0*np.exp(-0.042*(62.60700 * x_150innit[(i,j)] + 0.00 )))*2*4/((2*150.0*np.exp(-0.042*(62.60700 * x_150innit[(i,j)] + 0.00 )))+76.00+(2*150.0*np.exp(-0.042*(62.60700 * x_150innit[(i,j)] + 0.00 )))**2/2124.1800)
)*1.0/18.0)

    fI_300innit[(i,j)] =( ( (300.0 * (np.exp(-0.084*(62.60700 * x_300innit[(i,j)] + 0.00))+1))/((300.0 * (np.exp(-0.084*(62.60700 * x_300innit[(i,j)] + 0.00))+1))+76.00+((300.0 * (np.exp(-0.084*(62.60700 * x_300innit[(i,j)] + 0.00))+1)))**2/2124.1800) * 2
+
(300.0 * (np.exp(-0.063*(62.60700 * x_300innit[(i,j)] + 0.00))+np.exp(-0.021 * (62.60700 * x_300innit[(i,j)] + 0.00))))/((300.0 * (np.exp(-0.063*(62.60700 * x_300innit[(i,j)] + 0.00))+np.exp(-0.021 * (62.60700 * x_300innit[(i,j)] + 0.00))))+76.00+(300.0 * (np.exp(-0.063*(62.60700 * x_300innit[(i,j)] + 0.00))+np.exp(-0.021 * (62.60700 * x_300innit[(i,j)] + 0.00))))**2/2124.1800) * 4
+
(300.0 * (np.exp(-0.0525*(62.60700 * x_300innit[(i,j)] + 0.00))+np.exp(-0.0315 * (62.60700 * x_300innit[(i,j)] + 0.00))))/((300.0 * (np.exp(-0.0525*(62.60700 * x_300innit[(i,j)] + 0.00))+np.exp(-0.0315 * (62.60700 * x_300innit[(i,j)] + 0.00))))+76.00+(300.0 * (np.exp(-0.0525*(62.60700 * x_300innit[(i,j)] + 0.00))+np.exp(-0.0315 * (62.60700 * x_300innit[(i,j)] + 0.00))))**2/2124.1800) * 4
+
(300.0 * (np.exp(-0.0735*(62.60700 * x_300innit[(i,j)] + 0.00))+np.exp(-0.0105* (62.60700 * x_300innit[(i,j)] + 0.00))))/((300.0 * (np.exp(-0.0735*(62.60700 * x_300innit[(i,j)] + 0.00))+np.exp(-0.0105 * (62.60700 * x_300innit[(i,j)] + 0.00))))+76.00+(300.0 * (np.exp(-0.0735*(62.60700 * x_300innit[(i,j)] + 0.00))+np.exp(-0.0105 * (62.60700 * x_300innit[(i,j)] + 0.00))))**2/2124.1800) * 4
+
(300.0*np.exp(-0.042*(62.60700 * x_300innit[(i,j)] + 0.00 )))*2*4/((2*300.0*np.exp(-0.042*(62.60700 * x_300innit[(i,j)] + 0.00 )))+76.00+(2*300.0*np.exp(-0.042*(62.60700 * x_300innit[(i,j)] + 0.00 )))**2/2124.1800)
)*1.0/18.0)
    
    fI_450innit[(i,j)] =( ( (450.0 * (np.exp(-0.084*(62.60700 * x_450innit[(i,j)] + 0.00))+1))/((450.0 * (np.exp(-0.084*(62.60700 * x_450innit[(i,j)] + 0.00))+1))+76.00+((450.0 * (np.exp(-0.084*(62.60700 * x_450innit[(i,j)] + 0.00))+1)))**2/2124.1800) * 2
+
(450.0 * (np.exp(-0.063*(62.60700 * x_450innit[(i,j)] + 0.00))+np.exp(-0.021 * (62.60700 * x_450innit[(i,j)] + 0.00))))/((450.0 * (np.exp(-0.063*(62.60700 * x_450innit[(i,j)] + 0.00))+np.exp(-0.021 * (62.60700 * x_450innit[(i,j)] + 0.00))))+76.00+(450.0 * (np.exp(-0.063*(62.60700 * x_450innit[(i,j)] + 0.00))+np.exp(-0.021 * (62.60700 * x_450innit[(i,j)] + 0.00))))**2/2124.1800) * 4
+
(450.0 * (np.exp(-0.0525*(62.60700 * x_450innit[(i,j)] + 0.00))+np.exp(-0.0315 * (62.60700 * x_450innit[(i,j)] + 0.00))))/((450.0 * (np.exp(-0.0525*(62.60700 * x_450innit[(i,j)] + 0.00))+np.exp(-0.0315 * (62.60700 * x_450innit[(i,j)] + 0.00))))+76.00+(450.0 * (np.exp(-0.0525*(62.60700 * x_450innit[(i,j)] + 0.00))+np.exp(-0.0315 * (62.60700 * x_450innit[(i,j)] + 0.00))))**2/2124.1800) * 4
+
(450.0 * (np.exp(-0.0735*(62.60700 * x_450innit[(i,j)] + 0.00))+np.exp(-0.0105* (62.60700 * x_450innit[(i,j)] + 0.00))))/((450.0 * (np.exp(-0.0735*(62.60700 * x_450innit[(i,j)] + 0.00))+np.exp(-0.0105 * (62.60700 * x_450innit[(i,j)] + 0.00))))+76.00+(450.0 * (np.exp(-0.0735*(62.60700 * x_450innit[(i,j)] + 0.00))+np.exp(-0.0105 * (62.60700 * x_450innit[(i,j)] + 0.00))))**2/2124.1800) * 4
+
(450.0*np.exp(-0.042*(62.60700 * x_450innit[(i,j)] + 0.00 )))*2*4/((2*450.0*np.exp(-0.042*(62.60700 * x_450innit[(i,j)] + 0.00 )))+76.00+(2*450.0*np.exp(-0.042*(62.60700 * x_450innit[(i,j)] + 0.00 )))**2/2124.1800)
)*1.0/18.0)

    fI_600innit[(i,j)] =( ( (600.0 * (np.exp(-0.084*(62.60700 * x_600innit[(i,j)] + 0.00))+1))/((600.0 * (np.exp(-0.084*(62.60700 * x_600innit[(i,j)] + 0.00))+1))+76.00+((600.0 * (np.exp(-0.084*(62.60700 * x_600innit[(i,j)] + 0.00))+1)))**2/2124.1800) * 2
+
(600.0 * (np.exp(-0.063*(62.60700 * x_600innit[(i,j)] + 0.00))+np.exp(-0.021 * (62.60700 * x_600innit[(i,j)] + 0.00))))/((600.0 * (np.exp(-0.063*(62.60700 * x_600innit[(i,j)] + 0.00))+np.exp(-0.021 * (62.60700 * x_600innit[(i,j)] + 0.00))))+76.00+(600.0 * (np.exp(-0.063*(62.60700 * x_600innit[(i,j)] + 0.00))+np.exp(-0.021 * (62.60700 * x_600innit[(i,j)] + 0.00))))**2/2124.1800) * 4
+
(600.0 * (np.exp(-0.0525*(62.60700 * x_600innit[(i,j)] + 0.00))+np.exp(-0.0315 * (62.60700 * x_600innit[(i,j)] + 0.00))))/((600.0 * (np.exp(-0.0525*(62.60700 * x_600innit[(i,j)] + 0.00))+np.exp(-0.0315 * (62.60700 * x_600innit[(i,j)] + 0.00))))+76.00+(600.0 * (np.exp(-0.0525*(62.60700 * x_600innit[(i,j)] + 0.00))+np.exp(-0.0315 * (62.60700 * x_600innit[(i,j)] + 0.00))))**2/2124.1800) * 4
+
(600.0 * (np.exp(-0.0735*(62.60700 * x_600innit[(i,j)] + 0.00))+np.exp(-0.0105* (62.60700 * x_600innit[(i,j)] + 0.00))))/((600.0 * (np.exp(-0.0735*(62.60700 * x_600innit[(i,j)] + 0.00))+np.exp(-0.0105 * (62.60700 * x_600innit[(i,j)] + 0.00))))+76.00+(600.0 * (np.exp(-0.0735*(62.60700 * x_600innit[(i,j)] + 0.00))+np.exp(-0.0105 * (62.60700 * x_600innit[(i,j)] + 0.00))))**2/2124.1800) * 4
+
(600.0*np.exp(-0.042*(62.60700 * x_600innit[(i,j)] + 0.00 )))*2*4/((2*600.0*np.exp(-0.042*(62.60700 * x_600innit[(i,j)] + 0.00 )))+76.00+(2*600.0*np.exp(-0.042*(62.60700 * x_600innit[(i,j)] + 0.00 )))**2/2124.1800)
)*1.0/18.0)

# g(I)      ----------
# define the dictionary
gI_150innit = {}
gI_300innit = {}
gI_450innit = {}
gI_600innit = {}

for i in range(0, Elements + 1):
  for j in range(0,CollocationPoints+1):
    gI_150innit[(i,j)] =( ( (150.0 * (np.exp(-0.084*(62.60700 * x_150innit[(i,j)] + 0.00))+1))/((150.0 * (np.exp(-0.084*(62.60700 * x_150innit[(i,j)] + 0.00))+1))+ksL_I+((150.0 * (np.exp(-0.084*(62.60700 * x_150innit[(i,j)] + 0.00))+1)))**2/kiL_I) * 2
+
(150.0 * (np.exp(-0.063*(62.60700 * x_150innit[(i,j)] + 0.00))+np.exp(-0.021 * (62.60700 * x_150innit[(i,j)] + 0.00))))/((150.0 * (np.exp(-0.063*(62.60700 * x_150innit[(i,j)] + 0.00))+np.exp(-0.021 * (62.60700 * x_150innit[(i,j)] + 0.00))))+ksL_I+(150.0 * (np.exp(-0.063*(62.60700 * x_150innit[(i,j)] + 0.00))+np.exp(-0.021 * (62.60700 * x_150innit[(i,j)] + 0.00))))**2/kiL_I) * 4
+
(150.0 * (np.exp(-0.0525*(62.60700 * x_150innit[(i,j)] + 0.00))+np.exp(-0.0315 * (62.60700 * x_150innit[(i,j)] + 0.00))))/((150.0 * (np.exp(-0.0525*(62.60700 * x_150innit[(i,j)] + 0.00))+np.exp(-0.0315 * (62.60700 * x_150innit[(i,j)] + 0.00))))+ksL_I+(150.0 * (np.exp(-0.0525*(62.60700 * x_150innit[(i,j)] + 0.00))+np.exp(-0.0315 * (62.60700 * x_150innit[(i,j)] + 0.00))))**2/kiL_I) * 4
+
(150.0 * (np.exp(-0.0735*(62.60700 * x_150innit[(i,j)] + 0.00))+np.exp(-0.0105* (62.60700 * x_150innit[(i,j)] + 0.00))))/((150.0 * (np.exp(-0.0735*(62.60700 * x_150innit[(i,j)] + 0.00))+np.exp(-0.0105 * (62.60700 * x_150innit[(i,j)] + 0.00))))+ksL_I+(150.0 * (np.exp(-0.0735*(62.60700 * x_150innit[(i,j)] + 0.00))+np.exp(-0.0105 * (62.60700 * x_150innit[(i,j)] + 0.00))))**2/kiL_I) * 4
+
(150.0*np.exp(-0.042*(62.60700 * x_150innit[(i,j)] + 0.00 )))*2*4/((2*150.0*np.exp(-0.042*(62.60700 * x_150innit[(i,j)] + 0.00 )))+ksL_I+(2*150.0*np.exp(-0.042*(62.60700 * x_150innit[(i,j)] + 0.00 )))**2/kiL_I)
)*1.0/18.0)

    gI_300innit[(i,j)] =( ( (300.0 * (np.exp(-0.084*(62.60700 * x_300innit[(i,j)] + 0.00))+1))/((300.0 * (np.exp(-0.084*(62.60700 * x_300innit[(i,j)] + 0.00))+1))+ksL_I+((300.0 * (np.exp(-0.084*(62.60700 * x_300innit[(i,j)] + 0.00))+1)))**2/kiL_I) * 2
+
(300.0 * (np.exp(-0.063*(62.60700 * x_300innit[(i,j)] + 0.00))+np.exp(-0.021 * (62.60700 * x_300innit[(i,j)] + 0.00))))/((300.0 * (np.exp(-0.063*(62.60700 * x_300innit[(i,j)] + 0.00))+np.exp(-0.021 * (62.60700 * x_300innit[(i,j)] + 0.00))))+ksL_I+(300.0 * (np.exp(-0.063*(62.60700 * x_300innit[(i,j)] + 0.00))+np.exp(-0.021 * (62.60700 * x_300innit[(i,j)] + 0.00))))**2/kiL_I) * 4
+
(300.0 * (np.exp(-0.0525*(62.60700 * x_300innit[(i,j)] + 0.00))+np.exp(-0.0315 * (62.60700 * x_300innit[(i,j)] + 0.00))))/((300.0 * (np.exp(-0.0525*(62.60700 * x_300innit[(i,j)] + 0.00))+np.exp(-0.0315 * (62.60700 * x_300innit[(i,j)] + 0.00))))+ksL_I+(300.0 * (np.exp(-0.0525*(62.60700 * x_300innit[(i,j)] + 0.00))+np.exp(-0.0315 * (62.60700 * x_300innit[(i,j)] + 0.00))))**2/kiL_I) * 4
+
(300.0 * (np.exp(-0.0735*(62.60700 * x_300innit[(i,j)] + 0.00))+np.exp(-0.0105* (62.60700 * x_300innit[(i,j)] + 0.00))))/((300.0 * (np.exp(-0.0735*(62.60700 * x_300innit[(i,j)] + 0.00))+np.exp(-0.0105 * (62.60700 * x_300innit[(i,j)] + 0.00))))+ksL_I+(300.0 * (np.exp(-0.0735*(62.60700 * x_300innit[(i,j)] + 0.00))+np.exp(-0.0105 * (62.60700 * x_300innit[(i,j)] + 0.00))))**2/kiL_I) * 4
+
(300.0*np.exp(-0.042*(62.60700 * x_300innit[(i,j)] + 0.00 )))*2*4/((2*300.0*np.exp(-0.042*(62.60700 * x_300innit[(i,j)] + 0.00 )))+ksL_I+(2*300.0*np.exp(-0.042*(62.60700 * x_300innit[(i,j)] + 0.00 )))**2/kiL_I)
)*1.0/18.0)
    
    gI_450innit[(i,j)] =( ( (450.0 * (np.exp(-0.084*(62.60700 * x_450innit[(i,j)] + 0.00))+1))/((450.0 * (np.exp(-0.084*(62.60700 * x_450innit[(i,j)] + 0.00))+1))+ksL_I+((450.0 * (np.exp(-0.084*(62.60700 * x_450innit[(i,j)] + 0.00))+1)))**2/kiL_I) * 2
+
(450.0 * (np.exp(-0.063*(62.60700 * x_450innit[(i,j)] + 0.00))+np.exp(-0.021 * (62.60700 * x_450innit[(i,j)] + 0.00))))/((450.0 * (np.exp(-0.063*(62.60700 * x_450innit[(i,j)] + 0.00))+np.exp(-0.021 * (62.60700 * x_450innit[(i,j)] + 0.00))))+ksL_I+(450.0 * (np.exp(-0.063*(62.60700 * x_450innit[(i,j)] + 0.00))+np.exp(-0.021 * (62.60700 * x_450innit[(i,j)] + 0.00))))**2/kiL_I) * 4
+
(450.0 * (np.exp(-0.0525*(62.60700 * x_450innit[(i,j)] + 0.00))+np.exp(-0.0315 * (62.60700 * x_450innit[(i,j)] + 0.00))))/((450.0 * (np.exp(-0.0525*(62.60700 * x_450innit[(i,j)] + 0.00))+np.exp(-0.0315 * (62.60700 * x_450innit[(i,j)] + 0.00))))+ksL_I+(450.0 * (np.exp(-0.0525*(62.60700 * x_450innit[(i,j)] + 0.00))+np.exp(-0.0315 * (62.60700 * x_450innit[(i,j)] + 0.00))))**2/kiL_I) * 4
+
(450.0 * (np.exp(-0.0735*(62.60700 * x_450innit[(i,j)] + 0.00))+np.exp(-0.0105* (62.60700 * x_450innit[(i,j)] + 0.00))))/((450.0 * (np.exp(-0.0735*(62.60700 * x_450innit[(i,j)] + 0.00))+np.exp(-0.0105 * (62.60700 * x_450innit[(i,j)] + 0.00))))+ksL_I+(450.0 * (np.exp(-0.0735*(62.60700 * x_450innit[(i,j)] + 0.00))+np.exp(-0.0105 * (62.60700 * x_450innit[(i,j)] + 0.00))))**2/kiL_I) * 4
+
(450.0*np.exp(-0.042*(62.60700 * x_450innit[(i,j)] + 0.00 )))*2*4/((2*450.0*np.exp(-0.042*(62.60700 * x_450innit[(i,j)] + 0.00 )))+ksL_I+(2*450.0*np.exp(-0.042*(62.60700 * x_450innit[(i,j)] + 0.00 )))**2/kiL_I)
)*1.0/18.0)

    gI_600innit[(i,j)] =( ( (600.0 * (np.exp(-0.084*(62.60700 * x_600innit[(i,j)] + 0.00))+1))/((600.0 * (np.exp(-0.084*(62.60700 * x_600innit[(i,j)] + 0.00))+1))+ksL_I+((600.0 * (np.exp(-0.084*(62.60700 * x_600innit[(i,j)] + 0.00))+1)))**2/kiL_I) * 2
+
(600.0 * (np.exp(-0.063*(62.60700 * x_600innit[(i,j)] + 0.00))+np.exp(-0.021 * (62.60700 * x_600innit[(i,j)] + 0.00))))/((600.0 * (np.exp(-0.063*(62.60700 * x_600innit[(i,j)] + 0.00))+np.exp(-0.021 * (62.60700 * x_600innit[(i,j)] + 0.00))))+ksL_I+(600.0 * (np.exp(-0.063*(62.60700 * x_600innit[(i,j)] + 0.00))+np.exp(-0.021 * (62.60700 * x_600innit[(i,j)] + 0.00))))**2/kiL_I) * 4
+
(600.0 * (np.exp(-0.0525*(62.60700 * x_600innit[(i,j)] + 0.00))+np.exp(-0.0315 * (62.60700 * x_600innit[(i,j)] + 0.00))))/((600.0 * (np.exp(-0.0525*(62.60700 * x_600innit[(i,j)] + 0.00))+np.exp(-0.0315 * (62.60700 * x_600innit[(i,j)] + 0.00))))+ksL_I+(600.0 * (np.exp(-0.0525*(62.60700 * x_600innit[(i,j)] + 0.00))+np.exp(-0.0315 * (62.60700 * x_600innit[(i,j)] + 0.00))))**2/kiL_I) * 4
+
(600.0 * (np.exp(-0.0735*(62.60700 * x_600innit[(i,j)] + 0.00))+np.exp(-0.0105* (62.60700 * x_600innit[(i,j)] + 0.00))))/((600.0 * (np.exp(-0.0735*(62.60700 * x_600innit[(i,j)] + 0.00))+np.exp(-0.0105 * (62.60700 * x_600innit[(i,j)] + 0.00))))+ksL_I+(600.0 * (np.exp(-0.0735*(62.60700 * x_600innit[(i,j)] + 0.00))+np.exp(-0.0105 * (62.60700 * x_600innit[(i,j)] + 0.00))))**2/kiL_I) * 4
+
(600.0*np.exp(-0.042*(62.60700 * x_600innit[(i,j)] + 0.00 )))*2*4/((2*600.0*np.exp(-0.042*(62.60700 * x_600innit[(i,j)] + 0.00 )))+ksL_I+(2*600.0*np.exp(-0.042*(62.60700 * x_600innit[(i,j)] + 0.00 )))**2/kiL_I)
)*1.0/18.0)

#---------------------- variables---------------------#
model.dim = Set(dimen=2, initialize=[(i,j) for i in range(0,len(Indexing)+1) for j in Indexing[1]])

model.X_150dot= Var(model.dim ,bounds=(0.0, 2.0), initialize = x_150dotinnit)
model.X_150= Var(model.dim,within=NonNegativeReals,  bounds=(0.0, 3.0) , initialize = x_150innit)
model.N_150dot= Var(model.dim,  bounds=(-500.0, 500.0) , initialize = n_150dotinnit)
model.N_150= Var(model.dim,within=NonNegativeReals,  bounds=(200.0, 3000.0) , initialize = n_150innit)
model.Lu_150dot= Var(model.dim,  bounds=(-2.0, 2.0) , initialize = lu_150dotinnit)
model.Lu_150= Var(model.dim,within=NonNegativeReals,  bounds=(0.0, 3.0) , initialize = lu_150innit)
model.fI_150= Var(model.dim,within=NonNegativeReals, initialize = fI_150innit)
model.gI_150= Var(model.dim,within=NonNegativeReals, initialize = gI_150innit)

model.X_300dot= Var(model.dim, bounds=(0.0, 2.0), initialize = x_300dotinnit)
model.X_300= Var(model.dim,within=NonNegativeReals,  bounds=(0.0, 3.0) , initialize = x_300innit)
model.N_300dot= Var(model.dim,  bounds=(-500.0, 500.0) , initialize = n_300dotinnit)
model.N_300= Var(model.dim,within=NonNegativeReals,  bounds=(200.0, 3000.0) , initialize = n_300innit)
model.Lu_300dot= Var(model.dim,  bounds=(-2.0, 2.0) , initialize = lu_300dotinnit)
model.Lu_300= Var(model.dim,within=NonNegativeReals,  bounds=(0.0, 3.0) , initialize = lu_300innit)
model.fI_300= Var(model.dim,within=NonNegativeReals, initialize = fI_300innit)
model.gI_300= Var(model.dim,within=NonNegativeReals, initialize = gI_300innit)

model.X_450dot= Var(model.dim, bounds=(0.0, 2.0), initialize = x_450dotinnit)
model.X_450= Var(model.dim,within=NonNegativeReals,  bounds=(0.0, 3.0) , initialize = x_450innit)
model.N_450dot= Var(model.dim,  bounds=(-500.0, 500.0) , initialize = n_450dotinnit)
model.N_450= Var(model.dim,within=NonNegativeReals,  bounds=(200.0, 3000.0) , initialize = n_450innit)
model.Lu_450dot= Var(model.dim,  bounds=(-2.0, 2.0) , initialize = lu_450dotinnit)
model.Lu_450= Var(model.dim,within=NonNegativeReals,  bounds=(0.0, 3.0) , initialize = lu_450innit)
model.fI_450= Var(model.dim,within=NonNegativeReals, initialize = fI_450innit)
model.gI_450= Var(model.dim,within=NonNegativeReals, initialize = gI_450innit)

model.X_600dot= Var(model.dim, bounds=(0.0, 2.0), initialize = x_600dotinnit)
model.X_600= Var(model.dim,  bounds=(0.0, 3.0) , initialize = x_600innit)
model.N_600dot= Var(model.dim,  bounds=(-500.0, 500.0) , initialize = n_600dotinnit)
model.N_600= Var(model.dim,  bounds=(200.0, 3000.0) , initialize = n_600innit)
model.Lu_600dot= Var(model.dim,  bounds=(-2.0, 2.0) , initialize = lu_600dotinnit)
model.Lu_600= Var(model.dim,  bounds=(0.0, 3.0) , initialize = lu_600innit)
model.fI_600= Var(model.dim,within=NonNegativeReals, initialize = fI_600innit)
model.gI_600= Var(model.dim,within=NonNegativeReals, initialize = gI_600innit)

#---------------------- controles ---------------------#

model.ksL= Var(bounds=(5.0, 100.0), initialize = (300.0 - 10.0)/4.0 )
model.kiL= Var(bounds=(100.0, 800.0), initialize = (1000.0 - 30.0)/4.0 )
model.k= Var(bounds=(0.001, 0.1), initialize = 100)#(100.0 - 0.001)/4.0 )

model.kd= Var(bounds=(0.0, 1000.0), initialize = (100.0 - 0.0)/4.0 )
model.km= Var(bounds=(0.0, 200.0), initialize = (10.0 - 0.0)/4.0 )

#---------------------- Obj function---------------------#
model.obj = Objective(expr=  

(

( model.Lu_150[(1*scalar,0)]-0.0 )**2 +
( model.Lu_150[(2*scalar,0)]-0.92 )**2 +
( model.Lu_150[(3*scalar,0)]-0.57 )**2 +
( model.Lu_150[(4*scalar,0)]-0.44 )**2 +
( model.Lu_150[(5*scalar,0)]-0.36 )**2 +
( model.Lu_150[(6*scalar,0)]-0.296 )**2 +
( model.Lu_150[(7*scalar,0)]-0.265 )**2 +
( model.Lu_150[(8*scalar,0)]-0.26 )**2 +
( model.Lu_150[(9*scalar,0)]-0.235 )**2 +
( model.Lu_150[(10*scalar,0)]-0.23 )**2 +
( model.Lu_150[(11*scalar,0)]-0.18 )**2 +
( model.Lu_150[(12*scalar,0)]-0.153 )**2

)*4/(0.153+0.92)**2 +

(

( model.Lu_300[(1*scalar,0)]-0.0 )**2 +
( model.Lu_300[(2*scalar,0)]-2.11 )**2 +
( model.Lu_300[(3*scalar,0)]-1.94 )**2 +
( model.Lu_300[(4*scalar,0)]-1.53 )**2 +
( model.Lu_300[(5*scalar,0)]-1.4 )**2 *5+
( model.Lu_300[(6*scalar,0)]-1.39 )**2 *5+
( model.Lu_300[(7*scalar,0)]-1.27 )**2 *5+
( model.Lu_300[(8*scalar,0)]-1.28 )**2 *5+
( model.Lu_300[(9*scalar,0)]-1.28 )**2 +
( model.Lu_300[(10*scalar,0)]-1.22 )**2 +
( model.Lu_300[(11*scalar,0)]-1.30 )**2 +
( model.Lu_300[(12*scalar,0)]-1.25 )**2

)*4/(1.22+0.92)**2 +

(

( model.Lu_450[(1*scalar,0)]-0.0 )**2 +
( model.Lu_450[(2*scalar,0)]-1.076 )**2 +
( model.Lu_450[(3*scalar,0)]-1.043 )**2 +
( model.Lu_450[(4*scalar,0)]-1.33 )**2 +
( model.Lu_450[(5*scalar,0)]-0.89 )**2 *5+
( model.Lu_450[(6*scalar,0)]-0.81 )**2 *5+
( model.Lu_450[(7*scalar,0)]-0.81 )**2 *5+
( model.Lu_450[(8*scalar,0)]-0.83 )**2 *5+
( model.Lu_450[(9*scalar,0)]-0.90 )**2 +
( model.Lu_450[(10*scalar,0)]-0.95 )**2 +
( model.Lu_450[(11*scalar,0)]-1.01 )**2 +
( model.Lu_450[(12*scalar,0)]-0.906 )**2

)*4/(0.81+1.33)**2 +

(

( model.Lu_600[(1*scalar,0)]-0.0 )**2 +
( model.Lu_600[(2*scalar,0)]-0.673 )**2 +
( model.Lu_600[(3*scalar,0)]-0.681 )**2 +
( model.Lu_600[(4*scalar,0)]-0.599 )**2 +
( model.Lu_600[(5*scalar,0)]-0.656 )**2 *5+
( model.Lu_600[(6*scalar,0)]-0.703 )**2 *5+
( model.Lu_600[(7*scalar,0)]-0.767 )**2 *5+
( model.Lu_600[(8*scalar,0)]-0.74 )**2 *5+
( model.Lu_600[(9*scalar,0)]-0.76 )**2 +
( model.Lu_600[(10*scalar,0)]-0.66 )**2 +
( model.Lu_600[(11*scalar,0)]-0.558 )**2 +
( model.Lu_600[(12*scalar,0)]-0.49 )**2

)*4/(0.49+0.767)**2


)


#------------------ Collocation Constraints-----------------#

def CoverConstrCollocX150_rule(model, i, j):
  return model.X_150[(i,j)] == model.X_150[(i,0)]+(Final_time/Elements)*( A[j-1][0]*model.X_150dot[(i,1)] + A[j-1][1]*model.X_150dot[(i,2)] + A[j-1][2]*model.X_150dot[(i,3)] )
model.CoverConstrCollocX150 = Constraint(ListElem,ListPoints, rule= CoverConstrCollocX150_rule)

def CoverConstrCollocX300_rule(model, i, j):
  return model.X_300[(i,j)] == model.X_300[(i,0)]+(Final_time/Elements)*( A[j-1][0]*model.X_300dot[(i,1)] + A[j-1][1]*model.X_300dot[(i,2)] + A[j-1][2]*model.X_300dot[(i,3)] )
model.CoverConstrCollocX300 = Constraint(ListElem,ListPoints, rule= CoverConstrCollocX300_rule)

def CoverConstrCollocX450_rule(model, i, j):
  return model.X_450[(i,j)] == model.X_450[(i,0)]+(Final_time/Elements)*( A[j-1][0]*model.X_450dot[(i,1)] + A[j-1][1]*model.X_450dot[(i,2)] + A[j-1][2]*model.X_450dot[(i,3)] )
model.CoverConstrCollocX450 = Constraint(ListElem,ListPoints, rule= CoverConstrCollocX450_rule)

def CoverConstrCollocX600_rule(model, i, j):
  return model.X_600[(i,j)] == model.X_600[(i,0)]+(Final_time/Elements)*( A[j-1][0]*model.X_600dot[(i,1)] + A[j-1][1]*model.X_600dot[(i,2)] + A[j-1][2]*model.X_600dot[(i,3)] )
model.CoverConstrCollocX600 = Constraint(ListElem,ListPoints, rule= CoverConstrCollocX600_rule)

###

def CoverConstrCollocN150_rule(model, i, j):
  return model.N_150[(i,j)] == model.N_150[(i,0)]+(Final_time/Elements)*( A[j-1][0]*model.N_150dot[(i,1)] + A[j-1][1]*model.N_150dot[(i,2)] + A[j-1][2]*model.N_150dot[(i,3)] )
model.CoverConstrCollocN150 = Constraint(ListElem,ListPoints, rule= CoverConstrCollocN150_rule)

def CoverConstrCollocN300_rule(model, i, j):
  return model.N_300[(i,j)] == model.N_300[(i,0)]+(Final_time/Elements)*( A[j-1][0]*model.N_300dot[(i,1)] + A[j-1][1]*model.N_300dot[(i,2)] + A[j-1][2]*model.N_300dot[(i,3)] )
model.CoverConstrCollocN300 = Constraint(ListElem,ListPoints, rule= CoverConstrCollocN300_rule)

def CoverConstrCollocN450_rule(model, i, j):
  return model.N_450[(i,j)] == model.N_450[(i,0)]+(Final_time/Elements)*( A[j-1][0]*model.N_450dot[(i,1)] + A[j-1][1]*model.N_450dot[(i,2)] + A[j-1][2]*model.N_450dot[(i,3)] )
model.CoverConstrCollocN450 = Constraint(ListElem,ListPoints, rule= CoverConstrCollocN450_rule)

def CoverConstrCollocN600_rule(model, i, j):
  return model.N_600[(i,j)] == model.N_600[(i,0)]+(Final_time/Elements)*( A[j-1][0]*model.N_600dot[(i,1)] + A[j-1][1]*model.N_600dot[(i,2)] + A[j-1][2]*model.N_600dot[(i,3)] )
model.CoverConstrCollocN600 = Constraint(ListElem,ListPoints, rule= CoverConstrCollocN600_rule)

###

def CoverConstrCollocLu150_rule(model, i, j):
  return model.Lu_150[(i,j)] == model.Lu_150[(i,0)]+(Final_time/Elements)*( A[j-1][0]*model.Lu_150dot[(i,1)] + A[j-1][1]*model.Lu_150dot[(i,2)] + A[j-1][2]*model.Lu_150dot[(i,3)] )
model.CoverConstrCollocLu150 = Constraint(ListElem,ListPoints, rule= CoverConstrCollocLu150_rule)

def CoverConstrCollocLu300_rule(model, i, j):
  return model.Lu_300[(i,j)] == model.Lu_300[(i,0)]+(Final_time/Elements)*( A[j-1][0]*model.Lu_300dot[(i,1)] + A[j-1][1]*model.Lu_300dot[(i,2)] + A[j-1][2]*model.Lu_300dot[(i,3)] )
model.CoverConstrCollocLu300 = Constraint(ListElem,ListPoints, rule= CoverConstrCollocLu300_rule)

def CoverConstrCollocLu450_rule(model, i, j):
  return model.Lu_450[(i,j)] == model.Lu_450[(i,0)]+(Final_time/Elements)*( A[j-1][0]*model.Lu_450dot[(i,1)] + A[j-1][1]*model.Lu_450dot[(i,2)] + A[j-1][2]*model.Lu_450dot[(i,3)] )
model.CoverConstrCollocLu450 = Constraint(ListElem,ListPoints, rule= CoverConstrCollocLu450_rule)

def CoverConstrCollocLu600_rule(model, i, j):
  return model.Lu_600[(i,j)] == model.Lu_600[(i,0)]+(Final_time/Elements)*( A[j-1][0]*model.Lu_600dot[(i,1)] + A[j-1][1]*model.Lu_600dot[(i,2)] + A[j-1][2]*model.Lu_600dot[(i,3)] )
model.CoverConstrCollocLu600 = Constraint(ListElem,ListPoints, rule= CoverConstrCollocLu600_rule)

#------------------ Continuity Constraints -----------------#

def CoverConstrContX150_rule(model, i):
  if i !=0:
    return model.X_150[(i,0)] == model.X_150[(i-1,CollocationPoints)]
  else:
    return model.X_150[(i,0)] == 0.077
model.CoverConstrContX150= Constraint(ListElem, rule= CoverConstrContX150_rule)

def CoverConstrContX300_rule(model, i):
  if i !=0:
    return model.X_300[(i,0)] == model.X_300[(i-1,CollocationPoints)]
  else:
    return model.X_300[(i,0)] == 0.077
model.CoverConstrContX300= Constraint(ListElem, rule= CoverConstrContX300_rule)

def CoverConstrContX450_rule(model, i):
  if i !=0:
    return model.X_450[(i,0)] == model.X_450[(i-1,CollocationPoints)]
  else:
    return model.X_450[(i,0)] == 0.077
model.CoverConstrContX450= Constraint(ListElem, rule= CoverConstrContX450_rule)

def CoverConstrContX600_rule(model, i):
  if i !=0:
    return model.X_600[(i,0)] == model.X_600[(i-1,CollocationPoints)]
  else:
    return model.X_600[(i,0)] == 0.077
model.CoverConstrContX600= Constraint(ListElem, rule= CoverConstrContX600_rule)

###

def CoverConstrContN150_rule(model, i):
  if i !=0:
    return model.N_150[(i,0)] == model.N_150[(i-1,CollocationPoints)]
  else:
    return model.N_150[(i,0)] == 783.2
model.CoverConstrContN150= Constraint(ListElem, rule= CoverConstrContN150_rule)

def CoverConstrContN300_rule(model, i):
  if i !=0:
    return model.N_300[(i,0)] == model.N_300[(i-1,CollocationPoints)]
  else:
    return model.N_300[(i,0)] == 783.5
model.CoverConstrContN300= Constraint(ListElem, rule= CoverConstrContN300_rule)

def CoverConstrContN450_rule(model, i):
  if i !=0:
    return model.N_450[(i,0)] == model.N_450[(i-1,CollocationPoints)]
  else:
    return model.N_450[(i,0)] == 784.4
model.CoverConstrContN450= Constraint(ListElem, rule= CoverConstrContN450_rule)

def CoverConstrContN600_rule(model, i):
  if i !=0:
    return model.N_600[(i,0)] == model.N_600[(i-1,CollocationPoints)]
  else:
    return model.N_600[(i,0)] == 783.3
model.CoverConstrContN600= Constraint(ListElem, rule= CoverConstrContN600_rule)

###

def CoverConstrContLu150_rule(model, i):
  if i !=0:
    return model.Lu_150[(i,0)] == model.Lu_150[(i-1,CollocationPoints)]
  else:
    return model.Lu_150[(i,0)] == 0.0
model.CoverConstrContLu150= Constraint(ListElem, rule= CoverConstrContLu150_rule)

def CoverConstrContLu300_rule(model, i):
  if i !=0:
    return model.Lu_300[(i,0)] == model.Lu_300[(i-1,CollocationPoints)]
  else:
    return model.Lu_300[(i,0)] == 0.0
model.CoverConstrContLu300= Constraint(ListElem, rule= CoverConstrContLu300_rule)

def CoverConstrContLu450_rule(model, i):
  if i !=0:
    return model.Lu_450[(i,0)] == model.Lu_450[(i-1,CollocationPoints)]
  else:
    return model.Lu_450[(i,0)] == 0.0
model.CoverConstrContLu450= Constraint(ListElem, rule= CoverConstrContLu450_rule)

def CoverConstrContLu600_rule(model, i):
  if i !=0:
    return model.Lu_600[(i,0)] == model.Lu_600[(i-1,CollocationPoints)]
  else:
    return model.Lu_600[(i,0)] == 0.0
model.CoverConstrContLu600= Constraint(ListElem, rule= CoverConstrContLu600_rule)


#------------------ Differential Constraints-----------------#

# X

def CoverConstrDiffX150_rule(model, i, j):
  return model.X_150dot[(i,j)] == 0.202700 * model.fI_150[(i,j)] * model.N_150[(i,j)]/(300.47900 + model.N_150[(i,j)]) * model.X_150[(i,j)] - 0.044300 * model.X_150[(i,j)]
model.CoverConstrDiffX150= Constraint(ListElem,ListPoints, rule= CoverConstrDiffX150_rule)

def CoverConstrDiffX300_rule(model, i, j):
  return model.X_300dot[(i,j)] == 0.202700 * model.fI_300[(i,j)] * model.N_300[(i,j)]/(300.47900 + model.N_300[(i,j)]) * model.X_300[(i,j)] - 0.044300 * model.X_300[(i,j)]
model.CoverConstrDiffX300= Constraint(ListElem,ListPoints, rule= CoverConstrDiffX300_rule)

def CoverConstrDiffX450_rule(model, i, j):
  return model.X_450dot[(i,j)] == 0.202700 * model.fI_450[(i,j)] * model.N_450[(i,j)]/(300.47900 + model.N_450[(i,j)]) * model.X_450[(i,j)] - 0.044300 * model.X_450[(i,j)]
model.CoverConstrDiffX450= Constraint(ListElem,ListPoints, rule= CoverConstrDiffX450_rule)

def CoverConstrDiffX600_rule(model, i, j):
  return model.X_600dot[(i,j)] == 0.202700 * model.fI_600[(i,j)] * model.N_600[(i,j)]/(300.47900 + model.N_600[(i,j)]) * model.X_600[(i,j)] - 0.044300 * model.X_600[(i,j)]
model.CoverConstrDiffX600= Constraint(ListElem,ListPoints, rule= CoverConstrDiffX600_rule)

# N

def CoverConstrDiffN150_rule(model, i, j):
  return model.N_150dot[(i,j)] == - 232.25700 * 0.202700 * model.fI_150[(i,j)] * model.N_150[(i,j)]/(model.N_150[(i,j)] + 300.47900) * model.X_150[(i,j)] + Fin[i][j]
model.CoverConstrDiffN150= Constraint(ListElem,ListPoints, rule= CoverConstrDiffN150_rule)

def CoverConstrDiffN300_rule(model, i, j):
  return model.N_300dot[(i,j)] == - 232.25700 * 0.202700 * model.fI_300[(i,j)] * model.N_300[(i,j)]/(model.N_300[(i,j)] + 300.47900) * model.X_300[(i,j)] + Fin[i][j]
model.CoverConstrDiffN300= Constraint(ListElem,ListPoints, rule= CoverConstrDiffN300_rule)

def CoverConstrDiffN450_rule(model, i, j):
  return model.N_450dot[(i,j)] == - 232.25700 * 0.202700 * model.fI_450[(i,j)] * model.N_450[(i,j)]/(model.N_450[(i,j)] + 300.47900) * model.X_450[(i,j)] + Fin[i][j]
model.CoverConstrDiffN450= Constraint(ListElem,ListPoints, rule= CoverConstrDiffN450_rule)

def CoverConstrDiffN600_rule(model, i, j):
  return model.N_600dot[(i,j)] == - 232.25700 * 0.202700 * model.fI_600[(i,j)] * model.N_600[(i,j)]/(model.N_600[(i,j)] + 300.47900) * model.X_600[(i,j)] + Fin[i][j]
model.CoverConstrDiffN600= Constraint(ListElem,ListPoints, rule= CoverConstrDiffN600_rule)

# Lu

def CoverConstrDiffLu150_rule(model, i, j):
  return model.Lu_150dot[(i,j)] == model.k * model.gI_150[(i,j)] * model.N_150[(i,j)]/(model.N_150[(i,j)] + 300.47900) - model.Lu_150[(i,j)] * model.kd * model.N_150[(i,j)]/(300.47900 + model.N_150[(i,j)])
model.CoverConstrDiffLu150= Constraint(ListElem,ListPoints, rule= CoverConstrDiffLu150_rule)

def CoverConstrDiffLu300_rule(model, i, j):
  return model.Lu_300dot[(i,j)] == model.k * model.gI_300[(i,j)] * model.N_300[(i,j)]/(model.N_300[(i,j)] + 300.47900) - model.Lu_300[(i,j)] * model.kd * model.N_300[(i,j)]/(300.47900 + model.N_300[(i,j)])
model.CoverConstrDiffLu300= Constraint(ListElem,ListPoints, rule= CoverConstrDiffLu300_rule)

def CoverConstrDiffLu450_rule(model, i, j):
  return model.Lu_450dot[(i,j)] == model.k * model.gI_450[(i,j)] * model.N_450[(i,j)]/(model.N_450[(i,j)] + 300.47900) - model.Lu_450[(i,j)] * model.kd * model.N_450[(i,j)]/(300.47900 + model.N_450[(i,j)])
model.CoverConstrDiffLu450= Constraint(ListElem,ListPoints, rule= CoverConstrDiffLu450_rule)

def CoverConstrDiffLu600_rule(model, i, j):
  return model.Lu_600dot[(i,j)] == model.k * model.gI_600[(i,j)] * model.N_600[(i,j)]/(model.N_600[(i,j)] + 300.47900) - model.Lu_600[(i,j)] * model.kd * model.N_600[(i,j)]/(300.47900 + model.N_600[(i,j)])
model.CoverConstrDiffLu600= Constraint(ListElem,ListPoints, rule= CoverConstrDiffLu600_rule)

#--- Light --- #

# fI

def CoverConstrDifffI150_rule(model, i, j):
  return model.fI_150[(i,j)] == ( (150.0 * (exp(-0.084*(62.60700 * model.X_150[(i,j)] + 0.00))+1))/((150.0 * (exp(-0.084*(62.60700 * model.X_150[(i,j)] + 0.00))+1))+76.00+((150.0 * (exp(-0.084*(62.60700 * model.X_150[(i,j)] + 0.00))+1)))**2/2124.1800) * 2
+
(150.0 * (exp(-0.063*(62.60700 * model.X_150[(i,j)] + 0.00))+exp(-0.021 * (62.60700 * model.X_150[(i,j)] + 0.00))))/((150.0 * (exp(-0.063*(62.60700 * model.X_150[(i,j)] + 0.00))+exp(-0.021 * (62.60700 * model.X_150[(i,j)] + 0.00))))+76.00+(150.0 * (exp(-0.063*(62.60700 * model.X_150[(i,j)] + 0.00))+exp(-0.021 * (62.60700 * model.X_150[(i,j)] + 0.00))))**2/2124.1800) * 4
+
(150.0 * (exp(-0.0525*(62.60700 * model.X_150[(i,j)] + 0.00))+exp(-0.0315 * (62.60700 * model.X_150[(i,j)] + 0.00))))/((150.0 * (exp(-0.0525*(62.60700 * model.X_150[(i,j)] + 0.00))+exp(-0.0315 * (62.60700 * model.X_150[(i,j)] + 0.00))))+76.00+(150.0 * (exp(-0.0525*(62.60700 * model.X_150[(i,j)] + 0.00))+exp(-0.0315 * (62.60700 * model.X_150[(i,j)] + 0.00))))**2/2124.1800) * 4
+
(150.0 * (exp(-0.0735*(62.60700 * model.X_150[(i,j)] + 0.00))+exp(-0.0105* (62.60700 * model.X_150[(i,j)] + 0.00))))/((150.0 * (exp(-0.0735*(62.60700 * model.X_150[(i,j)] + 0.00))+exp(-0.0105 * (62.60700 * model.X_150[(i,j)] + 0.00))))+76.00+(150.0 * (exp(-0.0735*(62.60700 * model.X_150[(i,j)] + 0.00))+exp(-0.0105 * (62.60700 * model.X_150[(i,j)] + 0.00))))**2/2124.1800) * 4
+
(150.0*exp(-0.042*(62.60700 * model.X_150[(i,j)] + 0.00 )))*2*4/((2*150.0*exp(-0.042*(62.60700 * model.X_150[(i,j)] + 0.00 )))+76.00+(2*150.0*exp(-0.042*(62.60700 * model.X_150[(i,j)] + 0.00 )))**2/2124.1800)
)*1.0/18.0
model.CoverConstrDifffI150= Constraint(ListElem,ListPoints, rule= CoverConstrDifffI150_rule)

def CoverConstrDifffI300_rule(model, i, j):
  return model.fI_300[(i,j)] == ( (300.0 * (exp(-0.084*(62.60700 * model.X_300[(i,j)] + 0.00))+1))/((300.0 * (exp(-0.084*(62.60700 * model.X_300[(i,j)] + 0.00))+1))+76.00+((300.0 * (exp(-0.084*(62.60700 * model.X_300[(i,j)] + 0.00))+1)))**2/2124.1800) * 2
+
(300.0 * (exp(-0.063*(62.60700 * model.X_300[(i,j)] + 0.00))+exp(-0.021 * (62.60700 * model.X_300[(i,j)] + 0.00))))/((300.0 * (exp(-0.063*(62.60700 * model.X_300[(i,j)] + 0.00))+exp(-0.021 * (62.60700 * model.X_300[(i,j)] + 0.00))))+76.00+(300.0 * (exp(-0.063*(62.60700 * model.X_300[(i,j)] + 0.00))+exp(-0.021 * (62.60700 * model.X_300[(i,j)] + 0.00))))**2/2124.1800) * 4
+
(300.0 * (exp(-0.0525*(62.60700 * model.X_300[(i,j)] + 0.00))+exp(-0.0315 * (62.60700 * model.X_300[(i,j)] + 0.00))))/((300.0 * (exp(-0.0525*(62.60700 * model.X_300[(i,j)] + 0.00))+exp(-0.0315 * (62.60700 * model.X_300[(i,j)] + 0.00))))+76.00+(300.0 * (exp(-0.0525*(62.60700 * model.X_300[(i,j)] + 0.00))+exp(-0.0315 * (62.60700 * model.X_300[(i,j)] + 0.00))))**2/2124.1800) * 4
+
(300.0 * (exp(-0.0735*(62.60700 * model.X_300[(i,j)] + 0.00))+exp(-0.0105* (62.60700 * model.X_300[(i,j)] + 0.00))))/((300.0 * (exp(-0.0735*(62.60700 * model.X_300[(i,j)] + 0.00))+exp(-0.0105 * (62.60700 * model.X_300[(i,j)] + 0.00))))+76.00+(300.0 * (exp(-0.0735*(62.60700 * model.X_300[(i,j)] + 0.00))+exp(-0.0105 * (62.60700 * model.X_300[(i,j)] + 0.00))))**2/2124.1800) * 4
+
(300.0*exp(-0.042*(62.60700 * model.X_300[(i,j)] + 0.00 )))*2*4/((2*300.0*exp(-0.042*(62.60700 * model.X_300[(i,j)] + 0.00 )))+76.00+(2*300.0*exp(-0.042*(62.60700 * model.X_300[(i,j)] + 0.00 )))**2/2124.1800)
)*1.0/18.0
model.CoverConstrDifffI300= Constraint(ListElem,ListPoints, rule= CoverConstrDifffI300_rule)

def CoverConstrDifffI450_rule(model, i, j):
  return model.fI_450[(i,j)] == ( (450.0 * (exp(-0.084*(62.60700 * model.X_450[(i,j)] + 0.00))+1))/((450.0 * (exp(-0.084*(62.60700 * model.X_450[(i,j)] + 0.00))+1))+76.00+((450.0 * (exp(-0.084*(62.60700 * model.X_450[(i,j)] + 0.00))+1)))**2/2124.1800) * 2
+
(450.0 * (exp(-0.063*(62.60700 * model.X_450[(i,j)] + 0.00))+exp(-0.021 * (62.60700 * model.X_450[(i,j)] + 0.00))))/((450.0 * (exp(-0.063*(62.60700 * model.X_450[(i,j)] + 0.00))+exp(-0.021 * (62.60700 * model.X_450[(i,j)] + 0.00))))+76.00+(450.0 * (exp(-0.063*(62.60700 * model.X_450[(i,j)] + 0.00))+exp(-0.021 * (62.60700 * model.X_450[(i,j)] + 0.00))))**2/2124.1800) * 4
+
(450.0 * (exp(-0.0525*(62.60700 * model.X_450[(i,j)] + 0.00))+exp(-0.0315 * (62.60700 * model.X_450[(i,j)] + 0.00))))/((450.0 * (exp(-0.0525*(62.60700 * model.X_450[(i,j)] + 0.00))+exp(-0.0315 * (62.60700 * model.X_450[(i,j)] + 0.00))))+76.00+(450.0 * (exp(-0.0525*(62.60700 * model.X_450[(i,j)] + 0.00))+exp(-0.0315 * (62.60700 * model.X_450[(i,j)] + 0.00))))**2/2124.1800) * 4
+
(450.0 * (exp(-0.0735*(62.60700 * model.X_450[(i,j)] + 0.00))+exp(-0.0105* (62.60700 * model.X_450[(i,j)] + 0.00))))/((450.0 * (exp(-0.0735*(62.60700 * model.X_450[(i,j)] + 0.00))+exp(-0.0105 * (62.60700 * model.X_450[(i,j)] + 0.00))))+76.00+(450.0 * (exp(-0.0735*(62.60700 * model.X_450[(i,j)] + 0.00))+exp(-0.0105 * (62.60700 * model.X_450[(i,j)] + 0.00))))**2/2124.1800) * 4
+
(450.0*exp(-0.042*(62.60700 * model.X_450[(i,j)] + 0.00 )))*2*4/((2*450.0*exp(-0.042*(62.60700 * model.X_450[(i,j)] + 0.00 )))+76.00+(2*450.0*exp(-0.042*(62.60700 * model.X_450[(i,j)] + 0.00 )))**2/2124.1800)
)*1.0/18.0
model.CoverConstrDifffI450= Constraint(ListElem,ListPoints, rule= CoverConstrDifffI450_rule)

def CoverConstrDifffI600_rule(model, i, j):
  return model.fI_600[(i,j)] == ( (600.0 * (exp(-0.084*(62.60700 * model.X_600[(i,j)] + 0.00))+1))/((600.0 * (exp(-0.084*(62.60700 * model.X_600[(i,j)] + 0.00))+1))+76.00+((600.0 * (exp(-0.084*(62.60700 * model.X_600[(i,j)] + 0.00))+1)))**2/2124.1800) * 2
+
(600.0 * (exp(-0.063*(62.60700 * model.X_600[(i,j)] + 0.00))+exp(-0.021 * (62.60700 * model.X_600[(i,j)] + 0.00))))/((600.0 * (exp(-0.063*(62.60700 * model.X_600[(i,j)] + 0.00))+exp(-0.021 * (62.60700 * model.X_600[(i,j)] + 0.00))))+76.00+(600.0 * (exp(-0.063*(62.60700 * model.X_600[(i,j)] + 0.00))+exp(-0.021 * (62.60700 * model.X_600[(i,j)] + 0.00))))**2/2124.1800) * 4
+
(600.0 * (exp(-0.0525*(62.60700 * model.X_600[(i,j)] + 0.00))+exp(-0.0315 * (62.60700 * model.X_600[(i,j)] + 0.00))))/((600.0 * (exp(-0.0525*(62.60700 * model.X_600[(i,j)] + 0.00))+exp(-0.0315 * (62.60700 * model.X_600[(i,j)] + 0.00))))+76.00+(600.0 * (exp(-0.0525*(62.60700 * model.X_600[(i,j)] + 0.00))+exp(-0.0315 * (62.60700 * model.X_600[(i,j)] + 0.00))))**2/2124.1800) * 4
+
(600.0 * (exp(-0.0735*(62.60700 * model.X_600[(i,j)] + 0.00))+exp(-0.0105* (62.60700 * model.X_600[(i,j)] + 0.00))))/((600.0 * (exp(-0.0735*(62.60700 * model.X_600[(i,j)] + 0.00))+exp(-0.0105 * (62.60700 * model.X_600[(i,j)] + 0.00))))+76.00+(600.0 * (exp(-0.0735*(62.60700 * model.X_600[(i,j)] + 0.00))+exp(-0.0105 * (62.60700 * model.X_600[(i,j)] + 0.00))))**2/2124.1800) * 4
+
(600.0*exp(-0.042*(62.60700 * model.X_600[(i,j)] + 0.00 )))*2*4/((2*600.0*exp(-0.042*(62.60700 * model.X_600[(i,j)] + 0.00 )))+76.00+(2*600.0*exp(-0.042*(62.60700 * model.X_600[(i,j)] + 0.00 )))**2/2124.1800)
)*1.0/18.0
model.CoverConstrDifffI600= Constraint(ListElem,ListPoints, rule= CoverConstrDifffI600_rule)


# gI

def CoverConstrDiffgI150_rule(model, i, j):
  return model.gI_150[(i,j)] == ( (150.0 * (exp(-0.084*(62.60700 * model.X_150[(i,j)] + 0.00))+1))/((150.0 * (exp(-0.084*(62.60700 * model.X_150[(i,j)] + 0.00))+1))+model.ksL+((150.0 * (exp(-0.084*(62.60700 * model.X_150[(i,j)] + 0.00))+1)))**2/model.kiL) * 2
+
(150.0 * (exp(-0.063*(62.60700 * model.X_150[(i,j)] + 0.00))+exp(-0.021 * (62.60700 * model.X_150[(i,j)] + 0.00))))/((150.0 * (exp(-0.063*(62.60700 * model.X_150[(i,j)] + 0.00))+exp(-0.021 * (62.60700 * model.X_150[(i,j)] + 0.00))))+model.ksL+(150.0 * (exp(-0.063*(62.60700 * model.X_150[(i,j)] + 0.00))+exp(-0.021 * (62.60700 * model.X_150[(i,j)] + 0.00))))**2/model.kiL) * 4
+
(150.0 * (exp(-0.0525*(62.60700 * model.X_150[(i,j)] + 0.00))+exp(-0.0315 * (62.60700 * model.X_150[(i,j)] + 0.00))))/((150.0 * (exp(-0.0525*(62.60700 * model.X_150[(i,j)] + 0.00))+exp(-0.0315 * (62.60700 * model.X_150[(i,j)] + 0.00))))+model.ksL+(150.0 * (exp(-0.0525*(62.60700 * model.X_150[(i,j)] + 0.00))+exp(-0.0315 * (62.60700 * model.X_150[(i,j)] + 0.00))))**2/model.kiL) * 4
+
(150.0 * (exp(-0.0735*(62.60700 * model.X_150[(i,j)] + 0.00))+exp(-0.0105* (62.60700 * model.X_150[(i,j)] + 0.00))))/((150.0 * (exp(-0.0735*(62.60700 * model.X_150[(i,j)] + 0.00))+exp(-0.0105 * (62.60700 * model.X_150[(i,j)] + 0.00))))+model.ksL+(150.0 * (exp(-0.0735*(62.60700 * model.X_150[(i,j)] + 0.00))+exp(-0.0105 * (62.60700 * model.X_150[(i,j)] + 0.00))))**2/model.kiL) * 4
+
(150.0*exp(-0.042*(62.60700 * model.X_150[(i,j)] + 0.00 )))*2*4/((2*150.0*exp(-0.042*(62.60700 * model.X_150[(i,j)] + 0.00 )))+model.ksL+(2*150.0*exp(-0.042*(62.60700 * model.X_150[(i,j)] + 0.00 )))**2/model.kiL)
)*1.0/18.0
model.CoverConstrDiffgI150= Constraint(ListElem,ListPoints, rule= CoverConstrDiffgI150_rule)

def CoverConstrDiffgI300_rule(model, i, j):
  return model.gI_300[(i,j)] == ( (300.0 * (exp(-0.084*(62.60700 * model.X_300[(i,j)] + 0.00))+1))/((300.0 * (exp(-0.084*(62.60700 * model.X_300[(i,j)] + 0.00))+1))+model.ksL+((300.0 * (exp(-0.084*(62.60700 * model.X_300[(i,j)] + 0.00))+1)))**2/model.kiL) * 2
+
(300.0 * (exp(-0.063*(62.60700 * model.X_300[(i,j)] + 0.00))+exp(-0.021 * (62.60700 * model.X_300[(i,j)] + 0.00))))/((300.0 * (exp(-0.063*(62.60700 * model.X_300[(i,j)] + 0.00))+exp(-0.021 * (62.60700 * model.X_300[(i,j)] + 0.00))))+model.ksL+(300.0 * (exp(-0.063*(62.60700 * model.X_300[(i,j)] + 0.00))+exp(-0.021 * (62.60700 * model.X_300[(i,j)] + 0.00))))**2/model.kiL) * 4
+
(300.0 * (exp(-0.0525*(62.60700 * model.X_300[(i,j)] + 0.00))+exp(-0.0315 * (62.60700 * model.X_300[(i,j)] + 0.00))))/((300.0 * (exp(-0.0525*(62.60700 * model.X_300[(i,j)] + 0.00))+exp(-0.0315 * (62.60700 * model.X_300[(i,j)] + 0.00))))+model.ksL+(300.0 * (exp(-0.0525*(62.60700 * model.X_300[(i,j)] + 0.00))+exp(-0.0315 * (62.60700 * model.X_300[(i,j)] + 0.00))))**2/model.kiL) * 4
+
(300.0 * (exp(-0.0735*(62.60700 * model.X_300[(i,j)] + 0.00))+exp(-0.0105* (62.60700 * model.X_300[(i,j)] + 0.00))))/((300.0 * (exp(-0.0735*(62.60700 * model.X_300[(i,j)] + 0.00))+exp(-0.0105 * (62.60700 * model.X_300[(i,j)] + 0.00))))+model.ksL+(300.0 * (exp(-0.0735*(62.60700 * model.X_300[(i,j)] + 0.00))+exp(-0.0105 * (62.60700 * model.X_300[(i,j)] + 0.00))))**2/model.kiL) * 4
+
(300.0*exp(-0.042*(62.60700 * model.X_300[(i,j)] + 0.00 )))*2*4/((2*300.0*exp(-0.042*(62.60700 * model.X_300[(i,j)] + 0.00 )))+model.ksL+(2*300.0*exp(-0.042*(62.60700 * model.X_300[(i,j)] + 0.00 )))**2/model.kiL)
)*1.0/18.0
model.CoverConstrDiffgI300= Constraint(ListElem,ListPoints, rule= CoverConstrDiffgI300_rule)

def CoverConstrDiffgI450_rule(model, i, j):
  return model.gI_450[(i,j)] == ( (450.0 * (exp(-0.084*(62.60700 * model.X_450[(i,j)] + 0.00))+1))/((450.0 * (exp(-0.084*(62.60700 * model.X_450[(i,j)] + 0.00))+1))+model.ksL+((450.0 * (exp(-0.084*(62.60700 * model.X_450[(i,j)] + 0.00))+1)))**2/model.kiL) * 2
+
(450.0 * (exp(-0.063*(62.60700 * model.X_450[(i,j)] + 0.00))+exp(-0.021 * (62.60700 * model.X_450[(i,j)] + 0.00))))/((450.0 * (exp(-0.063*(62.60700 * model.X_450[(i,j)] + 0.00))+exp(-0.021 * (62.60700 * model.X_450[(i,j)] + 0.00))))+model.ksL+(450.0 * (exp(-0.063*(62.60700 * model.X_450[(i,j)] + 0.00))+exp(-0.021 * (62.60700 * model.X_450[(i,j)] + 0.00))))**2/model.kiL) * 4
+
(450.0 * (exp(-0.0525*(62.60700 * model.X_450[(i,j)] + 0.00))+exp(-0.0315 * (62.60700 * model.X_450[(i,j)] + 0.00))))/((450.0 * (exp(-0.0525*(62.60700 * model.X_450[(i,j)] + 0.00))+exp(-0.0315 * (62.60700 * model.X_450[(i,j)] + 0.00))))+model.ksL+(450.0 * (exp(-0.0525*(62.60700 * model.X_450[(i,j)] + 0.00))+exp(-0.0315 * (62.60700 * model.X_450[(i,j)] + 0.00))))**2/model.kiL) * 4
+
(450.0 * (exp(-0.0735*(62.60700 * model.X_450[(i,j)] + 0.00))+exp(-0.0105* (62.60700 * model.X_450[(i,j)] + 0.00))))/((450.0 * (exp(-0.0735*(62.60700 * model.X_450[(i,j)] + 0.00))+exp(-0.0105 * (62.60700 * model.X_450[(i,j)] + 0.00))))+model.ksL+(450.0 * (exp(-0.0735*(62.60700 * model.X_450[(i,j)] + 0.00))+exp(-0.0105 * (62.60700 * model.X_450[(i,j)] + 0.00))))**2/model.kiL) * 4
+
(450.0*exp(-0.042*(62.60700 * model.X_450[(i,j)] + 0.00 )))*2*4/((2*450.0*exp(-0.042*(62.60700 * model.X_450[(i,j)] + 0.00 )))+model.ksL+(2*450.0*exp(-0.042*(62.60700 * model.X_450[(i,j)] + 0.00 )))**2/model.kiL)
)*1.0/18.0
model.CoverConstrDiffgI450= Constraint(ListElem,ListPoints, rule= CoverConstrDiffgI450_rule)

def CoverConstrDiffgI600_rule(model, i, j):
  return model.gI_600[(i,j)] == ( (600.0 * (exp(-0.084*(62.60700 * model.X_600[(i,j)] + 0.00))+1))/((600.0 * (exp(-0.084*(62.60700 * model.X_600[(i,j)] + 0.00))+1))+model.ksL+((600.0 * (exp(-0.084*(62.60700 * model.X_600[(i,j)] + 0.00))+1)))**2/model.kiL) * 2
+
(600.0 * (exp(-0.063*(62.60700 * model.X_600[(i,j)] + 0.00))+exp(-0.021 * (62.60700 * model.X_600[(i,j)] + 0.00))))/((600.0 * (exp(-0.063*(62.60700 * model.X_600[(i,j)] + 0.00))+exp(-0.021 * (62.60700 * model.X_600[(i,j)] + 0.00))))+model.ksL+(600.0 * (exp(-0.063*(62.60700 * model.X_600[(i,j)] + 0.00))+exp(-0.021 * (62.60700 * model.X_600[(i,j)] + 0.00))))**2/model.kiL) * 4
+
(600.0 * (exp(-0.0525*(62.60700 * model.X_600[(i,j)] + 0.00))+exp(-0.0315 * (62.60700 * model.X_600[(i,j)] + 0.00))))/((600.0 * (exp(-0.0525*(62.60700 * model.X_600[(i,j)] + 0.00))+exp(-0.0315 * (62.60700 * model.X_600[(i,j)] + 0.00))))+model.ksL+(600.0 * (exp(-0.0525*(62.60700 * model.X_600[(i,j)] + 0.00))+exp(-0.0315 * (62.60700 * model.X_600[(i,j)] + 0.00))))**2/model.kiL) * 4
+
(600.0 * (exp(-0.0735*(62.60700 * model.X_600[(i,j)] + 0.00))+exp(-0.0105* (62.60700 * model.X_600[(i,j)] + 0.00))))/((600.0 * (exp(-0.0735*(62.60700 * model.X_600[(i,j)] + 0.00))+exp(-0.0105 * (62.60700 * model.X_600[(i,j)] + 0.00))))+model.ksL+(600.0 * (exp(-0.0735*(62.60700 * model.X_600[(i,j)] + 0.00))+exp(-0.0105 * (62.60700 * model.X_600[(i,j)] + 0.00))))**2/model.kiL) * 4
+
(600.0*exp(-0.042*(62.60700 * model.X_600[(i,j)] + 0.00 )))*2*4/((2*600.0*exp(-0.042*(62.60700 * model.X_600[(i,j)] + 0.00 )))+model.ksL+(2*600.0*exp(-0.042*(62.60700 * model.X_600[(i,j)] + 0.00 )))**2/model.kiL)
)*1.0/18.0
model.CoverConstrDiffgI600= Constraint(ListElem,ListPoints, rule= CoverConstrDiffgI600_rule)


#------------------ Additional Constraints -----------------#

model.con2 = Constraint(expr = model.ksL <= model.kiL )

print 'lu_450innit[(element,0)] = ',(lu_450innit[(1,0)])


X150_guess_list=[]
X300_guess_list=[]
X450_guess_list=[]
X600_guess_list=[]

N150_guess_list=[]
N300_guess_list=[]
N450_guess_list=[]
N600_guess_list=[]

Lu150_guess_list=[]
Lu300_guess_list=[]
Lu450_guess_list=[]
Lu600_guess_list=[]

fI150_guess_list=[]
fI300_guess_list=[]
fI450_guess_list=[]
fI600_guess_list=[]

	
for element in range(0,Elements+1):

  X150_guess_list.append(x_150innit[(element,0)])
  X300_guess_list.append(x_300innit[(element,0)])
  X450_guess_list.append(x_450innit[(element,0)])
  X600_guess_list.append(x_600innit[(element,0)])

  N150_guess_list.append(n_150innit[(element,0)])
  N300_guess_list.append(n_300innit[(element,0)])
  N450_guess_list.append(n_450innit[(element,0)])
  N600_guess_list.append(n_600innit[(element,0)])

  Lu150_guess_list.append(lu_150innit[(element,0)])
  Lu300_guess_list.append(lu_300innit[(element,0)])
  Lu450_guess_list.append(lu_450innit[(element,0)])
  Lu600_guess_list.append(lu_600innit[(element,0)])

  fI150_guess_list.append(fI_150innit[(element,0)])
  fI300_guess_list.append(fI_300innit[(element,0)])
  fI450_guess_list.append(fI_450innit[(element,0)])
  fI600_guess_list.append(fI_600innit[(element,0)])

#print "len(X75_list) = ",len(X75_list)
#print "len(time_list) = ",len(time_list)
	
fig=matplotlib.pyplot.figure(figsize=(18,4))
# (2,6)<- total (fila,columna),(fila,columna)

plt.subplot2grid((4,8),(0,0),colspan=2)
plt.plot(time_list,X150_guess_list)
plt.plot([0, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144],[0.077, 0.1715, 0.2498, 0.4045, 0.5874, 0.7426, 0.9118, 1.0584, 1.1149, 1.1919, 1.3063, 1.3352, 1.4414],'ro' )
plt.ylabel('X 150',rotation= 360,fontsize=15)
plt.xlabel('time',fontsize=15)

plt.subplot2grid((4,8),(0,2),colspan=2)
plt.plot(time_list,X300_guess_list)
plt.plot([0, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144], [0.077, 0.2067, 0.4593, 0.6191, 0.9408, 1.1327, 1.3546, 1.5643, 1.6803, 1.867, 2.0856, 2.0902, 2.2181],'ro' )
plt.ylabel('X 300',rotation= 360,fontsize=15)
plt.xlabel('time',fontsize=15)

plt.subplot2grid((4,8),(0,4),colspan=2)
plt.plot(time_list,X450_guess_list)
plt.plot([0, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144],[0.077, 0.1772, 0.2323, 0.401, 0.6518, 0.9769, 1.1603, 1.3322, 1.6307, 1.8684, 2.0537, 2.1806, 2.2851],'ro' )
plt.ylabel('X 450',rotation= 360,fontsize=15)
plt.xlabel('time',fontsize=15)

plt.subplot2grid((4,8),(0,6),colspan=2)
plt.plot(time_list,X600_guess_list)
plt.plot([0, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144],[0.077, 0.2458, 0.5945, 0.8218, 1.0512, 1.3269, 1.6084, 1.8375, 2.0981, 2.2753, 2.4609, 2.5819, 2.6911],'ro' )
plt.ylabel('X 600',rotation= 360,fontsize=15)
plt.xlabel('time',fontsize=15)

###

plt.subplot2grid((4,8),(1,0),colspan=2)
plt.plot(time_list,N150_guess_list)
plt.plot([0, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144],[783.2, 758.3, 695.8, 608.1, 509.9, 460.4, 677.6, 949, 1153.1, 1427.5, 1601, 1867.2, 2614.3],'ro' )
plt.ylabel('N 150',rotation= 360,fontsize=15)
plt.xlabel('time',fontsize=15)

plt.subplot2grid((4,8),(1,2),colspan=2)
plt.plot(time_list,N300_guess_list)
plt.plot([0, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144], [783.5, 759.6, 599.2, 481.4, 383.6, 319.9, 517.7, 859.7, 1089.6, 1372.4, 1612.9, 1848.7, 2608.9],'ro' )
plt.ylabel('N 300',rotation= 360,fontsize=15)
plt.xlabel('time',fontsize=15)

plt.subplot2grid((4,8),(1,4),colspan=2)
plt.plot(time_list,N450_guess_list)
plt.plot( [0, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144], [784.4, 762.9, 744.8, 646.9, 484.2, 335.8, 638.4, 940.2, 1148.3, 1330.4, 1484.6, 1667.8, 1885.1],'ro' )
plt.ylabel('N 450',rotation= 360,fontsize=15)
plt.xlabel('time',fontsize=15)

plt.subplot2grid((4,8),(1,6),colspan=2)
plt.plot(time_list,N600_guess_list)
plt.plot( [00, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144], [783.3, 709.5, 465.6, 465.7, 335.8, 215, 460.3, 730.9, 947.9, 1150.6, 1328.6, 1537.4, 1753.6],'ro' )
plt.ylabel('N 600',rotation= 360,fontsize=15)
plt.xlabel('time',fontsize=15)

###

plt.subplot2grid((4,8),(2,0),colspan=2)
plt.plot(time_list,fI150_guess_list)
plt.ylabel('fI 150',rotation= 360,fontsize=15)
plt.xlabel('time',fontsize=15)

plt.subplot2grid((4,8),(2,2),colspan=2)
plt.plot(time_list,fI300_guess_list)
plt.ylabel('fI 300',rotation= 360,fontsize=15)
plt.xlabel('time',fontsize=15)

plt.subplot2grid((4,8),(2,4),colspan=2)
plt.plot(time_list,fI450_guess_list)
plt.ylabel('fI 450',rotation= 360,fontsize=15)
plt.xlabel('time',fontsize=15)

plt.subplot2grid((4,8),(2,6),colspan=2)
plt.plot(time_list,fI600_guess_list)
plt.ylabel('fI 600',rotation= 360,fontsize=15)
plt.xlabel('time',fontsize=15)

###

plt.subplot2grid((4,8),(3,0),colspan=2)
plt.plot(time_list,Lu150_guess_list)
plt.plot([0, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144],[0.0, 0.0, 0.92, 0.57, 0.44, 0.36, 0.296, 0.265, 0.26, 0.235, 0.23, 0.18, 0.153],'ro' )
plt.ylabel('Lu 150',rotation= 360,fontsize=15)
plt.xlabel('time',fontsize=15)

plt.subplot2grid((4,8),(3,2),colspan=2)
plt.plot(time_list,Lu300_guess_list)
plt.plot([0, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144],[0.0, 0.0, 2.11, 1.94, 1.53, 1.4, 1.39, 1.27, 1.28, 1.28, 1.22, 1.3, 1.25],'ro' )
plt.ylabel('Lu 300',rotation= 360,fontsize=15)
plt.xlabel('time',fontsize=15)

plt.subplot2grid((4,8),(3,4),colspan=2)
plt.plot(time_list,Lu450_guess_list)
plt.plot([0, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144],[0.0, 0.0, 1.076, 1.043, 1.33, 0.89, 0.81, 0.81, 0.83, 0.9, 0.95, 1.01, 0.906],'ro' )
plt.ylabel('Lu 450',rotation= 360,fontsize=15)
plt.xlabel('time',fontsize=15)

plt.subplot2grid((4,8),(3,6),colspan=2)
plt.plot(time_list,Lu600_guess_list)
plt.plot([0, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144],[0.0, 0.0, 0.673, 0.681, 0.599, 0.656, 0.703, 0.767, 0.74, 0.76, 0.66, 0.558, 0.49],'ro' )
plt.ylabel('Lu 600',rotation= 360,fontsize=15)
plt.xlabel('time',fontsize=15)

subplots_adjust(left=0.05,right=0.95,top=0.9,bottom=0.14,wspace=0.7)

plt.savefig('initial_points.png')

print "creating model ..."
instance = model.create()
print "optimizing model ..."
opt = SolverFactory("ipopt")
print "compiling results ..."
results = opt.solve(instance)
instance.load(results)

print "ksL = ",instance.ksL.value
print "kiL = ",instance.kiL.value
print "k = ",instance.k.value
print "kd = ",instance.kd.value
print "km = ",instance.km.value

X150_list=[]
X300_list=[]
X450_list=[]
X600_list=[]

X150_guess_list=[]
X300_guess_list=[]
X450_guess_list=[]
X600_guess_list=[]

N150_list=[]
N300_list=[]
N450_list=[]
N600_list=[]

N150_guess_list=[]
N300_guess_list=[]
N450_guess_list=[]
N600_guess_list=[]

q150_list=[]
q300_list=[]
q450_list=[]
q600_list=[]

Lu150_list=[]
Lu300_list=[]
Lu450_list=[]
Lu600_list=[]

Lu150_guess_list=[]
Lu300_guess_list=[]
Lu450_guess_list=[]
Lu600_guess_list=[]

fI150_guess_list=[]
fI300_guess_list=[]
fI450_guess_list=[]
fI600_guess_list=[]

gI150_guess_list=[]
gI300_guess_list=[]
gI450_guess_list=[]
gI600_guess_list=[]

	
for element in range(0,Elements+1):
  X150_list.append(instance.X_150[(element,1)].value)
  X300_list.append(instance.X_300[(element,1)].value)
  X450_list.append(instance.X_450[(element,0)].value)
  X600_list.append(instance.X_600[(element,0)].value)

  X150_guess_list.append(x_150innit[(element,1)])
  X300_guess_list.append(x_300innit[(element,1)])
  X450_guess_list.append(x_450innit[(element,0)])
  X600_guess_list.append(x_600innit[(element,0)])

  N150_list.append(instance.N_150[(element,1)].value)
  N300_list.append(instance.N_300[(element,1)].value)
  N450_list.append(instance.N_450[(element,0)].value)
  N600_list.append(instance.N_600[(element,0)].value)

  N150_guess_list.append(n_150innit[(element,1)])
  N300_guess_list.append(n_300innit[(element,1)])
  N450_guess_list.append(n_450innit[(element,0)])
  N600_guess_list.append(n_600innit[(element,0)])

  Lu150_list.append(instance.Lu_150[(element,1)].value)
  Lu300_list.append(instance.Lu_300[(element,1)].value)
  Lu450_list.append(instance.Lu_450[(element,0)].value)
  Lu600_list.append(instance.Lu_600[(element,0)].value)

  Lu150_guess_list.append(lu_150innit[(element,1)])
  Lu300_guess_list.append(lu_300innit[(element,1)])
  Lu450_guess_list.append(lu_450innit[(element,0)])
  Lu600_guess_list.append(lu_600innit[(element,0)])

  fI150_guess_list.append(fI_150innit[(element,1)])
  fI300_guess_list.append(fI_300innit[(element,1)])
  fI450_guess_list.append(fI_450innit[(element,0)])
  fI600_guess_list.append(fI_600innit[(element,0)])

  gI150_guess_list.append(gI_150innit[(element,1)])
  gI300_guess_list.append(gI_300innit[(element,1)])
  gI450_guess_list.append(gI_450innit[(element,0)])
  gI600_guess_list.append(gI_600innit[(element,0)])

#print "len(X75_list) = ",len(X75_list)
#print "len(time_list) = ",len(time_list)
	
fig=matplotlib.pyplot.figure(figsize=(18,4))
# (2,6)<- total (fila,columna),(fila,columna)

plt.subplot2grid((4,8),(0,0),colspan=2)
plt.plot(time_list,X150_list)
plt.plot(time_list,X150_guess_list)
plt.plot([0, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144],[0.077, 0.1715, 0.2498, 0.4045, 0.5874, 0.7426, 0.9118, 1.0584, 1.1149, 1.1919, 1.3063, 1.3352, 1.4414],'ro' )
plt.ylabel('X 150',rotation= 360,fontsize=15)
plt.xlabel('time',fontsize=15)

plt.subplot2grid((4,8),(0,2),colspan=2)
plt.plot(time_list,X300_list)
plt.plot(time_list,X300_guess_list)
plt.plot([0, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144], [0.077, 0.2067, 0.4593, 0.6191, 0.9408, 1.1327, 1.3546, 1.5643, 1.6803, 1.867, 2.0856, 2.0902, 2.2181],'ro' )
plt.ylabel('X 300',rotation= 360,fontsize=15)
plt.xlabel('time',fontsize=15)

plt.subplot2grid((4,8),(0,4),colspan=2)
plt.plot(time_list,X450_list)
plt.plot(time_list,X450_guess_list)
plt.plot([0, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144],[0.077, 0.1772, 0.2323, 0.401, 0.6518, 0.9769, 1.1603, 1.3322, 1.6307, 1.8684, 2.0537, 2.1806, 2.2851],'ro' )
plt.ylabel('X 450',rotation= 360,fontsize=15)
plt.xlabel('time',fontsize=15)

plt.subplot2grid((4,8),(0,6),colspan=2)
plt.plot(time_list,X600_list)
plt.plot(time_list,X600_guess_list)
plt.plot([0, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144],[0.077, 0.2458, 0.5945, 0.8218, 1.0512, 1.3269, 1.6084, 1.8375, 2.0981, 2.2753, 2.4609, 2.5819, 2.6911],'ro' )
plt.ylabel('X 600',rotation= 360,fontsize=15)
plt.xlabel('time',fontsize=15)

###

plt.subplot2grid((4,8),(1,0),colspan=2)
plt.plot(time_list,N150_list)
plt.plot(time_list,N150_guess_list)
plt.plot([0, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144],[783.2, 758.3, 695.8, 608.1, 509.9, 460.4, 677.6, 949, 1153.1, 1427.5, 1601, 1867.2, 2614.3],'ro' )
plt.ylabel('N 150',rotation= 360,fontsize=15)
plt.xlabel('time',fontsize=15)

plt.subplot2grid((4,8),(1,2),colspan=2)
plt.plot(time_list,N300_list)
plt.plot(time_list,N300_guess_list)
plt.plot([0, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144], [783.5, 759.6, 599.2, 481.4, 383.6, 319.9, 517.7, 859.7, 1089.6, 1372.4, 1612.9, 1848.7, 2608.9],'ro' )
plt.ylabel('N 300',rotation= 360,fontsize=15)
plt.xlabel('time',fontsize=15)

plt.subplot2grid((4,8),(1,4),colspan=2)
plt.plot(time_list,N450_list)
plt.plot(time_list,N450_guess_list)
plt.plot( [0, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144], [784.4, 762.9, 744.8, 646.9, 484.2, 335.8, 638.4, 940.2, 1148.3, 1330.4, 1484.6, 1667.8, 1885.1],'ro' )
plt.ylabel('N 450',rotation= 360,fontsize=15)
plt.xlabel('time',fontsize=15)

plt.subplot2grid((4,8),(1,6),colspan=2)
plt.plot(time_list,N600_list)
plt.plot(time_list,N600_guess_list)
plt.plot( [0, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144], [783.3, 709.5, 465.6, 465.7, 335.8, 215, 460.3, 730.9, 947.9, 1150.6, 1328.6, 1537.4, 1753.6],'ro' )
plt.ylabel('N 600',rotation= 360,fontsize=15)
plt.xlabel('time',fontsize=15)

###

plt.subplot2grid((4,8),(2,0),colspan=2)
plt.plot(time_list,fI150_guess_list)
plt.ylabel('gI 150',rotation= 360,fontsize=15)
plt.xlabel('time',fontsize=15)

plt.subplot2grid((4,8),(2,2),colspan=2)
plt.plot(time_list,fI300_guess_list)
plt.ylabel('gI 300',rotation= 360,fontsize=15)
plt.xlabel('time',fontsize=15)

plt.subplot2grid((4,8),(2,4),colspan=2)
plt.plot(time_list,fI450_guess_list)
plt.ylabel('gI 450',rotation= 360,fontsize=15)
plt.xlabel('time',fontsize=15)

plt.subplot2grid((4,8),(2,6),colspan=2)
plt.plot(time_list,fI600_guess_list)
plt.ylabel('gI 600',rotation= 360,fontsize=15)
plt.xlabel('time',fontsize=15)
###

plt.subplot2grid((4,8),(3,0),colspan=2)
plt.plot(time_list,Lu150_list)
plt.plot(time_list,Lu150_guess_list)
plt.plot([0, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144],[0.0, 0.0, 0.92, 0.57, 0.44, 0.36, 0.296, 0.265, 0.26, 0.235, 0.23, 0.18, 0.153],'ro' )
plt.ylabel('Lu 150',rotation= 360,fontsize=15)
plt.xlabel('time',fontsize=15)

plt.subplot2grid((4,8),(3,2),colspan=2)
plt.plot(time_list,Lu300_list)
plt.plot(time_list,Lu300_guess_list)
plt.plot([0, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144],[0.0, 0.0, 2.11, 1.94, 1.53, 1.4, 1.39, 1.27, 1.28, 1.28, 1.22, 1.3, 1.25],'ro' )
plt.ylabel('Lu 300',rotation= 360,fontsize=15)
plt.xlabel('time',fontsize=15)

plt.subplot2grid((4,8),(3,4),colspan=2)
plt.plot(time_list,Lu450_list)
plt.plot(time_list,Lu450_guess_list)
plt.plot([0, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144],[0.0, 0.0, 1.076, 1.043, 1.33, 0.89, 0.81, 0.81, 0.83, 0.9, 0.95, 1.01, 0.906],'ro' )
plt.ylabel('Lu 450',rotation= 360,fontsize=15)
plt.xlabel('time',fontsize=15)

plt.subplot2grid((4,8),(3,6),colspan=2)
plt.plot(time_list,Lu600_list)
plt.plot(time_list,Lu600_guess_list)
plt.plot([0, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144],[0.0, 0.0, 0.673, 0.681, 0.599, 0.656, 0.703, 0.767, 0.74, 0.76, 0.66, 0.558, 0.49],'ro' )
plt.ylabel('Lu 600',rotation= 360,fontsize=15)
plt.xlabel('time',fontsize=15)

subplots_adjust(left=0.05,right=0.95,top=0.9,bottom=0.14,wspace=0.7)
plt.savefig('run_simple.png')
plt.show()
    
