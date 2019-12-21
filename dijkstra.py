from collections import defaultdict
import heapq


class Graph:
    def __init__(self, number_of_vertices):
        self.nodes = defaultdict(list)

        self.number_of_vertices = number_of_vertices

    def add_edge(self, where, to, weight):
        # adding edges for undirected graph
        self.nodes[where].append([to, weight])
        self.nodes[to].append([where, weight])

    def print_graph(self):
        print(self.nodes)

    def empty_graph(self):
        self.nodes.clear()

    def dijkstra_shortest_path_distances(self, where=1):
        distances = []
        heap = []
        max_number = pow(2, 32)
        visited = []

        for v in range(0, self.number_of_vertices + 1):
            distances.append(max_number)
        heapq.heappush(heap, (where, 0))
        distances[where] = 0
        while len(visited) != self.number_of_vertices:
            min_distance = heapq.heappop(heap)
            visited.append(min_distance[0])
            for i in range(0, len(self.nodes[min_distance[0]])):
                node = self.nodes[min_distance[0]][i]
                vertex, weight = node[0], node[1]
                if vertex not in visited:
                    edgeDistance = weight
                    newDistance = distances[min_distance[0]] + edgeDistance

                    if newDistance < distances[vertex]:
                        distances[vertex] = newDistance
                        heapq.heappush(heap, (vertex, distances[vertex]))
        print(distances[1:len(distances)])

    def dijkstra_shortest_path(self, where=1, to=1):
        distances = []
        heap = []
        max_number = pow(2, 32)
        visited = []
        path = set()

        for v in range(0, self.number_of_vertices + 1):
            distances.append(max_number)
        heapq.heappush(heap, (where, 0, None))
        distances[where] = 0
        while len(visited) != self.number_of_vertices:
            min_distance = heapq.heappop(heap)
            visited.append(min_distance[0])
            path.add(min_distance[2])
            if min_distance[0] == to:
                path.add(to)
                print(distances)
                if path.__contains__(None): path.remove(None)
                return path, min_distance[1]
            for i in range(0, len(self.nodes[min_distance[0]])):
                node = self.nodes[min_distance[0]][i]
                vertex, weight = node[0], node[1]
                if vertex not in visited:
                    edgeDistance = weight
                    newDistance = distances[min_distance[0]] + edgeDistance

                    if newDistance < distances[vertex]:
                        distances[vertex] = newDistance
                        heapq.heappush(heap, (vertex, distances[vertex], min_distance[0]))
