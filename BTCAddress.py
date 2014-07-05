import time
import json
import urllib.parse
import urllib.request
import hmac
import haslib

class BTCAddress:
	__nonce_v = ''
	__encode_type = 'utf-8'

	def __init__(self):

	

    def __get-timestamp(self):
    	return "time"

	def __nonce(self):
		self.__nonce_v = '{:.10f}'.format(time.time() * 1000).split('.')[0]
		print("nonce: " + self.__nonce_v)


	def GenerateAddress(self, data):
		e_data = data.encode(self.__encode_type)
		hash = haslib.sha256(e_data).hexdigest()

		print(hash)

		vhash = haslib.new('ripemd160')
		vhash.update(hash)

		print(vhash.hexdigest())