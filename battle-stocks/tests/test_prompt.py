from pickle import FALSE
from battle_stocks.classes.input_validation import InputValidation
from battle_stocks.classes.portfolio import Portfolio
from battle_stocks.scripts.main import main
from battle_stocks.classes.prompt import Prompt
from battle_stocks.classes.user import User
from battle_stocks.utils.validate_transaction import validate_transaction
from colorama import Fore
from battle_stocks.utils.constants import SYMBOL
import sys

def test_main():
  expected = 'b'
  actual = 'q'
  assert expected != actual

def test_validate_start_quit_yes():
  validated = InputValidation.validate_start_quit('Y')
  expected = validated.upper()
  actual = 'Y'
  assert expected == actual

def test_validate_start_quit_no():
  validated = InputValidation.validate_start_quit('N')
  expected = validated.upper()
  actual = 'N'
  assert expected == actual

def test_user_name():
  prompt = Fore.GREEN + 'Please enter a user name to get started.\n> '
  user_input= 'brandon'
  validated = InputValidation.validate_user_name(user_input,prompt)
  expected = 'BRANDON'
  actual = validated.upper()
  assert actual == expected

def test_buy_command():
  prompt = Fore.MAGENTA + '''
To buy stocks please enter: (b)uy
To sell stocks please enter: (s)ell
To deposit money please enter: (d)eposit
To withdraw money please enter: (w)ithdraw
To plot your portfolio please enter (p)lot
To quit please enter: (q)uit
> '''
  user_input = 'b'
  validated = InputValidation.validate_command(user_input, prompt)
  expected = 'B'
  actual = validated.upper()
  assert actual == expected

def test_sell_command():
  prompt = Fore.MAGENTA + '''
To buy stocks please enter: (b)uy
To sell stocks please enter: (s)ell
To deposit money please enter: (d)eposit
To withdraw money please enter: (w)ithdraw
To plot your portfolio please enter (p)lot
To quit please enter: (q)uit
> '''
  user_input = 's'
  validated = InputValidation.validate_command(user_input, prompt)
  expected = 'S'
  actual = validated.upper()
  assert actual == expected

def test_deposit_command():
  prompt = Fore.MAGENTA + '''
To buy stocks please enter: (b)uy
To sell stocks please enter: (s)ell
To deposit money please enter: (d)eposit
To withdraw money please enter: (w)ithdraw
To plot your portfolio please enter (p)lot
To quit please enter: (q)uit
> '''
  user_input = 'd'
  validated = InputValidation.validate_command(user_input, prompt)
  expected = 'D'
  actual = validated.upper()
  assert actual == expected

def test_withdraw_command():
  prompt = Fore.MAGENTA + '''
To buy stocks please enter: (b)uy
To sell stocks please enter: (s)ell
To deposit money please enter: (d)eposit
To withdraw money please enter: (w)ithdraw
To plot your portfolio please enter (p)lot
To quit please enter: (q)uit
> '''
  user_input = 'w'
  validated = InputValidation.validate_command(user_input, prompt)
  expected = 'W'
  actual = validated.upper()
  assert actual == expected

def test_plot_command():
  prompt = Fore.MAGENTA + '''
To buy stocks please enter: (b)uy
To sell stocks please enter: (s)ell
To deposit money please enter: (d)eposit
To withdraw money please enter: (w)ithdraw
To plot your portfolio please enter (p)lot
To quit please enter: (q)uit
> '''
  user_input = 'p'
  validated = InputValidation.validate_command(user_input, prompt)
  expected = 'P'
  actual = validated.upper()
  assert actual == expected

def test_quit_command():
  prompt = Fore.MAGENTA + '''
To buy stocks please enter: (b)uy
To sell stocks please enter: (s)ell
To deposit money please enter: (d)eposit
To withdraw money please enter: (w)ithdraw
To plot your portfolio please enter (p)lot
To quit please enter: (q)uit
> '''
  user_input = 'q'
  validated = InputValidation.validate_command(user_input, prompt)
  expected = 'Q'
  actual = validated.upper()
  assert actual == expected

def test_company_name_apple():
  stock_list = {
    'APPLE': 'AAPL',
    'MICROSOFT': 'MSFT',
    'FACEBOOK': 'FB',
}
  prompt = Fore.GREEN + f'\nThis is the current list of stocks that are available for purchase: {stock_list}.\n\nFrom this list, please enter the stock you would like to buy.\n> '
  user_input = 'apple'
  validated = InputValidation.validate_company_name(user_input, prompt)
  expected = 'APPLE'
  actual = validated.upper()
  assert actual == expected 

def test_company_name_microsoft():
  stock_list = {
    'APPLE': 'AAPL',
    'MICROSOFT': 'MSFT',
    'FACEBOOK': 'FB',
}
  prompt = Fore.GREEN + f'\nThis is the current list of stocks that are available for purchase: {stock_list}.\n\nFrom this list, please enter the stock you would like to buy.\n> '
  user_input = 'microsoft'
  validated = InputValidation.validate_company_name(user_input, prompt)
  expected = 'MICROSOFT'
  actual = validated.upper()
  assert actual == expected

def test_company_name_facebook():
  stock_list = {
    'APPLE': 'AAPL',
    'MICROSOFT': 'MSFT',
    'FACEBOOK': 'FB',
}
  prompt = Fore.GREEN + f'\nThis is the current list of stocks that are available for purchase: {stock_list}.\n\nFrom this list, please enter the stock you would like to buy.\n> '
  user_input = 'facebook'
  validated = InputValidation.validate_company_name(user_input, prompt)
  expected = 'FACEBOOK'
  actual = validated.upper()
  assert actual == expected  

# def test_not_company_name_():
#   stock_list = {
#     'APPLE': 'AAPL',
#     'MICROSOFT': 'MSFT',
#     'FACEBOOK': 'FB',
# }
#   prompt = Fore.GREEN + f'\nThis is the current list of stocks that are available for purchase: {stock_list}.\n\nFrom this list, please enter the stock you would like to buy.\n> '
#   user_input = 'instagram'
#   validated = InputValidation.validate_company_name(user_input, prompt)
#   error_message = Fore.RED + f'\n{validated.upper()} is not available.\n\n {prompt}'
#   expected = error_message
#   actual = validated.upper()
#   assert actual == expected

def test_validate_numbers():
  stock_list = {
    'APPLE': 'AAPL',
    'MICROSOFT': 'MSFT',
    'FACEBOOK': 'FB',
}
  company_name_prompt = Fore.GREEN + f'\nThis is the current list of stocks that are available for purchase: {stock_list}.\n\nFrom this list, please enter the stock you would like to buy.\n> '
  company_name = 'apple'
  validated_company_name = InputValidation.validate_company_name(company_name, company_name_prompt)
  shares_prompts = f'\nHow many shares of {validated_company_name} would you like to purchase?\n> '
  user_input = '10'
  validate_number = InputValidation.validate_numbers(user_input,shares_prompts)
  expected = 10.0
  actual = float(validate_number)
  assert actual == expected

def test_validate_sell_company_name():
  current_portfolio = User.show_current_portfolio
  company_name_prompt = Fore.GREEN+ f'\nThis is your current positions:\n{current_portfolio}\n\nWhich stock would you like to sell?\n> '
  company_name_input = 'apple'
  validated_company_name = InputValidation.validate_company_name(company_name_input, company_name_prompt)
  expected = 'APPLE'
  actual = validated_company_name.upper()
  assert actual == expected

def test_validate_sell_numbers():
  current_portfolio = User.show_current_portfolio
  company_name_prompt = Fore.GREEN+ f'\nThis is your current positions:\n{current_portfolio}\n\nWhich stock would you like to sell?\n> '
  company_name_input = 'apple'
  validated_company_name = InputValidation.validate_company_name(company_name_input, company_name_prompt)
  shares_prompt = Fore.GREEN+ f'\nHow many shares of {company_name_input} would you like to sell?\n> '
  shares = 10
  validated_shares = InputValidation.validate_numbers(shares, shares_prompt)
  expected = 10.0
  actual = float(validated_shares)
  assert actual == expected

def test_withdraw():
  amount_prompt = Fore.GREEN + f'\nHow much do you want to withdraw?\n> '
  amount = '500'
  validated_amount = InputValidation.validate_numbers(amount, amount_prompt)
  expected = 500.00
  actual = float(validated_amount)
  assert actual == expected

def test_deposit():
  amount_prompt = Fore.GREEN + f'\nHow much do you want to deposit?\n> '
  amount = '500'
  validated_amount = InputValidation.validate_numbers(amount, amount_prompt)
  expected = 500.00
  actual = float(validated_amount)
  assert actual == expected

