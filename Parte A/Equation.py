import numpy as np
# ecuación en forma de función
k = np.log(2)
Ta = 70

def f(T):
    return -k*(T - Ta)
