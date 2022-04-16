import pytest

from testproj.payments import Account, bill, InsufficientMoney


def test_bill_success(fake):
    source_amount = 1000
    destination_amount = 2000
    bill_amount = 200

    source = Account(fake.pystr(), amount=source_amount)
    destination = Account(fake.pystr(), amount=destination_amount)

    bill(source, destination, bill_amount)

    assert source.amount == source_amount - bill_amount
    assert destination.amount == destination_amount + bill_amount


def test_insufficient_money(fake):
    source_amount = 50
    destination_amount = 2000
    bill_amount = 200

    source = Account(fake.pystr(), amount=source_amount)
    destination = Account(fake.pystr(), amount=destination_amount)

    with pytest.raises(InsufficientMoney):
        bill(source, destination, bill_amount)

    assert source.amount == source_amount
    assert destination.amount == destination_amount
