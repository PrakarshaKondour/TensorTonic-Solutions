import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    # Write code here
    if(type(x)==list):
        x1=np.asarray(x,dtype=float)
        x1=np.asarray(list(map(lambda x:(np.maximum(0,x)),x1)),dtype=float)
        return x1
    else:
        return np.maximum(0,x)
    pass