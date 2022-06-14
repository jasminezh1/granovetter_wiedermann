import numpy as np
import math
import matplotlib.pyplot as plt

# attempt to implement the threshold distribution
rho = 0.5       # threshold fraction
k = 10      # average degree

# solve F(r) = (r-a)/c

# r is overall share of active nodes
def f(r):
    print("beginning of function")
    print("this is r: ",r)
    total_summation = [0]
    print("should be 10 zeros sometimes: ", total_summation)
    for b in range(1, 20):
        inner_max = rho * b / (1 - rho)
        inner_max = int(inner_max)
        inner_sum = 0

        for a in range(1, inner_max):
            inner_sum += ((k*r)**a)/math.factorial(a)
       
        outer_sum = ((k-k*r)**b)/math.factorial(b)
        temp = np.multiply(outer_sum, inner_sum)
        #print("temp: ",temp)
        total_summation += temp
    return 1 - math.exp(-k) * total_summation

# print("idk: ", f(0.1)) # this is fine

x = np.linspace(0,1,10)
#print(x)
test = f(x)
ugh = list(map(f,x))
#print("f(x) dimension", test.shape)
print(ugh)
plt.plot(x,ugh, color = 'red')
plt.show()
print("end program")