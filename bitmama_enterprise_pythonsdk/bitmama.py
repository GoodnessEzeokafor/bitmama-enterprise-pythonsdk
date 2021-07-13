'''


  getRate: async(ticker: Ticker) => {
    return await resources.rates.rates(Enterprise.BASE_URL, Enterprise.TOKEN,ticker);
  },
  tickers: () => {
    return resources.rates.tickers();
  },
  createWebhook: (endpoint: string) => {
    return resources.webhooks.create(Enterprise.BASE_URL, Enterprise.TOKEN, endpoint);
  },

  listBanks: (countryCode:BankCountryCode) => {
    return resources.banks.list(Enterprise.BASE_URL, Enterprise.TOKEN,countryCode);
  },
  resolveBankAccount: (param:BankResolveParam) => {
    return resources.banks.resolve(Enterprise.BASE_URL, Enterprise.TOKEN, param);
  },
'''
from bank import Bank
from config import TICKERS
from rate import Rate
from wallet import Wallet
from webhook import Webhook
class Bitmama():
    def __init__(self, token, environment) -> None:
        self._token = token
        self._environment = environment
        self.wallet = Wallet(self._token, self._environment)
        self.rate = Rate(self._token, self._environment)
        self.webhook = Webhook(self._token, self._environment)
        self.banks = Bank(self._token, self._environment)
    def tickers(self):
      '''
      returns all tickers used on bitmama
      '''
      return TICKERS
if __name__ == "__main__":
    bitmama = Bitmama('3ee3701e057b26c6b55d0bee2', "dev")
    # print(bitmama.wallet.create_ripple_wallet("ripple python sdk"))
    # pagination = {"page":1,"size":40}
    # print(bitmama.wallet.listCryptoWallet("teth", pagination))
    print(bitmama.webhook.get_webhook())

