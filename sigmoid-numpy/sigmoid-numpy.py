import numpy as np
import math
def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    if(type(x)==list):
        x1=np.asarray(x,dtype=float)
        # for i in x1:
        #     x1[]=1/1+(np.exp(-x))
        x1=np.asarray((list(map((lambda x:(1/(1+np.exp(-x)))),x1))),dtype=float)
        return x1
    else:
        return 1/(1+np.exp(-x))
    pass