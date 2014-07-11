import os
import sys, getopt
import time
import binascii, ecdsa, hashlib

import urllib.parse
import urllib.request



class BTCAddress:
    __nonce_v = ''
    __encode_type = 'utf-8'

    def __init__(self):
        print("constructor")


    def __nonce(self):
        self.__nonce_v = '{:.10f}'.format(time.time() * 1000).split('.')[0]
        print("nonce: " + self.__nonce_v)

    def __get_timestamp(self):
        now = time.time()
        return time.strftime('%Y%m%d%H%M%S', time.gmtime(now)) + ('%03d' % int((now-int(now)) *1000))


    def generate_address(self, data):
        ts_data =  data + self.__get_timestamp();
        e_data = ts_data.encode(self.__encode_type)
        hash = hashlib.sha256(e_data).hexdigest()

        print(hash)

        # vhash = hashlib.new('ripemd160')
        # vhash.update(hash)

        #print(vhash.hexdigest())