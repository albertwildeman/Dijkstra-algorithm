from GraphReadLib import get_graph
import numpy as np


# Read graph from file
g = get_graph("dijkstraData", 2)

# Apply Dijkstra's algorithm to find length of shortest path to all nodes, given a starting node.
short_paths = dijkstra(graph, start_node)

print("main.py: Done.")