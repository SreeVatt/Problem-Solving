from collections import defaultdict, deque

class Graph:
    def _init_(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u) 

    def bfs(self, start, end):
        visited = set()
        queue = deque([(start, [start])])

        while queue:
            n, p = queue.popleft()
            if n == end:
                return p
            if n not in visited:
                visited.add(n)
                for neighbor in self.graph[n]:
                    if neighbor not in visited:
                        queue.append((neighbor, p + [neighbor]))

        return None

    def Path(self, path):
        for i in range(len(path) - 1):
            print(path[i], '->', end=' ')
        print(path[-1])


g = Graph()
g.add_edge(1,3)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 4)
g.add_edge(3, 4)
g.add_edge(3, 5)
g.add_edge(4, 5)

start_node = 1
end_node = 6
shortest_path = g.bfs(start_node, end_node)

if shortest_path:
    print("Shortest Path from", start_node, "to", end_node, ":", shortest_path)
    print("Highlighted Path:")
    g.Path(shortest_path)
else:
    print("No path found between", start_node, "and",end_node)
