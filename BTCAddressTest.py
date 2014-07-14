import unittest
import BTCAddress

class BTCAddressTest(unittest.TestCase):

    count_max = 1000000

    def test_get_btc_address(self):
        test_count=0
        while test_count < self.count_max:
            test_addy = BTCAddress.BTCAddress()
            btc_address001 = test_addy.get_btc_address("war-pig")
            btc_address002 = test_addy.get_btc_address2("war-pig")
            assert isinstance(btc_address001,object)
            assert isinstance(btc_address002, object)
            self.assertEqual(btc_address001, btc_address002)
            print('test#', test_count, 'address001:', btc_address001, 'address002:', btc_address002,  'passed')
            test_count += 1

if __name__ == "__main__":
    unittest.main()
