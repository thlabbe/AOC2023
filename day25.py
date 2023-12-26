from collections import defaultdict
from dataclasses import dataclass
import graphviz

FILE = "input25.txt"
# FILE = "test25.txt"

L = open(FILE).read().splitlines()

@dataclass(frozen=True)
class Graph:
    edges: dict
    def add_edge(self, na, nb):
        self.edges[na].add(nb)
        self.edges[nb].add(na)

    def del_edge(self, na, nb):
        self.edges[na].remove(nb)
        self.edges[nb].remove(na)

    def del_node(self, n):
        for nb in self.edges[n]:
            self.edges[nb].remove[n]
        del self.edges[n]

    def count_nodes_from(self, n):
        nxt = [n]
        seen = {n}
        while nxt:
            current = nxt.pop()
            for nn in self.edges[current]:
                if nn not in seen:
                    seen.add(nn)
                    nxt.append(nn)
        return len(seen)

    def render(self):
        dot = graphviz.Graph(format='svg')
        for na, ns in self.edges.items():
            for nb in ns:
                if na < nb :
                    dot.edge(na, nb)
        dot.view()
def lines_to_graph(L):
    g = Graph(defaultdict(set))
    for l in L:
        tmp = l.split(':')
        na = tmp[0]
        for nb in [n for n in tmp[1].split(' ') if len(n) > 0]:
            g.add_edge(na, nb)
    return g

g = lines_to_graph(L)

nodes_count = len(g.edges)
g.del_edge('dct','kns')
g.del_edge( 'jxb','ksq')
g.del_edge( 'nqq','pxp')
cluster_count = g.count_nodes_from('dct')
print(f"{nodes_count=} {cluster_count=}")
print(f"part1 : {cluster_count * (nodes_count - cluster_count)}")