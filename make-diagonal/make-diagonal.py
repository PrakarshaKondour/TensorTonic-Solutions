import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Write code here
    v1=np.zeros((len(v),len(v)))
    v1=np.diag(v)
    for i in range(len(v1)):
        for j in range(len(v1)):
            if(i==j):
                v1[i][i]=v[i]
    return v1                
    pass
