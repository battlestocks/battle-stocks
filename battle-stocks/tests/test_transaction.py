import pytest
from battle_stocks.classes.transaction import Transaction
from battle_stocks.utils.constants import STOCKS
from battle_stocks.utils.scraping import get_current_stock_price

@pytest.fixture
def apple():
  apple = Transaction('apple', STOCKS.APPLE, 10, 'buy')
  return apple

@pytest.mark.transaction
def test_transaction(apple):
  assert apple.name == 'apple'

@pytest.mark.transaction
def test_transacion_qty(apple):
  assert apple.qty == 10

@pytest.mark.transaction
def test_transacion_symbol(apple):
  assert apple.symbol == STOCKS.APPLE

@pytest.mark.transaction
def test_transacion_get_price(apple):
  actual = float(get_current_stock_price(STOCKS.APPLE))
  assert apple.get_current_price() == actual

@pytest.mark.transaction
def test_transacion_get_value(apple):
  price = round(float(get_current_stock_price(STOCKS.APPLE)),2)
  actual = round(price * 10, 2)
  assert round(apple.get_current_value(),2) == actual

@pytest.mark.transaction
def test_get_history(apple):
  apple.get_price_history()
  assert len(apple.price_history) > 10
