from base import Base
import trio

class Webhook(Base):
    def __init__(self,token, environment) -> None:
        super().__init__(token, environment)
        self._environment = environment
    
    def create_webhook(self, endpoint):
        params = dict(endpoint=endpoint)
        api_call = trio.run(self.post,"/webhook",params)
        return api_call

    def get_webhook(self):
        api_call = trio.run(self.get,"/webhook")
        return api_call
