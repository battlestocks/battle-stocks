import pytest
from battle_stocks.utils.validate_transaction import validate_transaction
from battle_stocks.classes.user import User
from battle_stocks.classes.transaction import Transaction
from battle_stocks.utils.constants import STOCKS
from battle_stocks.classes.input_validation import InputValidation

@pytest.fixture
def user():
  user = User('FluffyKins')
  return user

@pytest.fixture
def apple():
  apple = Transaction('apple', STOCKS.APPLE, 1000000, 'buy')
  return apple

@pytest.mark.validateT
def test_validate_transaction(user):
  assert user.bank.get_balance() == 10000

@pytest.mark.validateT
def test_validate_transaction_failure(user, apple):
  actual = validate_transaction(user, apple)
  assert actual == False

@pytest.mark.validateT
def test_validate_transaction_success(user):
  fb = Transaction('fb', STOCKS.FACEBOOK, 2, 'buy')
  actual = validate_transaction(user, fb)
  assert actual == True

@pytest.mark.iv
def test_iv_start_quit(monkeypatch):
  monkeypatch.setattr('builtins.input', lambda _: 'Y')
  user_input = input('y')
  assert InputValidation.validate_start_quit(user_input) == 'Y'
