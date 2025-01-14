class Edge:
    def __init__(self, node, weight):
        self.node = node
        self.weight = weight


class DirectedWeightedGraph:
    def __init__(self):
        self.adjList = {}

    def addNode(self, node):
        if node not in self.adjList:
            self.adjList[node] = []

    def addEdge(self, node1, node2, weight):
        if node1 not in self.adjList:
            self.addNode(node1)
        if node2 not in self.adjList:
            self.addNode(node2)

        edge = Edge(node2, weight)
        self.adjList[node1].append(edge)
