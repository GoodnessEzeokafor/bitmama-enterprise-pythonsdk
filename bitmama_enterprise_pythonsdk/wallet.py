from base import Base
import trio

# from bitmama.base import Base
# class Wallet(Base):
#     @classmethod
#     def create_wallet(cls,label,coin):


class Wallet(Base):
    def __init__(self,token, environment) -> None:
        super().__init__(token, environment)
        self._environment = environment
    # def __init__(self,token, environment, **kwargs) -> None:
    #     super().__init__(token, environment, **kwargs)
    # # def __init__(self, ) -> None:
    # #     self.token = token
    # #     self.environment = environment
    # #     print(kwargs)
    
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
