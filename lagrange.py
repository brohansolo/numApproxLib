###################
### lagrange.py ###
###################

import numpy as np
# Creates a lagrange polynomial output out two numpy arrays
# One array for x-coordinates and one array for y-coordinates

def polynomial(x_coord, y_coord):

    if x_coord.shape[0] != y_coord.shape[0]:
       return False

    full_poly = np.poly1d(0)

    iter_i = 0
    for _ in x_coord:

        coeff = y_coord[iter_i] 

        iter_j = 0
        for _ in x_coord:
                if iter_i != iter_j:
                    val = 1 / (x_coord[iter_i] 
                                    - x_coord[iter_j])  # Calculates 1/(x_i - x_j)
                    coeff = coeff * val # Multiplies them into the coeff
                iter_j += 1
                
        poly_term = np.poly1d(np.delete(x_coord, iter_i), True)
        # print('term', iter_i, ':', poly_term, '\n')
        poly_term = coeff*poly_term
        full_poly += poly_term
        iter_i += 1

    return full_poly
        

                   