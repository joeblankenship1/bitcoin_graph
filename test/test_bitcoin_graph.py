import unittest
import hashlib
import os
import pandas as pd
from bitcoin_graph.bitcoin_graph import *


class TestBitcoinGraph(unittest.TestCase):

    # TODO: Need to remove/delete tempfiles for export tests

    def test_timestamp_conv(self):
        data = 1570418869
        self.assertEqual(timestamp_conv(data), '2019-10-07 03:27:49', "Should be 2019-10-07 03:27:49")

    def test_bitcoin_data(self):
        data = '1DqeUNa3wqJRamTEUMTiUXHAQynQuLh426'
        self.assertIn(bitcoin_data(data)[0][0], '1DqeUNa3wqJRamTEUMTiUXHAQynQuLh426', "Should contain 1DqeUNa3wqJRamTEUMTiUXHAQynQuLh426")
        self.assertIn(bitcoin_data(data)[0][1], '1NsooQ8fvpJinqyp3hDtSBUxKMQFUxXEkE', "Should contain 1NsooQ8fvpJinqyp3hDtSBUxKMQFUxXEkE")
        self.assertEqual(bitcoin_data(data)[0][2]["input_value"], 21383, "Should contain 21383")
        self.assertEqual(bitcoin_data(data)[0][2]["output_value"], 7928, "Should contain 7928")
        self.assertIn(bitcoin_data(data)[0][2]["hash"], '2fe15db1f629e873aa7b8ef1e5adc7c323667a6f1eb83cfb5b6cbd04c1329df8', "Should contain 2fe15db1f629e873aa7b8ef1e5adc7c323667a6f1eb83cfb5b6cbd04c1329df8")
        self.assertIn(bitcoin_data(data)[0][2]["time"], '2019-10-07 06:27:39', "Should contain 2019-10-07 06:27:39")
        self.assertIn(bitcoin_data(data)[0][2]["relay"], '127.0.0.1', "Should contain 127.0.0.1")

    def test_bitcoin_network(self):
        data = [('1DqeUNa3wqJRamTEUMTiUXHAQynQuLh426', {'name': 'Near Genesis'})]
        self.assertIn(bitcoin_network(data)[0][0], '1DqeUNa3wqJRamTEUMTiUXHAQynQuLh426', "Should contain 1DqeUNa3wqJRamTEUMTiUXHAQynQuLh426")
        self.assertIn(bitcoin_network(data)[0][1], '1NsooQ8fvpJinqyp3hDtSBUxKMQFUxXEkE', "Should contain 1NsooQ8fvpJinqyp3hDtSBUxKMQFUxXEkE")
        self.assertEqual(bitcoin_network(data)[0][2]["input_value"], 21383, "Should contain 21383")
        self.assertEqual(bitcoin_network(data)[0][2]["output_value"], 7928, "Should contain 7928")
        self.assertIn(bitcoin_network(data)[0][2]["hash"], '2fe15db1f629e873aa7b8ef1e5adc7c323667a6f1eb83cfb5b6cbd04c1329df8', "Should contain 2fe15db1f629e873aa7b8ef1e5adc7c323667a6f1eb83cfb5b6cbd04c1329df8")
        self.assertIn(bitcoin_network(data)[0][2]["time"], '2019-10-07 06:27:39', "Should contain 2019-10-07 06:27:39")
        self.assertIn(bitcoin_network(data)[0][2]["relay"], '127.0.0.1', "Should contain 127.0.0.1")

    def test_bitcoin_graph(self):
        node_data = [('1DqeUNa3wqJRamTEUMTiUXHAQynQuLh426', {'name': 'Near Genesis'})]
        edge_data = bitcoin_network(node_data)
        graph_data = bitcoin_graph(node_data, edge_data)
        self.assertIn(list(graph_data.nodes)[0], '1DqeUNa3wqJRamTEUMTiUXHAQynQuLh426', "Should contain 1DqeUNa3wqJRamTEUMTiUXHAQynQuLh426")
        self.assertIn(list(graph_data.edges)[0][0], '1DqeUNa3wqJRamTEUMTiUXHAQynQuLh426', "Should contain 1DqeUNa3wqJRamTEUMTiUXHAQynQuLh426")

    def test_bitcoin_data_export_edgelist(self):
        expected_hash = 'a5d9bca17ae7a76e31daea9d984936ee'
        node_data = [('1DqeUNa3wqJRamTEUMTiUXHAQynQuLh426', {'name': 'Near Genesis'})]
        edge_data = bitcoin_network(node_data)
        graph_data = bitcoin_graph(node_data, edge_data)
        bitcoin_data_export(graph_data, 'edgelist', 'test')
        md5_hash = hashlib.md5()
        with open('test.edgelist', "rb") as f:
            for chunk in iter(lambda: f.read(4098), b""):
                md5_hash.update(chunk)
        self.assertEqual(md5_hash.hexdigest(), expected_hash, f"Should be {expected_hash}")

    def test_bitcoin_data_export_graphml(self):
        expected_hash = '4fedad68b59a7c37105a2b54385782e8'
        node_data = [('1DqeUNa3wqJRamTEUMTiUXHAQynQuLh426', {'name': 'Near Genesis'})]
        edge_data = bitcoin_network(node_data)
        graph_data = bitcoin_graph(node_data, edge_data)
        bitcoin_data_export(graph_data, 'graphml', 'test')
        md5_hash = hashlib.md5()
        with open('test.graphml', "rb") as f:
            for chunk in iter(lambda: f.read(4098), b""):
                md5_hash.update(chunk)
        self.assertEqual(md5_hash.hexdigest(), expected_hash, f"Should be {expected_hash}")

    def test_bitcoin_data_export_adjlist(self):
        # TODO: hash output is inconsistent; need to examine adjlist output
        expected_hash = '569d25ec97fdeaeff676aa2131e436e9'
        node_data = [('1DqeUNa3wqJRamTEUMTiUXHAQynQuLh426', {'name': 'Near Genesis'})]
        edge_data = bitcoin_network(node_data)
        graph_data = bitcoin_graph(node_data, edge_data)
        bitcoin_data_export(graph_data, 'adjacencylist', 'test')
        md5_hash = hashlib.md5()
        with open('test.adjlist', "rb") as f:
            for chunk in iter(lambda: f.read(4098), b""):
                md5_hash.update(chunk)
        self.assertEqual(md5_hash.hexdigest(), expected_hash, f"Should be {expected_hash}")

    def test_bitcoin_data_export_adjmatrix(self):
        expected_hash = 'e82afed32d1ef7772e371bddc810b1c1'
        node_data = [('1DqeUNa3wqJRamTEUMTiUXHAQynQuLh426', {'name': 'Near Genesis'})]
        edge_data = bitcoin_network(node_data)
        graph_data = bitcoin_graph(node_data, edge_data)
        bitcoin_data_export(graph_data, 'adjacencymatrix', 'test')
        md5_hash = hashlib.md5()
        with open('test.csv', "rb") as f:
            for chunk in iter(lambda: f.read(4098), b""):
                md5_hash.update(chunk)
        self.assertEqual(md5_hash.hexdigest(), expected_hash, f"Should be {expected_hash}")


if __name__ == "__main__":
    unittest.main()
