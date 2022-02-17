from battle_stocks.classes.bank import Bank
from classes.stock import Stock
# from battle_stocks.classes.portfolio import Portfolio
# from battle_stocks.classes.user import User
from battle_stocks.utils.constants import SYMBOL

class Prompt:
    def __init__(self, stocks = 0):
        self.bank = Bank()
        self.stocks = stocks
        self.show_stocks = Stock()
        self.status = True

    def stock_greetings():
        print('''
        Welcome to Battle Stocks, an app designed to create investment strategies and develop exciting and new ways to learn stock trade!
        ''')

    def start_investing(self):
        print('''Please enter (y)es to start investing or (n)o to decline''')
        while True:
            user_input = input('> ')
            if user_input == 'n':
                print('Too Bad! Lets invest soon!')
            elif user_input == 'y':
                self.show()

# static method show command  
    # @staticmethod
    def show(self):
        print('''
            Now that you are intersted, you can either buy or sell stocks!

            To buy stocks please enter: (b)uy
            To sell stocks pleaser enter: (s)ell
        ''')
        user_stock_input = input('> ')
        if user_stock_input == 'b':
            self.buy_stock()
        if user_stock_input == 's':
            self.sell_stock()

# static method for buy stock
    @staticmethod
    def buy_stock(self, stock_counter):
        symbol = SYMBOL
        while self.status and self.bank.balance > 0:
            add_stock_list = []
            # print(f'{symbol}')
            print('''From the list of stocks, please enter the stock you would like to buy by entering its accompanied ticker.
            ''')
            user_input = input('> ')

            # 


# static method for sell stock       
    @staticmethod
    def sell_stock(self, stock_counter):
        symbol = SYMBOL
        while self.status and self.bank.balance != 0:
            pass

if __name__ == "__main__":
    prompt = Prompt()
    prompt.stock_greetings()
    prompt.start_investing()
    prompt.buy_stock()
    prompt.sell_stock()
