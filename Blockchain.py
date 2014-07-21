import urllib.request

class Blockchain:

    __send_btc_address = '1HRz4Jb9rthPDUz4mamMktn5fkwLGwcZjj'
    __blockchain_url = 'http://blockchain.info/q/'
    __verbs = {0: 'addressfirstseen/',
               1: 'addressbalance/'}

    def blockchain_checks(self, v, a):
        web_url =  self.__blockchain_url + self.__verbs[v] + a

        response = urllib.request.urlopen(web_url)
        result = response.read()

        return result