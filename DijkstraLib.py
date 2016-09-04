import numpy as np

def dijkstra(g, start_node):
    # Computes length of shortest path from starting node to every other node in the given graph.

    # Get number of nodes
    nNodes = len(g)

    # Initialize array holding exploration status of nodes (1 is explored:
    explored = np.zeros(nNodes, dtype=np.bool)
    explored[start_node] = 1
    # also initialize list holding all the explored nodes
    expl_list = [start_node]

    # Initialize array to hold output
    short_paths = np.zeros(nNodes, dtype=np.int32)

    # Get sum of all edgelengths in graph. Will be used to disqualify some paths.
    disqualifier = sum([sum(x[:,1]) for x in g])

    for nodesExplored in range(1,nNodes):

        minScore = disqualifier

        for iNode in expl_list:

            edges_to_explored = explored[g[iNode][:, 0]]
            # Initialize minimum score to infinity
            edgelengths_from_node = ( disqualifier * edges_to_explored
                                               + g[iNode][:, 1])
            candidate_edge = np.argmin(edgelengths_from_node)
            node_minScore = short_paths[iNode] + edgelengths_from_node[candidate_edge]
            if node_minScore < minScore:
                minScore = node_minScore
                exploreNode = g[iNode][candidate_edge, 0]

        # Add node to list of explored nodes
        explored[exploreNode] = True
        expl_list.append(exploreNode)

        # Set shortest path length for node
        short_paths[exploreNode] = minScore

    return short_paths