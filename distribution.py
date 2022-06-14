from binascii import a2b_hex
import numpy as np
import math
import matplotlib.pyplot as plt

# attempt to implement the threshold distribution
rho = 0.5       # threshold fraction
k = 10      # average degree

# solve F(r) = (r-a)/c

# r is overall share of active nodes
def f(r):
    #print("beginning of function")
    #print("this is r: ",r)
    total_summation = [0]
    #print("should be 10 zeros sometimes: ", total_summation)
    for b in range(0, 40):
        inner_max = rho * b / (1 - rho)
        inner_max = int(inner_max)
        inner_sum = 0

        for a in range(0, inner_max):
            inner_sum += ((k*r)**a)/math.factorial(a)
       
        outer_sum = ((k-k*r)**b)/math.factorial(b)
        temp = np.multiply(outer_sum, inner_sum)
        total_summation += temp
    return 1 - (math.exp(-k) * total_summation)

def line(r):
    a = 0.12
    c = 0.8
    return (r-a)/c


# print("idk: ", f(0.1)) # this is fine

x = np.linspace(0,1,6000)
#print(x)
#test = f(x)
ugh = list(map(f,x))
ugh_array = np.concatenate(ugh, axis=0)
#print("f(x) dimension", test.shape)
# print(ugh_array)
plt.plot(x,ugh, color = 'red')

ugh2 = list(map(line, x))
plt.plot(x, ugh2, color = 'blue')

# maybe = np.intersect1d(ugh_array, ugh2)   #nvm it's not precise enough
#print("maybe ", maybe)

close_enough = []
counter_indices = []

counter = 0
for i in x:
    subtract = ugh_array[counter] - ugh2[counter]
    if np.abs(subtract) <0.00012 :
         close_enough.append(i)
         counter_indices.append(counter)
    counter+=1

#print("**********", close_enough)

rounded = [round(elem, 2) for elem in close_enough]
#print("rounded", rounded)
no_dups =  np.unique(rounded).tolist()
print("x values, rounded: ", no_dups)
for i in counter_indices:
    plt.plot(x[i],ugh_array[i], 'go')

plt.title("F(t)")
plt.show()
print("end program")