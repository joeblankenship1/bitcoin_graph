import unittest
from bitcoin_graph.bitcoin_graph import *


class TestBitcoinGraph(unittest.TestCase):

    def test_timestamp_conv(self):
        data = 1570418869
        self.assertEqual(timestamp_conv(data), '2019-10-07 03:27:49', "Should be 2019-10-07 03:27:49")

    '''
    def test_bitcoin_data():
        pass

    def test_bitcoin_network():
        pass

    def test_bitcoin_graph():
        pass

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
