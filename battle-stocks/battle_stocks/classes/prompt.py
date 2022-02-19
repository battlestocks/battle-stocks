from battle_stocks.classes.bank import Bank
from battle_stocks.classes.stock import Stock
from battle_stocks.utils.constants import SYMBOL
from battle_stocks.classes.input_validation import InputValidation
import sys


class Prompt:
    def __init__(self, stocks=0):
        self.bank = Bank()
        self.stocks = stocks
        # self.show_stocks = Stock()

    @staticmethod
    def stock_greetings():
        print(
            '''
Welcome to Battle Stocks, an app designed to create investment strategies and acquire knowledge of stock trade!
            ''')

    @staticmethod
    def quit():
        print('''
Thank you for stopping by!''')
        sys.exit()

    @staticmethod
    def start_investing():
        print(
            '''
Please enter (y)es to start investing or (n)o to decline''')
        user_input = input('> ')
        validated = InputValidation.start_or_quit(user_input)
        if validated == 'N':
            print(
                '''
Too Bad! Lets invest soon!''')
            Prompt.quit()
        elif validated == 'Y':
            Prompt.show()

# static method show command
    @staticmethod
    def show():
        print(
            '''
Now that you are intersted, you can either buy or sell stocks!

To buy stocks please enter: (b)uy
To sell stocks please enter: (s)ell
To quit please enter: (q)uit
            ''')
        # user_stock_input = input('> ')
        # if user_stock_input == 'b':
        #     self.buy_stock()
        # if user_stock_input == 's':
        #     self.sell_stock()

# static method for buy stock
    @staticmethod
    def buy_stock():
        symbol = SYMBOL
        # print the list of stocks and tickers
        print(
            '''
From the list of stocks, please enter the stock you would like to buy by entering its accompanied ticker.
                ''')
        # function for checking stock price is less than the balance
    # if the stock price is higher:
        print(
            '''
Unfortunately, you currently do not have enough money to buy a stock. Please enter another ticker. If you would like to quit please enter q.
                ''')
        user_input = input('< ')
        if user_input == 'q':
            quit()
    # if the stock price is lower:
        print(
            f'''
Congratulations! You can purchase {symbol} stock. Would you like to purchase it?
                ''')
    # yes or no
        user_input = input('< ')
        if user_input == 'n':
            print(
                '''
Please enter another stock you would like to purchase or enter (q)uit to go back to the main menu.
                ''')
        # else the user can take out money from the bank and use it to purchase the stock.
        # the user then can store stocks in portfolio and get the info of its name, ticker, price.
        # the user can also have the option to print out a graph of the stock portfolio
        # or the user can type in quit and it will return to show()


# static method for sell stock

    @staticmethod
    def sell_stock():
        # first print out the tickers of the stocks in portfolio.
        print(
            '''
Which stock would you like to sell?''')
        user_input = input('> ')
        if user_input == SYMBOL:
            # take that stock from portfolio and sell it.
            # add money to the bank
            print(
                f'''
{SYMBOL} has successfully been sold! Would you like to sell another?  
                '''
            )
        continue_input = input('> ')
        if continue_input == 'n':
            Prompt.show()
        elif continue_input == 'y':
            #option to plot the current stock portfolio
            Prompt.sell_stock()

if __name__ == "__main__":
    Prompt.stock_greetings()
    Prompt.start_investing()
    # prompt.buy_stock()
    # prompt.sell_stock()
