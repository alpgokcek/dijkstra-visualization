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

    def print_path(self, start, end, parent_dict):
        path_list = list()
        path_list.append(end)
        print(end)
        if parent_dict[end] == start:
            print(parent_dict[end])
            path_list.append(parent_dict[end])
        else:
            path_list.extend(self.print_path(start, parent_dict[end], parent_dict))
        return path_list

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
                        try:
                            distances[vertex] = newDistance
                            old_index = heap.index((vertex, distances[vertex], min_distance[0]))
                            heap[old_index] = (vertex, distances[vertex], min_distance[0])
                            heap._siftdown(heap, old_index)

                        except ValueError:
                            heapq.heappush(heap, (vertex, distances[vertex], min_distance[0]))

    def dijkstra_shortest_path(self, where, to):
        distances = []
        heap = []
        max_number = pow(2, 32)
        visited = []
        path = set()

        for v in range(0, self.number_of_vertices + 1):
            distances.append(max_number)
        heapq.heappush(heap, (where, 0, None))
        distances[where] = 0
        popped_elements = dict()  # keys=node, value=parent of the node
        while len(visited) != self.number_of_vertices:
            min_distance = heapq.heappop(heap)
            popped_elements[min_distance[0]] = min_distance[2]
            visited.append(min_distance[0])
            if min_distance[0] == to:
                path.add(to)
                mylist= self.print_path(where, to, popped_elements)
                print("mylist", mylist)
                if path.__contains__(None): path.remove(None)
                return path, min_distance[1]
            for i in range(0, len(self.nodes[min_distance[0]])):
                node = self.nodes[min_distance[0]][i]
                vertex, weight = node[0], node[1]
                if vertex not in visited:
                    edgeDistance = weight
                    newDistance = distances[min_distance[0]] + edgeDistance

                    if newDistance < distances[vertex]:
                        try:
                            distances[vertex] = newDistance
                            old_index = heap.index((vertex, distances[vertex], min_distance[0]))
                            heap[old_index] = (vertex, distances[vertex], min_distance[0])
                            heap._siftdown(heap, old_index)


                        except ValueError:
                            heapq.heappush(heap, (vertex, distances[vertex], min_distance[0]))
