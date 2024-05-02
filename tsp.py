import sys

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
    [1, 12, 39, 0],
    [0, 18, 55, 32],
    [21, 34, 20, 0],
    [0, 15, 20, 0]
]
start_city = 0 
min_cost = traveling_salesman(graph, start_city)
print("Minimum cost of TSP tour:", min_cost)

'''
output:
Minimum cost of TSP tour: 54
'''
