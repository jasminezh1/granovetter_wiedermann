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
# vars = sys.arv[1:]
a = 2   # active
c = 5   # conditionally active
i = 2   # inactive
n = a+c+i
aNodes = list(range(1, a+1))
cNodes = list(range(a+1, a+c+1))
iNodes = list(range(a+c+1, n+1))
people.add_nodes_from(aNodes, activity = 'a')
people.add_nodes_from(cNodes, activity = 'c')
people.add_nodes_from(iNodes, activity = 'i')
#print(people.number_of_nodes())
#print(list(people.nodes.data("a")))

l = 0.2 # edge linking strength forget what it's called
rho = 0.5  # common threshold fraction

all = [*aNodes, *cNodes, *iNodes]
for node1 in all:
    for node2 in all:
        #print(node1, " ", node2)
        if(np.random.random() < l) and (node1!=node2):
            people.add_edge(node1, node2)

print(people.edges())
numNodes = people.number_of_nodes()
numEdges = people.size() 
k = numEdges / numNodes * 2     # average degree
print("number of nodes ", numNodes)
print("number of edges ", numEdges)
print("average degree ", k)

#   start iterating
# keep looping until number of new nodes is 0
# i guess loop through all the potentially active nodes
# for each node, check how many active
# keep a list of potentially active nodes, remove as needed

newly_active = 1
while newly_active > 0:
    print("in while loop")
    newly_active = 0
    updateNodes = []    # nodes to update to active at the end

    for currentNode in cNodes:
        numActive = 0
        numNeighbors = 0
        
        for neighbor in people.neighbors(currentNode):
            numNeighbors+=1
            print(neighbor)
            if(people.nodes[neighbor].get('activity') == 'a'):
                numActive += 1
                print("num active", numActive)
        
        if(numNeighbors == 0):
            cNodes.remove(currentNode) # no point in checking again
            continue

        fraction = numActive / numNeighbors
        if(fraction > rho):
            updateNodes.append(currentNode)
            newly_active+=1
            print("woo hoo")
            cNodes.remove(currentNode)
            
    if(newly_active > 0):
        for i in updateNodes:
            people.nodes[i]['activity'] = 'a'

print("end")
