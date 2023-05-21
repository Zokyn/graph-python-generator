import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, V, E) -> None:
        self.V = V
        self.E = E 
        self.n = len(self.V)
        self.m = len(self.E)
        self.Gnx = nx.Graph()
        for i in range(len(V)):
            self.Gnx.add_node(V[i])
        for i in range(len(E)):
            v, w = E[i]
            self.Gnx.add_edge(v, w)
    def isEmpty(self) -> bool:
        if(self.n == 0):
            return True
        return False
    def isTrivial(self) -> bool:
        if self.n > 0 and self.m == 0:
            return True
        return False
    def isComplet(self) -> bool:
        if self.m == ((self.n * (self.n-1))/2):
            return True
        return False
    def show(self):
        print(f"É um grafo Trivial") if self.isTrivial() else None
        print(f"É um grafo Completo") if self.isTrivial() else None
        print(f"Esse grafo possui {self.n} vértices e {self.m} arestas")
        print(f"Conjunto de Vértices: {self.V}")
        print(f"Conjunto de Arestas: {self.E}")
        print(f"-"*50)
        nx.draw(self.Gnx, with_labels=True)
        plt.show()
        