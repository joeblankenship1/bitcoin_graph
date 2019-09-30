import unittest
import bitcoin_graph

class TestBitcoinGraph:

    def test_timestamp_conv():
        data = ''
        timestamp = bitcoin_graph.timestamp_conv(data)
        # assert timestamp == ''
        # ValueError 

    def test_bitcoin_data():
        data = []
        bitcoin_trans = bitcoin_graph.bitcoin_data(data)
        # assert bitcoin_trans == []
        # Error

    def test_bitcoin_network():
        pass

    def test_bitcoin_graph():
        pass

    def test_bitcoin_data_export():
        # TODO: Need to make sure the exceptions are set each export with corresponding export error
        pass


if __name__ == "__main__":
    unittest.main()
