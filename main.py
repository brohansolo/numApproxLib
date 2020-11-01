#############
## main.py ##
#############

import math
import numpy as np
import matplotlib.pyplot as plt

import poly_interp
import interpolate
import graph


# x_prob = np.array([-1, 0 , 1])
# y_prob = np.array([0, 1 , 3])

# ps = poly_interp.powerseries(x_prob, y_prob)
# print(ps, '\n')

# lg_poly = poly_interp.lagrange(x_prob, y_prob)
# print(lg_poly, '\n')
    
def p2func(x):
    return 1/(1+x**2)

cheby1 = interpolate.do(p2func, 'chebyshev', 'lagrange', -5, 5, 5)
cheby2 = interpolate.do(p2func, 'chebyshev', 'lagrange', -5, 5, 10)
cheby3 = interpolate.do(p2func, 'chebyshev', 'lagrange', -5, 5, 25)
cheby4 = interpolate.do(p2func, 'chebyshev', 'powerseries', -5, 5, 50)
graph.makegraph(p2func, '$f(x)$')
graph.makegraph(cheby1, '5 nodes')
graph.makegraph(cheby2, '10 nodes')
graph.makegraph(cheby3, '25 nodes')
graph.makegraph(cheby4, '50 nodes')
graph.showgraph('With Chebyshev Nodes', '$x$', 
                    '$f(x), p_{n}(x)$', True, True)


graph.errorgraph(cheby1, p2func, '5 nodes')
graph.errorgraph(cheby2, p2func, '10 nodes')
graph.errorgraph(cheby3, p2func, '25 nodes')
graph.errorgraph(cheby4, p2func, '50 nodes')
graph.showgraph('$|e_{n}(x)|$ With Chebyshev Nodes', '$x$', 
                    '$f(x)-p_{n}(x)$', True, True)

equal1 = interpolate.do(p2func, 'equal', 'lagrange', -5, 5, 5)
equal2 = interpolate.do(p2func, 'equal', 'lagrange', -5, 5, 10)
equal3 = interpolate.do(p2func, 'equal', 'powerseries', -5, 5, 25)
equal4 = interpolate.do(p2func, 'equal', 'powerseries', -5, 5, 50)
graph.makegraph(p2func, '$f(x)$')
graph.makegraph(equal1, '5 nodes')
graph.makegraph(equal2, '10 nodes')
graph.showgraph('With Equidistant Nodes (5, 10)', '$x$', 
                    '$f(x), p_{n}(x)$', True, True)

graph.makegraph(p2func, '$f(x)$')
graph.makegraph(equal3, '25 nodes')
graph.showgraph('With Equidistant Nodes (25)', '$x$', 
                    '$f(x), p_{n}(x)$', True, True)
graph.makegraph(p2func, '$f(x)$')
graph.makegraph(equal4, '50 nodes')
graph.showgraph('With Equidistant Nodes (50)', '$x$', 
                    '$f(x), p_{n}(x)$', True, True)

graph.makegraph(p2func, '$f(x)$')
graph.errorgraph(equal1, p2func, '5 nodes')
graph.errorgraph(equal2,  p2func,'10 nodes')
graph.showgraph('$|e_{n}(x)|$ With Equidistant Nodes(5, 10)', '$x$', 
                    '$f(x)-p_{n}(x)$', True, True)

graph.makegraph(p2func, '$f(x)$')
graph.errorgraph(equal3,  p2func,'25 nodes')
graph.showgraph('$|e_{n}(x)|$ With Equidistant Nodes(25)', '$x$', 
                    '$f(x)-p_{n}(x)$', True, True)

graph.makegraph(p2func, '$f(x)$')
graph.errorgraph(equal4,  p2func,'50 nodes')
graph.showgraph('$|e_{n}(x)|$ With Equidistant Nodes(50)', '$x$', 
                    '$f(x)-p_{n}(x)$', True, True)

