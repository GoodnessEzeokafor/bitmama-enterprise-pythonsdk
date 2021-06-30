from bitmama.base import Base
class Bitmama(Base):
    def __init__(self, token, environment) -> None:
        super().__init__(token, environment)
        # resources