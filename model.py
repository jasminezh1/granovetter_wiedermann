# attempt at implementing Wiedermann's modified Granovetter model
import numpy as np
import networkx as nx


def threshold_distribution(r):
    print("oh boy")

print("testing file")

# okay what things go in this model
# needs some constants, some equations
# this is all a NETWORK. use networkx, just a network of nodes.

# fix the threshold fraction for now

# let A be the number of certainly acting nodes. hardcode this in for now (or make it command line arg)
# let P be th enumber of potentially acting nodes.
# create graph. assign A certainly acting nodes, assign P-A conditionally acting nodes. assign N-P inactive nodes.
#
# iterate through all pairs of nodes, adding an edge with probability l. directed vs undirected?


# for now, just hardcode in every single value. figure out the equations later.
# add methods and modularize later

people = nx.Graph() # undirected graph for now, can easily change
a = 2
c = 5
i = 2
n = a+c+i
aNodes = list(range(1, a+1))
cNodes = list(range(a+1, a+c+1))
iNodes = list(range(a+c+1, n+1))
people.add_nodes_from(aNodes, a = 'a')
people.add_nodes_from(cNodes, c = 'c')
people.add_nodes_from(iNodes, i = 'i')
#print(people.number_of_nodes())
#print(list(people.nodes.data("a")))

l = 0.2

all = [*aNodes, *cNodes, *iNodes]
for node1 in all:
    for node2 in all:
        #print(node1, " ", node2)
        if(np.random.random() < l) and (node1!=node2):
            people.add_edge(node1, node2)

print(people.edges())
numNodes = people.number_of_nodes()
numEdges = people.size() 
k = numEdges / numNodes * 2
print("number of nodes ", numNodes)
print("number of edges ", numEdges)
print("average degree ", k)


