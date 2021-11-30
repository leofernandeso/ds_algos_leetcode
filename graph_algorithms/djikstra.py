import heapq
from typing import List, Tuple
from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self._nodes = set()
        self._nodes_data = defaultdict(dict)

    @classmethod
    def from_adj_matrix(cls, adj_matrix: list) -> 'Graph':
        g = cls()
        g.graph = adj_matrix
        for node in range(len(g.graph)):
            g.add_node(node)
        return g

    def __str__(self):

        if not self.graph:
            return "Empty graph"

        s = ""
        for u, children in self.graph.items():
            s += f"{u}: {children}\n"
        return s

    def add_node(self, id_, data=None):

        if data is None:
            data = {}

        self._nodes.add(id_)
        self._nodes_data[id_] = data

    def add_edge(self, u, v, weight, u_data=None, v_data=None):

        if u_data is None:
            u_data = {}
        if v_data is None:
            v_data = {}

        self.graph[u].append(v)

    @property
    def size(self):
        return len(self._nodes)

    def topological_sort_helper(self, u: int, stack: list, visited: set) -> None:
        visited.add(u)
        for child in self.graph[u]:
            if child not in visited:
                self.topological_sort_helper(child, stack, visited)
        stack.appendleft(u)

    def topological_sort(self) -> List[int]:
        visited = set()
        stack = deque()
        for u in range(self.size):
            if u not in visited:
                self.topological_sort_helper(u, stack, visited)
        return stack

    def alap_schedule_helper(self, u: int, visited: set, desired_latency: int, schedule: dict):

        visited.add(u)
        if self._nodes_data[u].get('sink'):
            schedule[u] = desired_latency
            return desired_latency

        min_child_start_time = float('inf')
        for child in self.graph[u]:
            child_start_time = self.alap_schedule_helper(child, visited, desired_latency, schedule)
            min_child_start_time = min(min_child_start_time, child_start_time)

        scheduled_time = min_child_start_time - self._nodes_data[u]['duration']
        schedule[u] = scheduled_time
        return scheduled_time

    def alap_schedule(self, desired_latency: int):

        visited = set()

        schedule = {}
        for u in range(self.size):
            self.alap_schedule_helper(u, visited, desired_latency, schedule)

        return schedule

    def get_closest(self, dists: list, nodes_to_visit: set) -> Tuple[int, float]:
        min_dist = float('inf')
        closest = None
        for node, curr_dist in enumerate(dists):
            if node in nodes_to_visit and curr_dist < min_dist:
                min_dist = curr_dist
                closest = node
        return (closest, min_dist)

    def djikstra_shortest_path_distance(self, source: int) -> int:

        if not isinstance(self.graph, list):
            raise ValueError("Djikstra can only be run with adj matrix format!")
        if source not in self._nodes:
            raise ValueError(f"Source node {source} not in graph!")

        dists = [float('inf')] * self.size
        dists[source] = 0
        Q = []
        heapq.heappush(Q, (0, source))
        visited = set()
        while Q:
            smallest_dist, node = heapq.heappop(Q)
            visited.add(node)
            for node_neighbor, node_dist in enumerate(self.graph[node]):
                if node_dist and node_neighbor not in visited:
                    heapq.heappush(Q, (self.graph[node][node_neighbor], node_neighbor))
                    candidate_distance = dists[node] + self.graph[node][node_neighbor]
                    dists[node_neighbor] = candidate_distance if candidate_distance <= dists[node_neighbor] else dists[node_neighbor]
        return dists

if __name__ == "__main__":
    g = Graph.from_adj_matrix([
        [0, 6, 0, 1, 0],
        [6, 0, 5, 2, 2],
        [0, 5, 0, 0, 5],
        [1, 2, 0, 0, 1],
        [0, 2, 5, 1, 0],
    ])
    dists = g.djikstra_shortest_path_distance(0)
