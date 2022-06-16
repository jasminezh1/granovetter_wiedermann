from binascii import a2b_hex
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import optimize
from scipy.optimize import fsolve

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

# find where f() and line() intersect
# always in range [0,1]
def find_intersection(number, a, c):
    x = np.linspace(0,1,number)
    a = [a] * number
    c = [c] * number

    distribution = list(map(f,x))
    dis_array = np.concatenate(distribution, axis=0)

    line_ap = list(map(line, x, a, c))

    close_enough = []
    counter_indices = []

    # check if values in the two lines are sufficiently close 
    counter = 0
    for i in x:
        subtract = dis_array[counter] - line_ap[counter]
        if np.abs(subtract) <0.0001 :
            close_enough.append(i)
            counter_indices.append(counter)
        counter+=1

    rounded = [round(elem, 3) for elem in close_enough]     # rounded to 3 places. ok???
    no_dups =  np.unique(rounded).tolist()
    print("x values, rounded: ", no_dups)

    return no_dups, x, distribution, line_ap, dis_array, counter_indices

# plot f() and line() and their intersection points
def plot_intersection(x, distribution, line_ap, dis_array, counter_indices):
    plt.plot(x,distribution, color = 'red')
    plt.plot(x, line_ap, color = 'blue')

    for i in counter_indices:
        plt.plot(x[i],dis_array[i], 'go')

    plt.title("F(t)")
    plt.xlabel('R(t)')
    plt.ylabel('R(t+1) = A + CF(R(t))')
    plt.show()


def find_intersection_2(x):
    #print("hello")
    return [x[1] - f(x[0]), x[1] - line(x[0], 0.4, 0.8)]


# i think this one is fine
def find_intersection_3(x):
    return f(x) - line(x, 0.5, 0.3)


# a = .125, c = 0.8
fixed_points, x, distribution, line_ap, dis_array, counter_indices = find_intersection(5000, 0.3, 0.8)
#plot_intersection(x, distribution, line_ap, dis_array, counter_indices)

x0 = [0.5, 0.5]
root = fsolve(find_intersection_2, x0)
print("root: ", root)


root2 = fsolve(find_intersection_3, [0, 0.5, 1])

#sol = optimize.root(find_intersection_2, x0)
print("root 2: ", root2)

#test = optimize.brentq(find_intersection_3, 0, 1)
#print("root 3: ", test)

print("end program")