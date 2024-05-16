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
