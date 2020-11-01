import math
import numpy as np 
import matplotlib.pyplot as plt

def bisection (f, a, b, i = None, accuracy = None):
    if accuracy is None:
        fa = f(a)
        fb = f(b)
        if fa*fb > 0: 
            print("Error! f(a) and f(b) must have different signs!")
            return None

        error = np.zeros(i)
        value = np.zeros(i)
        funcvalue = np.zeros(i) 

        iterate = 0 
        for _ in range(i):
            c = (a+b)/2
            fc = f(c)

            error[iterate] = abs(c-0.7)
            value[iterate] = c
            funcvalue[iterate] = abs(fc)

            if f(c) == 0:
                #return c
                break
            
            if fa*fc > 0:
                a, fa = c, fc

            if fb*fc > 0:
                b, fb = c, fc
            iterate += 1
    #print(error) 

    #printing data
    xaxis = np.arange(1,i+1,1)

    #error between p_n and p
    plt.plot(xaxis,error)
    plt.xlabel("$Iterations$")
    plt.ylabel("$|p_n - p|$")
    plt.title("$|p_n - p|$")
    plt.locator_params('x', 1)
    plt.minorticks_on()
    plt.show()

    #error between p_n and p_n-1
    #for p_n we must start at 1 because p_n-1 must access array element 0, and if it ends at the 16th element, 15th element is p_n-1. Thus we create an array of 15.
    diffiter = abs(value[1:i] - value[0:i-1])
    plt.plot(diffiter)
    plt.xlabel('$Iterations$')
    plt.ylabel("$|p_n-p_{n-1}$")
    plt.title("$|p_n-p_{n-1}|$")
    plt.minorticks_on()
    plt.show()
    
    #possibilities are that I can create a new array with all the values of p_n-1 and also p_n
    plt.plot(xaxis,funcvalue)
    plt.xlabel("$Iterations$")
    plt.ylabel("$|f(p_n)|$")
    plt.title("$|f(p_n)|$") 
    plt.minorticks_on()
    plt.show()

    #error between

    return c

### Function 1 (Question 3)
def func1(x):
    return x**2 - 0.7*x

a1 = 0.5
b1 = 1
i1 = 16

p = bisection(func1, a1, b1, i1)
# print("Solution found: {}".format(p))

### Function 2 (Question 4)
def func2(x):
    return math.sqrt(x) - math.cos(x)

a2 = 0
b2 = 1
i2 = 17

p = bisection(func2, a2,b2,i2)
