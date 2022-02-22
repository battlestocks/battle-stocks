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
        prompt = 'Please enter a user name to get started.\n> '
        user_name = input(prompt)
        validated_user_name = InputValidation.validate_user_name(user_name, prompt)
        print(f'\nWelcome {validated_user_name}!'
        )
        return validated_user_name

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
            return Prompt.command()

    @staticmethod
    def command():
        command_prompt = '''
To buy stocks please enter: (b)uy
To sell stocks please enter: (s)ell
To deposit money please enter: (d)eposit
To withdraw money please enter: (w)ithdraw
To quit please enter: (q)uit
> '''
        user_input = input(command_prompt)
        return InputValidation.validate_command(user_input, command_prompt)

    @staticmethod
    def buy_stock_prompt():
        stock_list = []
        for stock in SYMBOL:
            stock_list.append(stock)
        company_name_prompt = f'\nThis is the current list of stocks that are avaiable for purchase: {stock_list}.\nFrom this list, please enter the stock you would like to buy.\n> '
        company_name = input(company_name_prompt)
        validated_company_name = InputValidation.validate_company_name(company_name, company_name_prompt)
        shares_prompt = f'How many shares of {validated_company_name} would you like to purchase?\n> '
        shares = input(shares_prompt)
        validated_shares = InputValidation.validate_numbers(shares, shares_prompt)
        return [validated_company_name, SYMBOL[validated_company_name], validated_shares]

    @staticmethod
    def continue_or_quit():
        user_input = input('\nIf you would like to continue purchasing or selling stocks, Please enter (c)ontinue or enter (q)uit to exit.\n> ')
        while user_input.upper() not in ['C', 'Q']:
            user_input = input('\nIf you would like to continue purchasing or selling stocks, Please enter (c)ontinue or enter (q)uit to exit.\n> ')
        if user_input.upper() == 'C':
            return Prompt.command()
        elif user_input.upper() == 'Q':
            Prompt.quit()

    @staticmethod
    def sell_stock_prompt(user):
        company_name_prompt = f'This is your current positions:\n{user.show_current_portfolio()}\nWhich stock would you like to sell?\n> '
        company_name = input(company_name_prompt)
        validated_company_name = InputValidation.validate_company_name(company_name, company_name_prompt)
        shares_prompt = f'How many shares of {company_name} would you like to sell?\n> '
        shares = input(shares_prompt)
        validated_shares = InputValidation.validate_numbers(shares, shares_prompt)
        return [validated_company_name, SYMBOL[validated_company_name], validated_shares]

    @staticmethod
    def deposit_withdraw_prompt(option):
        amount_prompt = f'How much do you want to {option}?\n> '
        amount = input(amount_prompt)
        validated_amount = InputValidation.validate_numbers(amount, amount_prompt)
        return validated_amount

