from battle_stocks.classes.Plot import Plot
from battle_stocks.classes.transaction import Transaction
from battle_stocks.utils.constants import SYMBOL

## Use auto completion or dot notation to check for parameters. 

## Create stock
## Symbol and quantity of purchase
apple = Transaction(SYMBOL['APPLE'], 300)
book_face = Transaction(SYMBOL['FACEBOOK'], 200)

## Get recent stock history (this is currently fake)
## update stock history.  Needs to return an object of { date: date object, price: number/string }
apple.get_price_history()
book_face.get_price_history2()

## Portfolio holds purchased stock transactions
sample_portfolio = [ apple, book_face ]

## Plot Portfolio
## portfolio required, other args optional
# Plot.plot_portfolio(sample_portfolio, line_color=Plot.colors.green, size=Plot.size.medium, face_color=Plot.colors.grey)


## Plot single stock stock
## Name and stock required, other args are optional
# Plot.plot_single_stock('BOOK FACE MEOW!', book_face, size=Plot.size.small)
