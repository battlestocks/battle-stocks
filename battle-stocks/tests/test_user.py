from curses.ascii import US
import pytest
from battle_stocks.classes.user import User

@pytest.fixture
def Fluffy():
  Fluffy = User('Fluffykins')
  return Fluffy

@pytest.mark.user
def test_user_created(Fluffy):
  assert Fluffy.bank.get_balance() == 10000

@pytest.mark.user
def test_user_portfolio(Fluffy):
  assert Fluffy.portfolio

@pytest.mark.user
def test_user_name(Fluffy):
  assert Fluffy.name == 'Fluffykins'