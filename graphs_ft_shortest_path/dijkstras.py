import WeightedGraph
import heapq


infinity = float("inf")


def dijkstras(graph, source):
    shortest_paths = {node: infinity for node in graph.adjList}
    shortest_paths[source] = 0
    priority_queue = [(0, source)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        for edge in graph.adjList[current_node]:
            neighbor, weight = edge.node, edge.weight
            distance = current_distance + weight

            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_paths


weighted_graph = WeightedGraph.DirectedWeightedGraph()
weighted_graph.addNode('A')
weighted_graph.addEdge('A', 'B', 2)
weighted_graph.addEdge('A', 'D', 8)
weighted_graph.addEdge('B', 'D', 5)
weighted_graph.addEdge('B', 'E', 6)
weighted_graph.addEdge('D', 'E', 3)
weighted_graph.addEdge('D', 'F', 2)
weighted_graph.addEdge('E', 'C', 9)
weighted_graph.addEdge('F', 'C', 3)

shortest = dijkstras(weighted_graph, 'A')
nodes = sorted(weighted_graph.adjList.keys())
for node in nodes:
    print(node, " ", shortest[node])
