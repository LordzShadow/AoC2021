from functools import lru_cache
from heapq import heapify, heappop, heappush

class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.edges = [-1 for i in range(self.v)]
        self.visited = set()

    def add_edge(self, u, weight):
        self.edges[u] = weight    

def dijkstra(graph: Graph, source, xs):
    D = {v:float('inf') for v in range(graph.v)}
    D[source] = 0
    heap = []
    heapify(heap)
    heappush(heap, (0, source))

    while heap:
        (dist, c) = heappop(heap)
        graph.visited.add(c)
        neighbours = []
        neighbours.append(c-1) if c-1 >= 0 and c%xs != 0 else None
        neighbours.append(c+1) if c+1 < g.v and (c+1)%xs != 0 else None
        neighbours.append(c-xs) if c-xs >= 0 else None
        neighbours.append(c+xs) if c+xs < g.v else None
        for next in neighbours:
            distance = graph.edges[next]
            if next not in graph.visited:
                old = D[next]
                new = D[c] + distance
                if new < old:
                    heappush(heap, (new, next))
                    D[next] = new
    return D

tile:"list[list]" = []
# Part 1  times = 1
times = 5
with open("input.txt", "r") as file:
    lines = file.readlines()
    xs = len(lines[0].strip())
    ys = len(lines)
    vertices = xs*ys*(times**2)
    g = Graph(vertices)
    for line in lines:
        tile.append([])
        for nr in line.strip():
            tile[-1].append(int(nr))
    for tiley in range(times):
        for tilex in range(times):
            for i,line in enumerate(tile):
                for j, val in enumerate(line):
                    val = val + tilex + tiley
                    val = val%9
                    if val == 0:
                        val = 9  
                    idx = (j+(xs)*tilex) + xs*times*i + (tiley*ys*xs*times)
                    g.add_edge(idx, val)
    print(dijkstra(g, 0, xs*times)[vertices-1])