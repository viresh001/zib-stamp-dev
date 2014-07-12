import os
import sys, getopt
import time
import binascii, ecdsa, hashlib

import urllib.parse
import urllib.request


class BTCAddress:
    __nonce_v = ''
    __encode_type = 'utf-8'
    __secp256k1_curve = ecdsa.ellipticcurve.CurveFp(
        115792089237316195423570985008687907853269984665640564039457584007908834671663, 0, 7)
    __secp256k1_point = ecdsa.ellipticcurve.Point(__secp256k1_curve,
                                                  0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
                                                  0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8,
                                                  0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141)
    __secp256k1 = ecdsa.curves.Curve('secp256k1', __secp256k1_curve, __secp256k1_point, (1, 3, 132, 0, 10))


    def __init__(self):
        print("constructor")


    def __nonce(self):
        self.__nonce_v = '{:.10f}'.format(time.time() * 1000).split('.')[0]
        print("nonce: " + self.__nonce_v)

    def __get_timestamp(self):
        now = time.time()
        return time.strftime('%Y%m%d%H%M%S', time.gmtime(now)) + ('%03d' % int((now - int(now)) * 1000))

    def __get_privatekey(self, data):
        return int(hashlib.sha256(data).hexdigest(), 16)

    def __base58_check_encoding(self, v):
        alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
        iseq = lambda s: s
        bseq = bytes
        buffer = lambda s: s.buffer

        origlen = len(v)
        v = v.lstrip(str('\0'))
        newlen = len(v)

        p, acc = 1, 0
        print(type(p))
        for c in iseq(v[::-1]):
            acc += p * int(c)
            p = p << 8

        result = ''
        while acc >= 58:
            acc, mod = divmod(acc, 58)
            result += alphabet[mod]

        return (result + alphabet[acc] + alphabet[0] * (origlen - newlen))[::-1]


    def generate_address(self, data):
        ts_data = data #+ self.__get_timestamp();
        e_data = ts_data.encode(self.__encode_type)
        private_key = self.__get_privatekey(e_data)

        pko = ecdsa.SigningKey.from_secret_exponent(private_key, self.__secp256k1)
        pubkey_001 = binascii.hexlify(pko.get_verifying_key().to_string())
        pubkey_002 = hashlib.sha256(binascii.unhexlify(str.encode('04', self.__encode_type) + pubkey_001)).hexdigest()

        pubkey_003 = hashlib.new('ripemd160', binascii.unhexlify(pubkey_002)).hexdigest()

        pubkey_004 = hashlib.sha256(binascii.unhexlify('00' + pubkey_003)).hexdigest()
        pubkey_005 = hashlib.sha256(binascii.unhexlify(pubkey_004)).hexdigest()

        pubkey_006 = pubkey_003 + pubkey_005[:8]

        print("pubkey006")
        print(int(pubkey_006, 16))

        pubkey_007 = str(int(pubkey_006, 16))

        btc_address = self.__base58_check_encoding(pubkey_007)

        print(pko.to_string())
        print(pubkey_001)
        print(pubkey_002)
        print(pubkey_003)
        print(pubkey_004)
        print(pubkey_005)
        print(pubkey_006)
        print(pubkey_007)
        print(btc_address)


    # vhash = hashlib.new('ripemd160')
    # vhash.update(hash)

    # print(vhash.hexdigest())