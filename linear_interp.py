########################
### linear_interp.py ###
########################

import numpy as np
import math
import matplotlib.pyplot as plt

import nodes
import graph

# linear_eval returns a 1d numpy array that shows eval_range+1 equidistant points
# evaluated on a linear interpolation of x_vals, fx_vals

def linear_eval(x_vals, fx_vals, evalpts):
    result = np.zeros(evalpts.shape[0])

    iter1 = 1
    iter2 = 0
    for _ in result:
        if iter2 >= evalpts.shape[0]:
            break

        if x_vals[iter1] < evalpts[iter2]:
            iter1 += 1
        
        result[iter2] = interval(x_vals[iter1-1], x_vals[iter1], 
                            fx_vals[iter1-1], fx_vals[iter1], evalpts[iter2])
        print(iter2, ':', result[iter2])
        iter2 += 1
    
    return result

def interval(x1, x2, fx1, fx2, var):
    return ((x2-x1)/(fx2 - fx1))*(var-x2) + fx2

def f_vals(func, arr):
    evals = np.zeros(arr.shape[0])
    i = 0
    for _ in arr:
        evals[i] = func(arr[i])
        i += 1
    return evals


# def p3func(x):
#     return math.exp(-2*x) + 2*x**2 + x + 1

# start = nodes.equal(0, 1, 317)
# fstart = f_vals(p3func, start)

# x = np.arange(0, 1.001, 10**-3)

# interpx = linear_eval(start, fstart, x)
# fx = f_vals(p3func, x)

# plt.plot(x, interpx, label = 'Interpolated Values')
# plt.plot(x, fx, label = '$f(x)$')
# graph.showgraph('$f(x)$, $S_{1,n}(x)$', 'x', '$f(x)$, $S_{1,n}(x)$', True, True)

# error = abs(interpx-fx)
# print (error)