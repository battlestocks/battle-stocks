from battle_stocks.utils.constants import SYMBOL
from battle_stocks.classes.input_validation import InputValidation
import sys


class Prompt:
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
    def collect_user_name():
        user_name = input('Please enter a user name to get started.\n> ')
        print(f'\nWelcome {user_name}!'
        )
        return user_name

    @staticmethod
    def start_investing():
        print(
            '''
\nPlease enter (y)es to start investing or (n)o to decline''')
        user_input = input('> ')
        validated = InputValidation.validate_start_quit(user_input)
        if validated == 'N':
            Prompt.quit()
        elif validated == 'Y':
            return Prompt.buy_sell_or_quit()

    @staticmethod
    def buy_sell_or_quit():
        buy_sell_quit = input('''
To buy stocks please enter: (b)uy
To sell stocks please enter: (s)ell
To quit please enter: (q)uit
> ''')
        return InputValidation.validate_buy_sell_quit(buy_sell_quit)

# static method for buy stock
    @staticmethod
    def buy_stock_prompt():
        stock_list = []
        for stock in SYMBOL:
            stock_list.append(stock)
        company_name = input(f'\nThis is the current list of stocks that are avaiable for purchase: {stock_list}.\nFrom this list, please enter the stock you would like to buy.\n> ')
        # validate company_name
        shares = input(f'How many shares of {company_name} would you like to purchase?\n> ')
        # validae shares
        return [company_name, SYMBOL[company_name], shares]
        # function for checking stock price is less than the balance
    # if the stock price is higher:
    @staticmethod
    def continue_or_quit():
        user_input = input('\nIf you would like to continue purchasing or selling stocks, Please enter (c)ontinue or enter (q)uit to exit.\n> ')
        if user_input == 'c':
            return Prompt.buy_sell_or_quit()
        else:
            Prompt.quit()
        # the user can also have the option to print out a graph of the stock portfolio

    @staticmethod
    def sell_stock_prompt(user):
        print(f'This is your current positions:\n{user.show_current_portfolio()}')
        company_name = input('Which stock would you like to sell?\n> ')
        shares = input(f'How many shares of {company_name} would you like to sell?\n> ')
        # Add input validations for company_name and shares
        return [company_name, SYMBOL[company_name], shares]