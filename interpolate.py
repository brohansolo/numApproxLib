######################
### interpolate.py ###
######################

import math
import numpy as np

import poly_interp
import nodes

def do(func, node_type, interp_type, beg, end, numnodes):

    thesenodes = [0]

    #nodes = np.array([0])

    if node_type == 'equal':
        thesenodes = nodes.equal(beg, end, numnodes)
    elif node_type == 'chebyshev':
        thesenodes = nodes.chebyshev(beg, end, numnodes)
    else:
        print('Inappropriate node type! Choose from either "equal" or "chebyshev"')
        return
    
    fnodes = f_vals(func, thesenodes)
    
    if interp_type == 'lagrange':
        return poly_interp.lagrange(thesenodes, fnodes)
    elif interp_type == 'powerseries':
        return poly_interp.powerseries(thesenodes, fnodes)
    else:
        print('Inappropriate Interpolation Type! Choose from either "lagrange" or "powerseries"')
        return
    return 

def f_vals(func, arr):
    evals = np.zeros(arr.shape[0])
    i = 0
    for _ in arr:
        evals[i] = func(arr[i])
        i += 1
    return evals

# def do(func, beg, end, num_nodes):

#     nodes = nodes_chebyshev(beg, end, num_nodes)
#     fnodes = f_vals(func, nodes)

#     final_poly = poly_interp.lagrange(nodes, fnodes)
#     return final_poly


# def do(func, node_type, beg, end, num_nodes):
#     nodes 
#     if node_type == 'equal':
#         nodes = nodes_equal(beg, end, num_nodes)
#     elif node_type == 'chebyshev':
#         nodes = nodes_chebyshev(beg, end, num_nodes)
#     else:
#         print('Inappropriate node type! Choose from either "equal" or "chebyshev"')
#         return

#     fnodes = f_vals(func, nodes)

#     final_poly = poly_interp.lagrange(nodes, fnodes)
#     return final_poly

