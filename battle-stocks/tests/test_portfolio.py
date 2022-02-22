import pytest
from battle_stocks.classes.portfolio import Portfolio
from battle_stocks.classes.transaction import Transaction

class TestObj:
  def __init__(self, name, symbol, qty, type):
    self.name = name
    self.symbol = symbol
    self.qty = qty
    self.type = type

@pytest.mark.portfolio
@pytest.fixture
def T():
  T = TestObj('APPLE', 'AAPL', 10, 'buy')
  return T

@pytest.mark.portfolio
@pytest.fixture
def apple():
  apple = Transaction('APPLE', 'AAPL', 10, 'buy')
  return apple

@pytest.mark.portfolio
@pytest.fixture
def port():
  port = Portfolio()
  return port





@pytest.mark.portfolio
def test_portfolio_created(port):
  assert port

@pytest.mark.portfolio
def test_porfolio_sell_shares_tooMany(port, apple):
  port.add_stock(apple)
  actual = port.sell_shares('APPLE', 'AAPL', 100)
  assert actual == 0
  

@pytest.mark.portfolio
def test_porfolio_sell_shares_1(port, apple):
  port.add_stock(apple)
  actual = port.sell_shares('APPLE', 'AAPL', 1)
  assert actual == apple.get_current_price()
  


