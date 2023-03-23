import pprint
from typing import Tuple, Any


class Graph:

    def __init__(self):
        self._nodes: dict = dict()

    @property
    def nodes(self):
        return self._nodes

    def __str__(self):
        return self.nodes

    def _validate_data(self, *args):
        for node in args:
            if node not in self.nodes.keys():
                raise KeyError()

    def add_node(self, node):
        self.nodes[node] = dict()
        return self.nodes

    def add_edge(self, node, *args):
        self._validate_data(node)
        for i in args:
            self.nodes[node][i] = dict()
        return self.nodes

    def value_edge(self, node1, node2, name, *args):
        self._validate_data(node1, node2)
        self.nodes[node1][node2] = {name: [i for i in args]}
        return self.nodes[node1][node2]


    def is_adjacent(self, node1, node2):
        self._validate_data(node1, node2)
        if node2 in self.nodes[node1]:
            return -1
        elif node1 in self.nodes[node2]:
            return 1
        else:
            return 0

    def bfs(self, from_node, to_node):

        # Create an empty set to store visited nodes
        visited = set()

        # Create a queue for BFS and add from_node to it
        queue = [from_node]

        # Mark the from_node as visited and enqueue it
        visited.add(from_node)

        while queue:

            # Dequeue a vertex from queue
            curr_node = queue.pop(0)

            # If this adjacent node is the destination node,
            # then return true
            if curr_node == to_node:
                return True

            #  Else, continue to do BFS
            for node in self.nodes[curr_node]:
                if node not in visited:
                    queue.append(node)
                    visited.add(node)
        return False

    def dfs_shortest_path(self, from_node, to_node, name) -> int or None:
        paths: list = list()
        self._dfs_all_paths_rec(from_node, to_node, set(), list(), list(), paths, name)
        if paths:
            curr_val = 0
            for price in paths:
                if curr_val < price[1]:
                    curr_val = price[1]
            return curr_val
        else:
            return None

    def _dfs_all_paths_rec(self, from_node, to_node, visited, path, cost, paths, name) -> None:
        self._validate_data(from_node, to_node)

        path.append(from_node)
        visited.add(from_node)
        if from_node == to_node:
            paths.append((list(path), sum(cost)))

        for node in self.nodes[from_node]:
            if node not in visited:
                cost.append(self.nodes[from_node][node][name][0])
                self._dfs_all_paths_rec(node, to_node, visited, path, cost, paths, name)
                cost.pop()
        visited.remove(from_node)
        path.pop()



if __name__ == '__main__':

    graph = Graph()
    for city in ('Brussels', 'Kyoto', 'Amsterdam',
                 'Tokyo', 'Tel Aviv', 'Paris', 'London', 'Hong Kong'):
        graph.add_node(city)

    graph.add_edge('Brussels', 'Tokyo')
    graph.add_edge('Brussels', 'Tel Aviv')

    graph.add_edge('Tokyo', 'Kyoto')
    graph.add_edge('Tokyo', 'Hong Kong')

    graph.add_edge('Tel Aviv', 'Paris')

    graph.add_edge('Hong Kong', 'Tel Aviv')

    graph.add_edge('Paris', 'Tel Aviv')
    graph.add_edge('Paris', 'Amsterdam')
    graph.add_edge('Paris', 'London')

    graph.value_edge('Brussels', 'Tel Aviv', 'price', 150)
    graph.value_edge('Brussels', 'Tokyo', 'price', 280)

    graph.value_edge('Tokyo', 'Kyoto', 'price', 50)
    graph.value_edge('Tokyo', 'Hong Kong', 'price', 70)

    graph.value_edge('Tel Aviv', 'Paris', 'price', 20)

    graph.value_edge('Hong Kong', 'Tel Aviv', 'price', 10)

    graph.value_edge('Paris', 'Amsterdam', 'price', 890)
    graph.value_edge('Paris', 'London', 'price', 540)
    #
    # pprint.pprint(graph._nodes)

    # print(f"Path from Brussels to Amsterdam: {graph.bfs('Brussels', 'Amsterdam')}")
    # print(f"Path from Tokyo to Brussels: {graph.bfs('Tokyo', 'Brussels')}")

    print(f"Path from Brussels to Amsterdam: {graph.dfs_shortest_path('Brussels', 'Amsterdam', 'price')}")
    print(f"Path from Tokyo to Brussels: {graph.dfs_shortest_path('Tokyo', 'Brussels', 'price')}")