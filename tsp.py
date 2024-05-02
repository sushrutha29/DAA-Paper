import sys
import networkx as nx
import matplotlib.pyplot as plt

def traveling_salesman(graph, startnode):
    n = len(graph)
    memory = {}  
    def traveling_salesman_helper(currentnode, visitednode):
        if (currentnode, visitednode) in memory:
            return memory[(currentnode, visitednode)]
        if visitednode == (1 << n) - 1:
            return graph[currentnode][startnode]

        min_cost = sys.maxsize
        for city in range(n):
            if (visitednode >> city) & 1 == 0: 
                new_visitednode = visitednode | (1 << city)  
                cost = graph[currentnode][city] + traveling_salesman_helper(city, new_visitednode)
                min_cost = min(min_cost, cost)

        memory[(currentnode, visitednode)] = min_cost
        return min_cost
    
    return traveling_salesman_helper(startnode, 1 << startnode)

graph = [
    [1, 14, 39, 0],
    [0, 18, 55, 44],
    [21, 23, 20, 0],
    [0, 13, 20, 0]
]
start_city = 0 
min_cost = traveling_salesman(graph, start_city)
print("Minimum cost:", min_cost)

# Create a graph from the input graph
G = nx.Graph()
for i in range(len(graph)):
    for j in range(len(graph)):
        if graph[i][j] != 0:
            G.add_edge(i, j, weight=graph[i][j])

# Plot the graph
pos = nx.spring_layout(G)
plt.figure(figsize=(4, 5))
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='white', font_size=20, font_weight='bold')
plt.title("TSP Tour")
plt.show()


'''
output:
Minimum cost : 43
'''
