import pytest
from bank import BankAccount

def test_deposit():
    account = BankAccount(
        "Ahmed",
        "100001",
        10000
    )
    
    account.deposit(5000)
    assert account.get_balance() == 15000
    
def test_withdraw():
    account = BankAccount(
        "Ahmed",
        "100001",
        10000
    )
    
    account.withdraw(3000)
    
    assert account.get_balance() == 7000
    
def test_insufficient_funds():
    account = BankAccount(
        "Ahmed",
        "100001",
        10000
    )
    
    with pytest.raises(ValueError):
        account.withdraw(20000)
        