import datetime
from battle_stocks.utils.scraping import get_current_stock_price
from battle_stocks.utils.constants import SYMBOL


class Transaction:
  def __init__(self, symbol, qty):
    self.symbol = symbol
    self.qty = qty
    self.purchased_price = get_current_stock_price(symbol)
    self.purchased_date = datetime.datetime.now().date()
    self.price_history = {}

  def sell_stock(self, qty):
      current_price = float(get_current_stock_price(self.symbol))
      self.qty -= qty
      self.sold_date = datetime.datetime.now().date()
      return current_price * qty

  def get_current_price(self):
    current_price = get_current_stock_price(self.symbol)
    return float(current_price)

  def get_current_value(self):
    return self.qty * self.get_current_price()
  
  def current_total_value(self):
    current_price = float(get_current_stock_price(self.symbol))
    return current_price * self.qty

  def get_price_history(self):
    # Need function to get price history data { date: price }
    # data = float(get_price_history(self.symbol))
    # self.price_history = data
    d1 = datetime.date.fromisoformat('2022-02-13')
    d2 = datetime.date.fromisoformat('2022-02-14')
    d3 = datetime.date.fromisoformat('2022-02-15')
    d4 = datetime.date.fromisoformat('2022-02-16')
    d5 = datetime.date.fromisoformat('2022-02-17')
    self.price_history = { d1: 50, d2: 52, d3: 55, d4: 60, d5: 62 }

  def get_price_history2(self):
    d1 = datetime.date.fromisoformat('2022-02-13')
    d2 = datetime.date.fromisoformat('2022-02-14')
    d3 = datetime.date.fromisoformat('2022-02-15')
    d4 = datetime.date.fromisoformat('2022-02-16')
    d5 = datetime.date.fromisoformat('2022-02-17')
    self.price_history = { d1: 77, d2: 88, d3: 80, d4: 76, d5: 79 }
 
  @staticmethod
  def buy_stock(symbol, qty):
    # Returns a Transaction instance
    price = float(get_current_stock_price(symbol))
    return Transaction(symbol, qty, price)
