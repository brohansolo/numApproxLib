import math
import numpy as np
import matplotlib.pyplot as plt

def fixedpoint(f, p0, tol, i):

    p = p0
    pprev = 0
    fp = f(p0)
    iterate = 0

    val = []
    fval = []

    for _ in range(i):
        fp = f(p)
        val.append(p)
        fval.append(fp)
        iterate += 1
        
        if abs(fp-p) < tol:
                break
        if abs(p-pprev) < tol:
                break
        pprev = p
        p = fp
    
    ####----Miscellaneous----####
    npval = np.array(val)
    npfval = np.array(fval)
    ####---------------------####

    # Shows the difference between fixed point and the function
    error = abs(npval - npfval)
    plt.plot(error)
    plt.xlabel("iterations")
    plt.ylabel("$|f(p_n) - p_n|$")
    plt.title("$|f(p_n) - p_n|$")
    # plt.minorticks_on()
    plt.show()

    #Shows the difference between p at every iterate and the final value calculated for p
    justp = np.full(iterate, p)
    howclose = abs(npval - justp)
    plt.plot(howclose)
    plt.xlabel("iterations")
    plt.ylabel("$|p_n - p|$")
    plt.title("$|p_n - p|$")
    # plt.minorticks_on()
    plt.show()

    # Shows the difference between successive iterations of p
    diffiter = abs(npval[1:iterate] - npval[0:iterate-1])
    plt.plot(diffiter)
    plt.xlabel("iterations")
    plt.ylabel("$|p_n - p_{n-1}|$")
    plt.title("$|p_n - p_{n-1}|$")
    plt.minorticks_on()
    plt.show()

    return p

def func(x):
    return math.pi + 0.5*math.sin(x/2)

p = fixedpoint(func, math.pi, 0.0001, 7)       