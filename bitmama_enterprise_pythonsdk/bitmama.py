from base import Base
from wallet import Wallet
class Bitmama():
    def __init__(self, token, environment) -> None:
        self._token = token
        self._environment = environment
        # Base.__init__(self,data=dict(token=token, environment=environment))
        # resources
        self.wallet = Wallet(self._token, self._environment)
    # def wallet(self):
    #     return Wallet(self._token, self._environment)
if __name__ == "__main__":
    bitmama = Bitmama('3ee3701e057b26c6b55d0bee2', "dev")
    # print(bitmama.get_base_url())
    print(bitmama.wallet.create_ripple_wallet("ripple python sdk"))