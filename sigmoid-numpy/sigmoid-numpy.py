import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    arr=np.array(x,dtype=float)
    return 1/(1+np.exp(-arr))
    pass