import WeightedGraph

infinity = float("inf")


class ShortestPath:
    def __init__(self, shortest_path, previous_node):
        self.shortest_path = shortest_path
        self.previous_node = previous_node


def dijkstras(graph: WeightedGraph.DirectedWeightedGraph, source):
    unvisited_nodes = set(graph.adjList.keys())
    shortest_paths = {node: ShortestPath(infinity, None) for node in graph.adjList}
    shortest_paths[source] = ShortestPath(0, None)

    while unvisited_nodes:
        current_node = min(unvisited_nodes, key=lambda node: shortest_paths[node].shortest_path)
        unvisited_nodes.remove(current_node)

        for edge in graph.adjList[current_node]:
            calculated_path = shortest_paths[current_node].shortest_path + edge.weight
            if calculated_path < shortest_paths[edge.node].shortest_path:
                shortest_paths[edge.node].shortest_path = calculated_path
                shortest_paths[edge.node].previous_node = current_node

    return shortest_paths

# weighted_graph = WeightedGraph.DirectedWeightedGraph()
# weighted_graph.addNode('A')
# weighted_graph.addEdge('A', 'B', 2)
# weighted_graph.addEdge('A', 'D', 8)
# weighted_graph.addEdge('B', 'D', 5)
# weighted_graph.addEdge('B', 'E', 6)
# weighted_graph.addEdge('D', 'E', 3)
# weighted_graph.addEdge('D', 'F', 2)
# weighted_graph.addEdge('E', 'C', 9)
# weighted_graph.addEdge('F', 'C', 3)
# 
# shortest = dijkstras(weighted_graph, 'A')
# nodes = sorted(weighted_graph.adjList.keys())
# for node in nodes:
#     print(node, " ", shortest[node].shortest_path, " ", shortest[node].previous_node)
