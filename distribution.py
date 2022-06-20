from binascii import a2b_hex
import sys
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import optimize
from scipy.optimize import fsolve
import warnings

# attempt to implement the threshold distribution
# keep these constant for now
rho = 0.5       # threshold fraction
k = 10      # average degree

# solve F(r) = (r-a)/c

# distribution threshold
# r is overall share of active nodes
def f(r):
    total_summation = [0]
    for b in range(0, 2*k):
        inner_max = rho * b / (1 - rho) #float
        inner_max = int(inner_max)
        inner_sum = 0

        for a in range(0, inner_max):
            inner_sum += ((k*r)**a)/math.factorial(a)
       
        outer_term = ((k-k*r)**b)/math.factorial(b)
        temp = np.multiply(outer_term, inner_sum)
        total_summation += temp
    return 1 - (math.exp(-k) * total_summation)

#line from (A,0) to (P,1)
def line(r, a, c):
    return (r-a)/c

# find fixed points
def find_intersection(x, a, c):
    return f(x) - line(x, a, c)

def plot_functions(root_x, root_y, a, c):
    intervals = 5000
    x = np.linspace(0,1,intervals)
    a = [a] * intervals
    c = [c] * intervals

    distribution = list(map(f,x))
    line_ap = list(map(line, x, a, c))
    #difference = list(map(find_intersection, x, a, c))
    
    plt.plot(x, distribution, color = 'red')
    plt.plot(x, line_ap, color = 'blue')
    #plt.plot(x, difference, color = 'black')

    for i in range(0, len(root_x)):
        plt.plot(root_x[i],root_y[i], 'go')

    plt.title("F(t)")
    plt.xlabel('R(t)')
    plt.ylabel('R(t+1) = A + CF(R(t))')
    plt.show()

def solve_root(start_guess, a, c):
    # start = [0, 0.5,1] ; some array with either 1 or 3 guesses
    root_x = fsolve(find_intersection, start_guess, args = (a, c))
    return root_x


vars = sys.argv[1:]
a, c = float(vars[0]), float(vars[1])   # active, conditionally active


with warnings.catch_warnings():
# hm. Issues. with when there's only one fixed point. 
    warnings.filterwarnings('error')
    start_guess = [0, 0.5, 1]
    try:
        #warnings.warn(Warning())
        root_x = solve_root(start_guess, a, c)
    except RuntimeWarning as e:
        try:
            start_guess = [1]
            root_x = solve_root(start_guess, a, c)
        except RuntimeWarning as e:
            start_guess = [0]
            root_x = solve_root(start_guess, a, c)
    #root_x =  np.unique(root_x).tolist()

#root_x = np.unique(root_x).tolist()     
#sometimes duplicates when only 1 root ; fix this later with difference probably
root_y = [line(x, a, c) for x in root_x]

print("root(s): ", root_x)

plot_functions(root_x, root_y, a, c)

print("end program")