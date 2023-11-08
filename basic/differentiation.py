import numpy as np

def numerical_differentiation(f, x, h = 1e-4):
    return (f(x + h) - f(x - h)) / (2 * h)

def numerical_gradient(f, x, h = 1e-4):
    grad = np.zeros_like(x)
    
    for idx in range(x.size):
        tmp_val = x[idx]
        
        x[idx] = tmp_val + h
        fxh_forward = f(x)
        
        x[idx] = tmp_val - h
        fxh_backward = f(x)
        
        grad[idx] = (fxh_forward - fxh_backward) / (2 * h)
        x[idx] = tmp_val
        
    return grad
