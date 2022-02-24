from battle_stocks.classes.user import User
from battle_stocks.classes.transaction import Transaction
from battle_stocks.utils.constants import SYMBOL, STOCKS

FluffyKins = User('Frank')

apple = Transaction('apple', STOCKS.APPLE, 300, 'buy')
book_face = Transaction('FB', STOCKS.FACEBOOK, 100, 'buy')

FluffyKins.portfolio.add_stock(apple)
FluffyKins.portfolio.add_stock(book_face)

## Plot a single stock
# apple.get_price_history()
# apple.plot()


## Plot portfolio
FluffyKins.portfolio.plot_portfolio()
