from base import Base
from config import NG_BANKS
import trio

class Bank(Base):
    def __init__(self,token, environment) -> None:
        super().__init__(token, environment)
        self._environment = environment
    
    def list_banks(self,code):
        if code == "ng": return NG_BANKS
        return f"No banks for this country code"

    def resolve_bank_account(self):
        pass
