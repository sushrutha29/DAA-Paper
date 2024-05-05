import random
import numpy as nump
import networkx as net
from scipy.optimize import linprog

def Randomization(nodes, edges):
    G = net.DiGraph()
    G.add_nodes_from(range(nodes))
    for _ in range(edges):
        source, target = random.sample(range(nodes), 2)
        while G.has_edge(source, target):
            target = random.randint(0, nodes - 1)
        G.add_edge(source, target)
    return G

def linear_programming(graph):
    n = graph.number_of_nodes()
    c = nump.zeros(n)
    c[0] = -1  
    A_eq = nump.zeros((1, n))
    A_eq[0, 0] = 1  
    b_eq = nump.array([1])
    bounds = [(0, 1) for _ in range(n)]  
    result = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds)
    return result.x

nodes = 7
edges = 9
random_graph = Randomization(nodes, edges)
solution = linear_programming(random_graph)
pos = net.spring_layout(random_graph)
net.draw(random_graph, pos, with_labels=True, node_color='white')
print("linear programming:", solution)
