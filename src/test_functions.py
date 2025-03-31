import numpy as np

def sphere(dim=3):
    def func(x):
        return np.sum(x**2)
    def grad(x):
        return 2*x
    return func,  grad