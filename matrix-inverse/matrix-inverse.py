import numpy as np

def matrix_inverse(A):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    # Write code here
    a=np.array(A)
    if(np.linalg.det(a)==0):
        return None
    return np.linalg.inv(a)
    pass
