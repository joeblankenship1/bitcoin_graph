import unittest
import bitcoin_graph

class TestBitcoinGraph(unittest.TestCase):

    def test_timestamp_conv(self):
        data = 1570418869
        self.assertEqual(bitcoin_graph.timestamp(data), '2019-10-07 03:27:49', 'Should be 2019-10-07 03:27:49')

    '''
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
    '''


if __name__ == "__main__":
    unittest.main()
