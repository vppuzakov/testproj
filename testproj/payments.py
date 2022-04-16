from decimal import Decimal
from dataclasses import dataclass


@dataclass
class Account:
    account: str
    amount: Decimal


class InsufficientMoney(Exception):
    
    def __init__(self, account: Decimal, amount: Decimal) -> None:
        super().__init__(f"Can't bill {account} -> {amount}")
        self.account = account
        self.amount = amount


def bill(source: Account, destination: Account, amount: Decimal):
    if source.amount < amount:
        raise InsufficientMoney(source.amount, amount)

    destination.amount += amount
    source.amount -= amount
