from base import Base
import trio

class Rate(Base):
    def __init__(self,token, environment) -> None:
        super().__init__(token, environment)
        self._environment = environment
    
    def getRate(self, ticker):
        params = dict(ticker=ticker)
        api_call = trio.run(self.get,"/rate",params)
        return api_call