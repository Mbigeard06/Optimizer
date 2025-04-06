import numpy as np

def sphere(dim=3):
    def func(x):
        return np.sum(x**2)
    def grad(x):
        return 2*x
    return func,  grad

def rastrigin(dim=3):
    def func(x):
        return 10 * dim + np.sum(np.pow(x, 2) - 10 * np.cos(2 * np.pi * x))
    def grad(x): 
        return 2 * x + 20 * np.pi * np.sin(2 * np.pi * x)
    return func, grad