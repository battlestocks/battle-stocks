import pytest
from battle_stocks.classes.portfolio import Portfolio
from battle_stocks.classes.transaction import Transaction
from battle_stocks.utils.constants import STOCKS
from battle_stocks.utils.scraping import get_current_stock_price

@pytest.mark.portfolio
@pytest.fixture
def apple():
  apple = Transaction('APPLE', 'AAPL', 10, 'buy')
  return apple

@pytest.mark.portfolio
@pytest.fixture
def fb():
    fb = Transaction('book_face', STOCKS.FACEBOOK, 10, 'buy')
    return fb

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
  
@pytest.mark.portfolio
def test_portfolio_add_stock(apple, port):
  port.add_stock(apple)
  actual = port.stocks[0].name
  assert actual == 'APPLE'

@pytest.mark.portfolio
def test_portfolio_sell_some_stock(apple, port, fb):
  port.add_stock(fb)
  port.add_stock(apple)
  port.sell_shares('book_face', STOCKS.FACEBOOK, 5)
  actual = port.stock_shares['book_face']
  assert actual == 5

@pytest.mark.portfolio
def test_portfolio_sell_all_fb_stock(apple, port, fb):
  port.add_stock(apple)
  port.add_stock(fb)
  port.sell_shares('book_face', STOCKS.FACEBOOK, 10)
  actual = port.stock_shares['book_face']
  assert actual == 0

@pytest.mark.portfolio
def test_portfolio_sell_remove_held_stock(apple, port, fb):
  port.add_stock(apple)
  port.add_stock(fb)
  port.sell_shares('book_face', STOCKS.FACEBOOK, 10)
  actual = len(port.held_stocks)
  assert actual == 1

@pytest.mark.portfolio
def test_portfolio_bad_buy(port):
  with pytest.raises(AttributeError):
    port.add_stock('Apple')

@pytest.mark.portfolio
def test_portfolio_bad_sell(port):
  with pytest.raises(TypeError):
    port.sell_shares('Chicken')

@pytest.mark.portfolio
def test_portfolio_get_value(port):
  ap = Transaction('ap', STOCKS.APPLE, 1, 'buy')
  port.add_stock(ap)
  actual = port.get_portfolio_value()
  current = float(get_current_stock_price(STOCKS.APPLE))
  assert actual == current