from GraphReadLib import get_graph
from DijkstraLib import dijkstra
import numpy as np


# Read graph from file
graph = get_graph("dijkstraData", 2)

# Apply Dijkstra's algorithm to find length of shortest path to all nodes, given a starting node.
start_node = 0
short_paths = dijkstra(graph, start_node)

Assignment_nodes = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]

answer = [short_paths[x-1] for x in Assignment_nodes]
ans_str = str(answer).replace(" ","")[1:-1]
print("Answer: " + ans_str)
print("main.py: Done.")