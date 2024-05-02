import networkx as q
import random
import matplotlib.pyplot as plt
import time

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
    plt.title("Vertex Cover Algorithm Graph")
    plt.show()

def benchmark(num, prob, runs):
    results = {}  
    for n in num:
        for p in prob:
            total_timetaken = 0
            for _ in range(runs):
                G = random_graph(n, p)
                start_timetaken = time.time()
                vertex_cover = approx_vertex_cover_algorithm(G)
                end_timetaken = time.time()
                total_timetaken += end_timetaken - start_timetaken
                
            average_time = total_timetaken / runs
            results[(n, p)] = average_time
    return results

num = [10, 20, 30, 40, 50, 60, 70, 80, 90] 
prob = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9] 
runs = 10
benchmark_results = benchmark(num, prob, runs)
plt.figure(figsize=(8, 5))
for n in num:
    average_times = [benchmark_results[(n, p)] for p in prob]
    plt.plot(prob, average_times, label=f'n={n}')
plt.xlabel('Probability (p)')
plt.ylabel('Average Time')
plt.title('Benchmark Vertex Cover Algorithm')
plt.legend()
plt.grid(True)
plt.show()
