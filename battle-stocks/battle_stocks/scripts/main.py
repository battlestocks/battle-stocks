from battle_stocks.classes.prompt import Prompt
from battle_stocks.classes.user import User
from battle_stocks.classes.transaction import Transaction
from battle_stocks.utils.validate_transaction import validate_transaction


def main():
    Prompt.stock_greetings()
    user_name = Prompt.collect_user_name()
    user = User(user_name)
    print(f'Your current balance stands at ${user.bank.balance}')
    validated_command = Prompt.start_investing()
    while True:
        if validated_command == 'B':
            buy_stock_info = Prompt.buy_stock_prompt()
            stock_name = buy_stock_info[0]
            stock_symbol = buy_stock_info[1]
            shares = buy_stock_info[2]
            transaction = Transaction(stock_name, stock_symbol, shares, 'buy')

            if validate_transaction(user, transaction) == False:
                print('\nUnfortunately, you currently do not have enough money to purchase your desired amount of shares. Please enter another amount.')
            else:
                user.portfolio.add_stock(transaction)
                user.bank.withdraw(transaction.current_total_value())
                print(f'\nCongratulations! You have successfully purchased {shares} shares of {stock_name} stock. Your current account balance is ${user.bank.get_balance()}')

        if validated_command == 'S':
            sell_stock_info = Prompt.sell_stock_prompt(user)
            stock_name = sell_stock_info[0]
            stock_symbol = sell_stock_info[1]
            shares = sell_stock_info[2]
            transaction_results = user.portfolio.sell_shares(stock_name, stock_symbol, shares)
            if transaction_results == 0:
                print(f"\nSorry. You currently do not have that amount in {stock_name} stocks. Please enter a valid amount.")
            else:
                user.bank.deposit(transaction_results) 
                print(f'\nCongratulations! You have successfully sold {shares} shares of {stock_name} stock. Your current account balance is ${user.bank.get_balance()}')

        if validated_command == 'D':
            deposit_amount = Prompt.deposit_withdraw_prompt('deposit')
            user.bank.deposit(deposit_amount)
            print(f'Congratulations! You successfully deposited ${deposit_amount}! Your current account balance is ${user.bank.get_balance()}')

        if validated_command == 'W':
            withdraw_amount = Prompt.deposit_withdraw_prompt('withdraw')
            if withdraw_amount <= user.bank.get_balance():
                user.bank.withdraw(withdraw_amount)
                print(f'\nCongratulations! You successfully withdrawed ${withdraw_amount}! Your current account balance is ${user.bank.get_balance()}')
            else:
                print(f'\nYou do not have enough balance to widthdraw $ {withdraw_amount}')

        if validated_command == 'P':
            user.portfolio.plot_portfolio()

        if validated_command == 'Q':
            Prompt.quit()
        validated_command = Prompt.continue_or_quit()

if __name__ == "__main__":
    main()
