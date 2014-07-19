import unittest
import BTCAddress

class BTCAddressTest(unittest.TestCase):

    count_max = 1000000

    def test_get_btc_address(self):
        f = open('scratch', 'rb', buffering=0)
        c = f.read()

        test_count=0
        while test_count < self.count_max:
            test_addy = BTCAddress.BTCAddress()
            btc_address001 = test_addy.make_btc_address(c)
            assert isinstance(btc_address001,object)
            self.assertIsInstance(btc_address001, object)
            print('test#', test_count, 'address001:', btc_address001)
            test_count += 1

if __name__ == "__main__":
    unittest.main()
