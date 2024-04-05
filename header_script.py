class WeightedEdge:
    def __init__(self, from_vertex, to_vertex, capacity):
        self.tail = from_vertex
        self.head = to_vertex
        self.capacity = capacity

class Graph:
    def __init__(self, vertices, edges, capacities):
        self.vertices = vertices
        self.edges = [WeightedEdge(edges[i][0], edges[i][1], capacities[i]) for i in range(len(edges))]

        self.__forward_list = {v : [] for v in vertices}
        self.__reverse_list = {v: [] for v in vertices}

        for i in range(len(edges)):
            self.__forward_list[edges[i][0]].append((edges[i][1], capacities[i]))
            self.__reverse_list[edges[i][1]].append((edges[i][0], capacities[i]))

    def out_edges(self, vertex):
        return [WeightedEdge(vertex, next_vertex, capacity) for (next_vertex, capacity) in self.__forward_list[vertex]]
    
    def in_edges(self, vertex):
        return [WeightedEdge(prev_vertex, vertex, capacity) for (prev_vertex, capacity) in self.__reverse_list[vertex]]

def is_equal(a, b):
    if a == 0 or b == 0:
        return a == b
    
    return abs(a/b - 1) < 1e-4