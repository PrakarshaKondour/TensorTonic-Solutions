import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    sum=0
    if(len(x)==len(y)):
        for i in range(len(x)):
                sum+=(y[i]-x[i])*(y[i]-x[i])
        return np.sqrt(sum) 
    raise ValueError   
    pass