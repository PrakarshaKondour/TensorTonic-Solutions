import numpy as np
def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    a=np.array(a)
    b=np.array(b)
    if(len(a)==len(b)):
        scalar=0
        for i in range(len(a)):
            scalar+=a[i]*b[i]
        magasq=0
        for x in a:
            magasq+=x*x
        magbsq=0
        for x in b:
            magbsq+=x*x
        if((magasq==0) or (magbsq==0)):
            return 0
        return scalar/(np.sqrt(magasq)*np.sqrt(magbsq))    
    pass