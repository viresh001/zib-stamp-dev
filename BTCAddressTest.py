import unittest
import BTCAddress

class BTCAddressTest(unittest.TestCase):
    def test_get_btc_address(self):
        test_addy = BTCAddress.BTCAddress()
        runs=0
        while runs < 100:
            btc_address001 = test_addy.get_btc_address("viresh")
            btc_address002 = test_addy.get_btc_address2("viresh")
            self.assertEqual(btc_address001, btc_address002)
            runs += 1

if __name__ == "__main__":
    unittest.main()
