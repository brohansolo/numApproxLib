######################
### powerseries.py ###
######################

# This function takes in a set of x-coordinates and y-coordinates as 1D numpy arrays
# And outputs an power series interpolating polynomial

import numpy as np
#import matplotlib.pyplot as plt

def polynomial(x_coord, y_coord):

   # x_coord and y_coord are numpy matrices

    if x_coord.shape[0] != y_coord.shape[0]:
            return 0

    vander_matrix = np.vander(x_coord, x_coord.shape[0])
    vect_pol = np.linalg.solve(vander_matrix, y_coord)

    final_poly = np.poly1d(vect_pol)

    return final_poly

x = np.array([1, 0, -1])
y = np.array([2, 0, 0])

print(polynomial(x, y))
