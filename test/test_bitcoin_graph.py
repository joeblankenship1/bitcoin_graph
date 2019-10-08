import unittest
from bitcoin_graph.bitcoin_graph import *


class TestBitcoinGraph(unittest.TestCase):

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

    '''
    def test_bitcoin_data_export_edgelist():
        pass

    def test_bitcoin_data_export_graphml():
        pass

    def test_bitcoin_data_export_adjlist():
        pass

    def test_bitcoin_data_export_csv():
        pass
    '''


if __name__ == "__main__":
    unittest.main()
