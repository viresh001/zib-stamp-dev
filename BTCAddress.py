import time
import json
import urllib.parse
import urllib.request
import hmac
import hashlib
import ecdsa

class BTCAddress:
	__nonce_v = ''
	__encode_type = 'utf-8'

	def __init__(self):
		print ("constructor")


	def __nonce(self):
		self.__nonce_v = '{:.10f}'.format(time.time() * 1000).split('.')[0]
		print("nonce: " + self.__nonce_v)

	def __get_timestamp(self):
		print("__get_timestamp")


	def generate_address(self, data):
		e_data = data.encode(self.__encode_type)
		hash = hashlib.sha256(e_data).hexdigest()

		print(hash)

		#vhash = hashlib.new('ripemd160')
		#vhash.update(hash)

		#print(vhash.hexdigest())