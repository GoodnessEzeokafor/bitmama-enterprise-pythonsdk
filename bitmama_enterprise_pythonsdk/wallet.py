'''
Wallet module
'''
from base import Base
import trio



class Wallet(Base):
    def __init__(self,token, environment) -> None:
        super().__init__(token, environment)
        self._environment = environment
    
    def create_wallet(self, label, coin):
        # print(coin, label)
        params = dict(label=label,coin=coin)
        api_call = trio.run(self.post,"/address",params)
        return api_call

    def create_celo_wallet(self, label):
        params = dict(label=label,coin="celo")
        api_call = trio.run(self.post,"/address",params)
        return api_call

    def create_btc_wallet(self, label):
        coin = "btc" if self._environment == "production" or self._environment == "prod" else "tbtc"
        params = dict(label=label,coin=coin)
        api_call = trio.run(self.post,"/address",params)
        return api_call

    def create_eth_wallet(self, label):
        coin = "eth" if self._environment == "production" or self._environment == "prod" else "teth"
        params = dict(label=label,coin=coin)
        api_call = trio.run(self.post,"/address",params)
        return api_call


    def create_ripple_wallet(self, label):
        params = dict(label=label,coin="xrp")
        api_call = trio.run(self.post,"/address",params)
        return api_call

    def create_stellar_wallet(self, label):
        params = dict(label=label,coin="xlm")
        api_call = trio.run(self.post,"/address",params)
        return api_call

    def listCryptoWallet(self,coin, pagination):
        params = dict(page=pagination['page'],size=pagination['size'], coin=coin)
        api_call = trio.run(self.get,"/address",params)
        return api_call

    def enterpriseWallet(self):
        '''
        list all wallets created on bitmama enterprise
        '''
        api_call = trio.run(self.get,"/wallet")
        return api_call