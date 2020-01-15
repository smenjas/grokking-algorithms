# Dijkstra's Algorithm

# A weighted graph, without negative weights.
# For negative weights, use the Bellman-Ford algorithm.
#        / a \
#       6  |  1
#      /   |   \
# start    3    fin
#      \   |   /
#       2  |  5
#        \ b /

# A hash table of the graph.
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

# A hash table to store the costs of each node.
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# A hash table to keep track of the parents of each node.
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# An array to record which nodes we've processed.
processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

#for var in ["graph", "costs", "parents", "processed"]
print("graph = " + str(graph))
print("costs = " + str(costs))
print("parents = " + str(parents))
print("processed = " + str(processed))
