import unittest
import BTCAddress

class BTCAddressTest(unittest.TestCase):

    def test_get_btc_address(self):
        test_addy = BTCAddress.BTCAddress()
        runs=0
        while runs < 10000:
            btc_address001 = test_addy.get_btc_address("war-pig")
            btc_address002 = test_addy.get_btc_address2("war-pig")
            assert isinstance(btc_address001,object)
            assert isinstance(btc_address002, object)
            self.assertEqual(btc_address001, btc_address002)
            print('address: ', runs, ' passed')
            runs += 1

if __name__ == "__main__":
    unittest.main()
