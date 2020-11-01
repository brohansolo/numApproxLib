####################
### poissonDE.py ###
####################

# this function outputs a numpy array with n values each of which approximates the function specified in the domain specified
# using the dirichlet boundary conditions 

import numpy as np

def approximate(func, beg, end, num_nodes):
    constdiff = (end - beg)/(num_nodes+1) # h

    # initializing rhs
    fvals = np.arange(beg + constdiff, end, constdiff)
    mult = 0
    for _ in fvals:
        fvals[mult] = constdiff**2 * func(fvals[mult]) # h^2*f_i
        mult += 1
    
    # initializing lhs
    # Creates 2D array of coefficients for each node we approximate
    ucoeffs = np.zeros( (num_nodes, num_nodes))
    x = 0
    y = 0
    for _ in range(0, num_nodes):
        for _ in range(0, num_nodes):

            ucoeffs[x][y] = 2
            if (x != 0): 
                ucoeffs[x-1][y] = -1
            if (x != num_nodes-1):
                ucoeffs[x+1][y] = -1
            break

        y += 1 
        x += 1

    # solving the linear system
    soln = np.linalg.solve(ucoeffs, fvals)

    return soln

