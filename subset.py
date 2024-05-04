import numpy as nump
import matplotlib.pyplot as plot
import networkx as network

def generate_random_set(n, mininum, maximum):
    return nump.random.randint(mininum, maximum, size=n)

def subset_sum(nodes, end):
    n = len(nodes)
    p = [[False] * (end + 1) for _ in range(n + 1)]
    p[0][0] = True
    
    for i in range(1, n + 1):
        for j in range(end + 1):
            p[i][j] = p[i - 1][j]
            if j >= nodes[i - 1]:
                p[i][j] |= p[i - 1][j - nodes[i - 1]]
    
    if p[n][end]:
        return True, [nodes[i] for i in range(n) if p[i + 1][end - nodes[i]]]
    else:
        return False, []

def subset_graph(nodes, end):
    g = network.DiGraph()
    g.add_node('Start')
    g.add_node('End')
    for i, num in enumerate(nodes):
        g.add_node(f'{i}', label=str(num))
        g.add_edge('Start', f'{i}')
        g.add_edge(f'{i}', 'End')
    
    solution_exists, subset = subset_sum(nodes, end)
    if solution_exists:
        num_list = list(nodes)
        for num in subset:
            g.add_edge(f'{num_list.index(num)}', 'End')

    pos = network.spring_layout(g)
    edge_colors = ['grey' if edge[1] == 'End' else 'black' for edge in g.edges]
    nx.draw(g, pos, with_labels=True, node_color='white', font_size=15, font_weight='bold', edge_color=edge_colors)
    plot.title(f"Subset Sum {end}")
    plot.show()

if __name__ == "__main__":
    set_size = 7
    mininum = 1
    maximum = 16
    end = 21
    nodes = generate_random_set(set_size, mininum, max_val)
    print("Final set:", nodes)
    subset_graph(nodes, end)

'''
output:
Final set: [ 9 13  4 13 14  2  9]
'''
