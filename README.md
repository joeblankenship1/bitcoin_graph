# Bitcoin Graph

The `bitcoin_graph` library makes it simple to produce graphs and matrices of Bitcoin transactions from a single wallet address of a list of wallet addresses.

    This is an alpha release, so please post bugs/requests as you encounter them. Thanks!

## Example

    from bitcoin_graph import bitcoin_graph

    # you can input a single wallet address or a list of dictionaries with metadata
    node_data = [('1DqeUNa3wqJRamTEUMTiUXHAQynQuLh426', {'name': 'Near Genesis'})]

    # this will take a single wallet address of a list of dictionaries with metadata
    edge_data = bitcoin_graph.bitcoin_network(node_data)

    # this will output a Networkx graph object
    graph_object = bitcoin_graph.bitcoin_graph(node_data, edge_data)

    # you can then export to one of several formats
    bitcoin_graph.bitcoin_data_export(graph_object, 'graphml', 'filename')

## Features

* Single or multiple addresses
* Multiple output formats
* Extends Networkx functionality
* Python 3.6+

## Documentation

Docs are forthcoming.

## Bugs/Requests

Please use [Github Issue Tracker](https://github.com/joeblankenship1/bitcoin_graph/issues)

## Changelog

Changelog is forthcoming (will be in same location as Docs).

## License

Copyright Joe Blankenship, 2019

Distributed under the terms of the [GNU GPL-3.0](https://github.com/joeblankenship1/bitcoin_graph/blob/master/LICENSE) license. Bitcoin_graph is free and open-source software.