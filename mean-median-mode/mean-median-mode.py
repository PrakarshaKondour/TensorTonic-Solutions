import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    if(len(x)>=1):
        x=np.array(x)
        
        d={}
        for i in x:
            if(i in d.keys()):
                d[i]=d[i]+1
            else:
                d[i]=1
            # d[i]=d.get(i,0)+1
        # print(d)        
        max=0
        for k in d.values():
            if(max<k):
                max=k
        keyformax=0
        for key,val in d.items():
            if(val==max):
                keyformax=key
                break
        x1=np.sort(x)
        median=0
        if(len(x1)%2!=0):
            median=x1[(len(x1)//2)]
        else:
            median=(x1[(len(x1)//2)]+x1[(len(x1)//2)-1])/2
        return np.mean(x),median,keyformax
    return x[0],x[0],x[0]    
    pass