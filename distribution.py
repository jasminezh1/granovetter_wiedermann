import numpy as np
import math
import matplotlib.pyplot as plt

# attempt to implement the threshold distribution
rho = 0.5       # threshold fraction
k = 10      # average degree
r = 100     # overll share of active nodes

# solve F(r) = (r-a)/c

def f(r):
    size_of_r = len(r)
    total_summation = [0]*size_of_r
    print("should be 10 zeros: ", total_summation)
    for b in range(1, 20):
        #print("yikes")
        inner_max = rho * b / (1 - rho)
        inner_max = int(inner_max)
        inner_sum = 0
        for a in range(1, inner_max):
            #print("extra yikes")
            inner_sum += ((k*r)**a)/math.factorial(a)
        outer_sum = ((k-k*r)**b)/math.factorial(b)
        #print("outer", outer_sum)
        #print("inner", inner_sum)
        temp = np.multiply(outer_sum, inner_sum)
        print("temp: ",temp)
        total_summation += temp
    return 1 - math.exp(-k) * total_summation

x = np.linspace(0,1,10)
#print(x)
test = f(x)
ugh = list(map(f,x))
#print("f(x) dimension", test.shape)
print(ugh)
plt.plot(x,ugh, color = 'red')
plt.show()
print("end program")