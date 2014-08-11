import urllib.request

class Blockchain:

    @property
    def send_btc_address(self):
        return '1HRz4Jb9rthPDUz4mamMktn5fkwLGwcZjj'

    @property
    def blockchain_url(self):
        return 'http://blockchain.info/q/'

    @property
    def url_verbs(self):
        uv = {0: 'addressfirstseen/',
              1: 'addressbalance/'}
        return uv

    def blockchain_checks(self, v, a):
        web_url =  self.blockchain_url + self.url_verbs[v] + a

        response = urllib.request.urlopen(web_url)
        result = response.read()

        return result