################
### nodes.py ###
################

import math
import numpy as np

def equal(beg, end, num_nodes):
    nodes = np.zeros(num_nodes + 1)
    const_diff = (end - beg) / num_nodes

    nodes[0] = beg
    i = 1
    for _ in range(1, num_nodes+ 1):
        nodes[i] = nodes[i-1] + const_diff
        i += 1
    nodes[num_nodes] = end
    
    return nodes

def chebyshev(beg, end, num_nodes):
    nodes = np.zeros(num_nodes + 1)

    t1 = (end + beg)/2
    t2 = (end - beg)/2

    nodes[0] = beg
    i = 1
    for _ in range(1, num_nodes + 1):
        nodes[i] = t1 - t2*math.cos((2*i+1)/(2*num_nodes + 2) * math.pi)
        i += 1
    nodes[num_nodes] = end

    return nodes 

