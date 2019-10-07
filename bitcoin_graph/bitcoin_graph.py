#!/usr/bin/env python3
"""
This is a library for processing API outputs from the blockchain.com API
into networkx graph objects.
"""

__author__ = "Joe Blankenship"
__version__ = "19.0.1"
__license__ = "GPL3"


from datetime import datetime
import network as nx
from blockchain import blockexplorer as bce

# TODO: build feature for offline import for data - need data format standards from JSON
# TODO: type hints for each method
# TODO: link to tests for lib - expected outputs


def timestamp_conv(time_stamp):
    """
    This function converts unix times to datetime groups
    """
    time_formatted = datetime.utcfromtimestamp(time_stamp).strftime('%Y-%m-%d %H:%M:%S')
    return time_formatted


def bitcoin_data(address):
    """
    Gather and format the Bitcoin data for a given address
    Output schema as Tuple:
        input address,
        output address,
        {
        input value
        output value
        transaction hash
        transaction time
        transaction relay
        }
    """
    transaction_pairs = []
    input_address = bce.get_address(address)
    transactions = input_address.transactions
    for event in transactions:
        for i in event.inputs:
            for o in event.outputs:
                transaction_pairs.append(tuple([i.address,
                                                o.address,
                                                {
                                                 'input_value': i.value,
                                                 'output_value': o.value,
                                                 'hash': event.hash,
                                                 'time': timestamp_conv(event.time),
                                                 'relay': event.relayed_by
                                                 }
                                                ]))
    return transaction_pairs


def bitcoin_network(node_data):
    """
    Iterate over node addresses
    Download transactions for addresses
    generate edge list for network
    """
    network_data = []
    for i in node_data:
        network_data.append(bitcoin_data(i[0]))
    network_data_combine = []
    for i in network_data:
        for j in i:
            network_data_combine.append(j)
    return network_data_combine


def bitcoin_graph(node_data, edge_data):
    """
    Generate graph object of bitcoin transactions
    """
    graph_object = nx.DiGraph()
    graph_object.add_nodes_from(node_data)
    graph_object.add_edges_from(edge_data)
    return graph_object


def bitcoin_data_export(graph_data, type, filename):
    """
    export data in one of these formats:
        edgelist
        graphml
        adjacencylist
        adjacencymatrix
    """
    if type.lower() == 'edgelist':
        nx.write_edgelist(graph_data, f'data/{filename}.edgelist')
    elif type.lower() == 'graphml':
        nx.write_graphml(graph_data, f'data/{filename}.graphml')
    elif type.lower() == 'adjacencylist':
        nx.write_adjlist(graph_data, f'data/{filename}.adjlist')
    elif type.lower() == 'adjacencymatrix':
        dataframe = nx.convert_matrix.to_pandas_adjacency(graph_data)
        dataframe.to_csv(f'data/{filename}.csv')
    else:
        'Please enter one of the following options: edgelist; graphml; adjacencylist, adjacencymatrix.'

# TODO: link to main() once CLI features complete
if __name__ == "__main__":
    """ This is executed when run from the command line """
    #main()
    print('This is currently in an importable state only and is not intended for direct use')
