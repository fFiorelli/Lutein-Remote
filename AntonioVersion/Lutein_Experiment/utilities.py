import numpy as np

def standardizer(var_list):
    #applies the Standard Score
    test_list=[]
    test_list=np.array(var_list,dtype='float64')
    
    test_list_2=[]
    #list_norm=numpy.linalg.norm(test_list0)
    
    test_mean=np.mean(test_list)
    test_dev=np.std(test_list)

    if test_dev > 0.00001:
        for j in xrange(0,len(var_list)):    
            test_list_2.append((float(var_list[j])-test_mean)/test_dev )
    else:
        test_list_2=numpy.zeros(len(test_list))
    
    return np.array(test_list_2,dtype='float64')

def normalizer(var_list):
    #applies the Standard Score
    test_list=[]
    test_list=np.array(var_list,dtype='float64')
    
    test_list_2=[]
    #list_norm=numpy.linalg.norm(test_list0)
    
    test_Min=min(test_list)
    test_Max=max(test_list)
    for j in xrange(0,len(var_list)):
        test_list_2.append((float(var_list[j])-test_Min)/(test_Max-test_Min))

    return np.array(test_list_2,dtype='float64')
