######################
### poly_interp.py ###
######################

import numpy as np

#---------------------#
# Power Series Method #
#---------------------#
def powerseries(x_coord, y_coord):

   # x_coord and y_coord are numpy matrices

    if x_coord.shape[0] != y_coord.shape[0]:
            return 0

    vander_matrix = np.vander(x_coord, x_coord.shape[0]) # creates a vandermonde matrix with passed x-values
    vect_pol = np.linalg.solve(vander_matrix, y_coord)   # solves the vandermonde matrix w.r.t. y values
                                                            # (Ouputs a vector)
    final_poly = np.poly1d(vect_pol)
    return final_poly

#-----------------#
# Lagrange Method #
#-----------------#
def lagrange(x_coord, y_coord):

    if x_coord.shape[0] != y_coord.shape[0]:
       return False

    full_poly = np.poly1d(0)

    iter_i = 0
    for _ in x_coord:
        coeff = y_coord[iter_i]     # Re-initializes coefficient to f(x_i) for new lagrange term

        iter_j = 0
        for _ in x_coord:
                if iter_i != iter_j:
                    val = 1 / (x_coord[iter_i] - 
                                    x_coord[iter_j])    # calculates 1/(x_i - x_j)
                    coeff = coeff * val                 # multiplies previous to the coefficient
                iter_j += 1
                
        poly_term = np.poly1d(np.delete(x_coord, iter_i), True) # creates a polynomial from terms in x-coord (excluding the current term)
        poly_term = coeff*poly_term # multiplies coefficient into polynomial created
        full_poly += poly_term
        iter_i += 1
    
    return full_poly