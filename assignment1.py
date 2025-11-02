# assignment1.py
import math

def find_period(L0, L1):
    """
    Print the pendulum period for integer lengths from L0 to L1 (inclusive),
    and return the period for L0 and L1 as a tuple (T0, T1).

    L0 and L1 are expected to be integers with 0 < L0 < L1.
    """
    
    if not (isinstance(L0, int) and isinstance(L1, int)):
        raise TypeError("L0 and L1 must be integers.")
    if not (0 < L0 < L1):
        raise ValueError("Require integers with 0 < L0 < L1.")

    g = 9.81  # m/s^2

    def period(L):
        return 2 * math.pi * math.sqrt(L / g)

  
    for L in range(L0, L1 + 1):
        T = period(L)
        
        print(f"When L = {L:4.1f} m, T = {T:3.1f} s")

   
    return period(L0), period(L1)



if __name__ == "__main__":
    T0, T1 = find_period(2, 10)
   


