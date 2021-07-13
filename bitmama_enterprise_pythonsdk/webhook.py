from base import Base

class Webhook(Base):
    def __init__(self,token, environment) -> None:
        super().__init__(token, environment)
        self._environment = environment