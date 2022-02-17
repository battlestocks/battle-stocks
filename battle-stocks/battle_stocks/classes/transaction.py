import datetime
from battle_stocks.utils.scraping import get_current_stock_price
from battle_stocks.utils.constants import SYMBOL

# Place holder Tester
# def get_current_stock_price(symbol):
#   return '75.86'

class Transaction:
  def __init__(self, symbol, qty, price):
    self.symbol = symbol
    self.qty = qty
    self.purchased_price = price
    self.purchased_date = datetime.datetime.now().date()

  def sell_stock(self, qty):
      current_price = float(get_current_stock_price(self.symbol))
      self.qty -= qty
      self.sold_date = datetime.datetime.now().date()
      return current_price * qty

  def get_current_price(self):
    current_price = get_current_stock_price(self.symbol)
    return float(current_price)

  def get_current_value(self):
    return self.qty * self.current_price
  
  def current_total_value(self):
    current_price = float(get_current_stock_price(self.symbol))
    return current_price * self.qty
 
  @staticmethod
  def buy_stock(symbol, qty):
    # Returns a Transaction instance
    price = float(get_current_stock_price(symbol))
    return Transaction(symbol, qty, price)



## Sample Output: 
# apple_stock = Transaction.buy_stock(SYMBOL['APPLE'], 20)
# print(apple_stock.current_total_value()) # 3451.0
# sold_value = apple_stock.sell_stock(10) 
# print(sold_value) # 1725.5
# print(apple_stock.qty)  #10
# print(apple_stock.current_total_value()) #1725.5
# print(apple_stock.purchased_price) # 172.55
# print(apple_stock.purchased_date) # 2022-02-16
