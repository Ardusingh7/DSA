nodes=3
edges=[(0,1),(0,2),(1,2)] 

class Graph:

    def __init__(self, nodes,edges):

        self.nodes = nodes
        self.data=[[] for _ in range(nodes)]

        for i,j in edges:
            self.data[i].append(j)
            self.data[j].append(i)

g=Graph(nodes, edges)
print(g.data)
print()

for x in enumerate(g.data):
    print(x)