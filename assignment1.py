import numpy as np
def find_period(L0, L1):
    if L1 > L0 > 0:
        g = 9.81 #in m/s^2
        for l in range(L0, L1+1, 1):
            t = 2 * np.pi * np.sqrt(l/g)
            print("When L = %4.1f m, T = %.1f s" % (l, t))
        
        T0 = 2 * np.pi * np.sqrt(L0/g)
        T1= 2 * np.pi * np.sqrt(L1/g)
        return (T0, T1)