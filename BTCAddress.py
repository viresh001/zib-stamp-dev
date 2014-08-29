import time
import binascii, ecdsa, hashlib

class BTCAddress():
    __timestamp = ''

    @property
    def timestamp(self):
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, v):
        self.__timestamp = v

    @property
    def encode_type(self):
        return 'utf-8'

    @property
    def secp256k1_curve(self):
        return ecdsa.ellipticcurve.CurveFp(
            115792089237316195423570985008687907853269984665640564039457584007908834671663, 0, 7)

    @property
    def secp256k1_point(self):
        return ecdsa.ellipticcurve.Point(self.secp256k1_curve,
            0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
            0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8,
            0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141)

    @property
    def secp256k1(self):
        return ecdsa.curves.Curve('secp256k1', self.secp256k1_curve, self.secp256k1_point, (1, 3, 132, 0, 10))

    @property
    def b58_digits(self):
        return '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

    @property
    def __b58_len(self):
        return len(self.b58_digits)

    def __init__(self):
        now = time.time()
        ts= time.strftime('%Y%m%d%H%M%S', time.gmtime(now)) + ('%03d' % int((now - int(now)) * 1000))
        self.timestamp = ts

    def __make_privatekey(self, v):
        return int(hashlib.sha256(v).hexdigest(), 16)

    def __base58_encode(self, v):
        if (v < 0):
            return ''

        encode = ''

        while v >= self.__b58_len:
            v, mod = divmod(v, self.__b58_len)
            encode = self.b58_digits[mod] + encode

        if v > 0:
            encode = self.b58_digits[v] + encode

        return self.b58_digits[0] + encode

    def __hash_key(self, k):
        pko = ecdsa.SigningKey.from_secret_exponent(k, self.secp256k1)

        pubkey_001 = binascii.hexlify(pko.get_verifying_key().to_string())
        pubkey_002 = hashlib.sha256(binascii.unhexlify(str.encode('04', self.encode_type) + pubkey_001)).hexdigest()

        pubkey_003 = hashlib.new('ripemd160', binascii.unhexlify(pubkey_002)).hexdigest()

        pubkey_004 = hashlib.sha256(binascii.unhexlify('00' + pubkey_003)).hexdigest()
        pubkey_005 = hashlib.sha256(binascii.unhexlify(pubkey_004)).hexdigest()

        pubkey_006 = pubkey_003 + pubkey_005[:8]

        return int(pubkey_006, 16)

    def make_btc_address(self, d):

        data = d + self.timestamp.encode(self.encode_type)

        private_key = self.__make_privatekey(data)

        assert isinstance(private_key, int)

        hash_key = self.__hash_key(private_key)

        assert isinstance(hash_key, int)

        return self.__base58_encode(hash_key)