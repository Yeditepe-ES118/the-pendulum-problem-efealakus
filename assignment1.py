# assignment1.py

import math

def find_period(L0, L1):
    g = 9.81 

    
    for L in range(L0, L1 + 1):
        T = 2 * math.pi * math.sqrt(L / g)
        print("When L =", float(L), "m, T =", round(T, 1), "s")

  
    T0 = 2 * math.pi * math.sqrt(L0 / g)
    T1 = 2 * math.pi * math.sqrt(L1 / g)

    return T0, T1
find_period(2, 10)
