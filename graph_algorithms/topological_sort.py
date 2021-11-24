from typing import List
from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self._nodes = set()

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self._nodes.add(u);
        self._nodes.add(v);

    @property
    def size(self):
        return len(self._nodes)

    def topological_sort_helper(self, u: int, stack: list, visited: set) -> None:
        visited.add(u)
        for neighbor in self.graph[u]:
            if neighbor not in visited:
                self.topological_sort_helper(neighbor, stack, visited)
        stack.appendleft(u)

    def topological_sort(self) -> List[int]:
        visited = set()
        stack = deque()
        for u in range(self.size):
            if u not in visited:
                self.topological_sort_helper(u, stack, visited)
        return stack

    def __str__(self):

        if not self.graph:
            return "Empty graph"

        s = ""
        for u, neighbors in self.graph.items():
            s += f"{u}: {neighbors}\n"
        return s

if __name__ == "__main__":
    g = Graph()
    g.add_edge(5, 2);
    g.add_edge(5, 0);
    g.add_edge(4, 0);
    g.add_edge(4, 1);
    g.add_edge(2, 3);
    g.add_edge(3, 1);
