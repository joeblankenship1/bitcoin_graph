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
