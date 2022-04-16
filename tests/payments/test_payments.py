from decimal import Decimal
import pytest

from testproj.payments import Account, bill, InsufficientMoney


@pytest.fixture
def account(fake):
    
    def inner(name: str = None, amount: Decimal = None):
        return Account(
            account=name or fake.pystr(),
            amount=amount or fake.pyint(),
        )

    return inner


@pytest.mark.parametrize('source_amount, bill_amount', [
    (1000, 200),
    (50, 50),
])
def test_bill_success(fake, account, source_amount, bill_amount):
    destination_amount = fake.pyint()

    source = account(amount=source_amount)
    destination = account(amount=destination_amount)

    bill(source, destination, bill_amount)

    assert source.amount == source_amount - bill_amount
    assert destination.amount == destination_amount + bill_amount


def test_insufficient_money(fake, account):
    source_amount = 50
    bill_amount = 200

    destination_amount = fake.pyint()
    source = account(amount=source_amount)
    destination = account(amount=destination_amount)

    with pytest.raises(InsufficientMoney):
        bill(source, destination, bill_amount)

    assert source.amount == source_amount
    assert destination.amount == destination_amount
