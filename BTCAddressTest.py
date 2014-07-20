import unittest
import BTCAddress
import LoadAsset
import Blockchain

class BTCAddressTest(unittest.TestCase):

    count_max = 32
    asset_name = 'scratch'

    def test_btc_address(self):

        la = LoadAsset.LoadAsset()
        asset_content = la.load_asset(self.asset_name)

        test_count=0

        while test_count < self.count_max:
            test_addy = BTCAddress.BTCAddress()

            ba = test_addy.make_btc_address(asset_content)
            self.assertIsInstance(ba, str)

            print('test#', test_count, 'timestamp:', test_addy.timestamp, 'address001:', ba)

            bc = Blockchain.Blockchain()

            addy_check = bc.blockchain_checks(0,ba)
            self.assertEqual(addy_check, b'0')

            balance_check = bc.blockchain_checks(1, ba)
            self.assertEqual(balance_check, b'0')

            test_count += 1


if __name__ == "__main__":
    unittest.main()
