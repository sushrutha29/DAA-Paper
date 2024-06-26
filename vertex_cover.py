import networkx as q
import random
import matplotlib.pyplot as plot

def approx_vertex_cover_algorithm(G):
    node = set()
    for u, v in G.edges():
        if u not in node and v not in node:
            node.add(u)
            node.add(v)
    return node

def random_graph(n, p):
    graph = q.gnp_random_graph(n, p)
    return graph

def plot_graph(graph, vertex_cover=None):
    position = q.spring_layout(graph)
    q.draw(graph, position, with_labels=True, node_color='blue', node_size=850)
    if vertex_cover:
        q.draw_networkx_nodes(graph, position, nodelist=vertex_cover, node_color='yellow', node_size=850)
    plot.title("Vertex Cover Algorithm Graph")
    plot.show()

n = 10  
p = 0.2  
graph = random_graph(n, p)
print("Graph:")
print("Nodes:", graph.nodes())
print("Edges:", graph.edges())
vertex_cover = approx_vertex_cover_algorithm(graph)
print("Vertex Cover:", vertex_cover)
plot_graph(graph, vertex_cover)


'''
output:
Graph:
Nodes: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Edges: [(0, 9), (1, 4), (1, 8), (2, 4), (3, 9), (4, 5), (5, 7), (6, 8), (7, 9), (8, 9)]
Vertex Cover: {0, 1, 4, 5, 6, 7, 8, 9}
'''
