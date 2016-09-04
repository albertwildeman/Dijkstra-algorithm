import os
import numpy as np

def get_graph(filename, graph_format):

    npy_version_exists = os.path.isfile(filename + ".npy")
    if not npy_version_exists:
        txt_to_npy(filename, graph_format)

    return np.load(filename + ".npy")


def txt_to_npy(filename, graph_format):

    filepath = os.getcwd() + "\\" + filename + ".txt"
    file_graph = open(filepath)

    nLines = sum(1 for line in file_graph)
    file_graph.seek(0, 0)

    if graph_format == 1:
        # This format holds en edge list for a directed graph, with the first entry on each line holding
        # the node the vertex goes out from and the second entry holding the node it goes to.
        graph = np.zeros((nLines, 2), dtype=np.int32)

        for iLine, line in enumerate(file_graph):
            graph[iLine,0], graph[iLine,1] = line.split(" ")[:2]

        file_graph.close()
        np.save(filename, graph)

    elif graph_format == 2:
        # Adjacency list fomat. Each line holds for the node (number=line number) pairs for each outgoing vertex.
        # In each pair, the first number is the number of the node at the receiving end of the vertex and the
        # second number is the edge length.
        # Save as a list of numpy arrays.
        graph = []

        file_graph.seek(0, 0)
        for iLine, line in enumerate(file_graph):

            local_edges = [x.split(",") for x in line.split("\t")[1:-1]]
            # Deduct 1 from the node number (x) to get 0-based node numbers
            graph.append(np.array([(int(x) - 1, int(y)) for x, y in local_edges]))

        file_graph.close()
        np.save(filename, graph)

    else:
        raise NameError("Specified graph format not defined.")