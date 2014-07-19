import unittest
import BTCAddress
import LoadAsset

class BTCAddressTest(unittest.TestCase):

    count_max = 1000000
    asset_name = 'scratch'

    def test_get_btc_address(self):

        la = LoadAsset.LoadAsset()
        asset_content = la.load_asset(self.asset_name)


        test_count=0
        while test_count < self.count_max:
            test_addy = BTCAddress.BTCAddress()
            btc_address001 = test_addy.make_btc_address(asset_content)
            assert isinstance(btc_address001,object)
            self.assertIsInstance(btc_address001, object)
            print('test#', test_count, 'timestamp:', test_addy.timestamp, 'address001:', btc_address001)
            test_count += 1

if __name__ == "__main__":
    unittest.main()
