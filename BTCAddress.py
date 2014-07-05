import time
import json
import urllib.parse
import urllib.request
import hmac
import haslib

class Connect:
	__username = ''
	__api_key = ''
	__api_secret = ''
	__nonce_v = ''
	__encode_type = 'utf-8'

	def __init__(self, username, api_key, api_secret):
		self.__username = username
		self.__api_key = api_key
		self.__api_secret = api_secret

	def GenerateAddress(self, data):
		#https://en.bitcoin.it/wiki/Technical_background_of_Bitcoin_addresses#How_to_create_Bitcoin_Address
		#hash data using sha256
		#hash the hash with ripemd160
		#verion byte (0x00) is added to the beginning (CONCAT)
		#checksum - first 4 bytes of sha256(sha256(vhash)) is added to the end
		#convert to base58


	def __nonce(self):
		self.__nonce_v = '{:.10f}'.format(time.time() * 1000).split('.')[0]
		print("nonce: " + self.__nonce_v)

