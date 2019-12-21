import heapq


class Graph:
    def __init__(self, number_of_vertices):
        self.graph = dict()
        self.number_of_vertices = number_of_vertices

    def add_edge(self, where, to, weight):
        # adding edges for undirected graph
        self.graph[where].append(0, [to, weight])
        self.graph[to].append(0, [where, weight])

    def print_graph(self): print(self.graph)

    def empty_graph(self): self.graph.clear()

    def dijkstra_shortest_path(self):
        distances = []
        heap = []
        max_number = pow(2, 32)

        for v in range(1, self.number_of_vertices+1):
            distances.append(max_number)
            heap.append([v, distances[v]])
