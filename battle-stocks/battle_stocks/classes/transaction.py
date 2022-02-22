import datetime
from battle_stocks.utils.scraping import get_current_stock_price, get_historical_stock_price
from battle_stocks.utils.constants import SYMBOL
from battle_stocks.classes.plot import Plot


class Transaction:
  def __init__(self, name, symbol, qty, type):
    self.name = name
    self.symbol = symbol
    self.qty = int(qty)
    self.type = type
    self.purchased_price = self.get_current_price()
    self.purchased_date = datetime.datetime.now().date()
    self.price_history = []

  def sell_stock(self, qty):
      current_price = float(get_current_stock_price(self.symbol))
      print(type(self.qty))
      print(type(qty))
      self.qty -= int(qty)
      return current_price * qty

  def get_current_price(self):
    current_price = get_current_stock_price(self.symbol)
    return float(current_price)

  def get_current_value(self):
    return self.qty * self.get_current_price()
  
  def current_total_value(self):
    current_price = float(get_current_stock_price(self.symbol))
    return current_price * int(self.qty)

  def get_price_history(self):
    data = get_historical_stock_price(self.symbol)
    data = data[1:]
    hist_list = []
    for i in data:
      if len(i) < 5:
        continue
      date = i[0].replace(',', '')
      date = datetime.datetime.strptime(date, '%b %d %Y')
      date = date.date()
      closing_price = float(i[4])
      hist_list.append((date, closing_price))
    hist_list.reverse()
    self.price_history = hist_list
    return hist_list

  def plot(self):
    Plot.plot_single_stock(f'Chart for {self.symbol}', self)


  @staticmethod
  def buy_stock(name, symbol, qty, type):
    # Returns a Transaction instance
    return Transaction(name, symbol, qty, type)
