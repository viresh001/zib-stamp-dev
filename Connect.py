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

	def __nonce(self):
		self.__nonce_v = '{:.10f}'.format(time.time() * 1000).split('.')[0]
		print("nonce: " + self.__nonce_v)

