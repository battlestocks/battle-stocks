import datetime
from battle_stocks.utils.scraping import get_current_stock_price, get_historical_stock_price
from battle_stocks.utils.constants import SYMBOL
from battle_stocks.classes.plot import Plot


class Transaction:
  def __init__(self, symbol, qty):
    self.symbol = symbol
    self.qty = qty
    self.original_qty = qty
    self.purchased_price = self.get_current_price()
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

  def original_transaction_value(self):
    return self.purchased_price * self.original_qty



  @staticmethod
  def buy_stock(symbol, qty):
    # Returns a Transaction instance
    price = float(get_current_stock_price(symbol))
    return Transaction(symbol, qty, price)
