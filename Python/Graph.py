from collections import defaultdict

class Graph(object):

    def __init__(self, directed=False):
        self.edges = defaultdict(list)
        self.weights = {}
        self.directed = directed

    def add_edge(self, from_node, to_node, weight):
        if self.directed:
            self.edges[from_node].append(to_node)
            self.weights[(from_node, to_node)] = weight
        else:
            self.edges[to_node].append(from_node)
            self.weights[(to_node, from_node)] = weight

    def dijsktra(graph, initial, end):
        # shortest paths is a dict of nodes
        # whose value is a tuple of (previous node, weight)
        shortest_paths = {initial: (None, 0)}
        current_node = initial
        visited = set()

        while current_node != end:
            visited.add(current_node)
            destinations = graph.edges[current_node]
            weight_to_current_node = shortest_paths[current_node][1]

            for next_node in destinations:
                weight = graph.weights[(current_node, next_node)] + weight_to_current_node
                if next_node not in shortest_paths:
                    shortest_paths[next_node] = (current_node, weight)
                else:
                    current_shortest_weight = shortest_paths[next_node][1]
                    if current_shortest_weight > weight:
                        shortest_paths[next_node] = (current_node, weight)

            next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
            if not next_destinations:
                return "Route Not Possible"
            # next node is the destination with the lowest weight
            current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

        # Work back through destinations in shortest path
        path = []
        while current_node is not None:
            path.append(current_node)
            next_node = shortest_paths[current_node][0]
            current_node = next_node
        # Reverse path
        path = path[::-1]
        return path


connections = [
    ('X', 'A', 7),
    ('X', 'B', 2),
    ('X', 'C', 3),
    ('X', 'E', 4),
    ('A', 'B', 3),
    ('A', 'D', 4),
    ('B', 'D', 4),
    ('B', 'H', 5),
    ('C', 'L', 2),
    ('D', 'F', 1),
    ('F', 'H', 3),
    ('G', 'H', 2),
    ('G', 'Y', 2),
    ('I', 'J', 6),
    ('I', 'K', 4),
    ('I', 'L', 4),
    ('J', 'L', 1),
    ('L', 'I', 1),
    ('L', 'J', 1),
    ('K', 'Y', 5),
]

graph = Graph(directed=True)

# for edge in connections:
#     graph.add_edge(*edge)
[graph.add_edge(*edge) for edge in connections]

print(graph.dijsktra('X', 'Y'))
print(graph.dijsktra('X', 'I'))