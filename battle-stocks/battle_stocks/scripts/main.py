from battle_stocks.classes.prompt import Prompt
from battle_stocks.classes.user import User
from battle_stocks.classes.transaction import Transaction
from battle_stocks.utils.validate_transaction import validate_transaction
from battle_stocks.utils.scraping import get_current_stock_price


def main():
    Prompt.stock_greetings()
    user_name = Prompt.collect_user_name()
    user = User(user_name)
    print(f'Your current balance stands at ${user.bank.balance}')
    validated_b_s_q = Prompt.start_investing()
    while True:
        if validated_b_s_q == 'B':
            buy_stock_info = Prompt.buy_stock_prompt()
            stock_name = buy_stock_info[0]
            stock_symbol = buy_stock_info[1]
            shares = buy_stock_info[2]
            transaction = Transaction(stock_name, stock_symbol, shares, 'buy')

            if validate_transaction(user, transaction) == False:
                print('Unfortunately, you currently do not have enough money to purchase your desired amount of shares. Please enter another amount.')
            else:
                user.portfolio.add_stock(transaction)
                user.bank.withdraw(transaction.current_total_value())
                print(f'Congratulations! You have successfully purchased {shares} shares of {stock_name} stock. Your current account balance is ${user.bank.get_balance()}')

        if validated_b_s_q == 'S':
            sell_stock_info = Prompt.sell_stock_prompt(user)
            stock_name = sell_stock_info[0]
            stock_symbol = sell_stock_info[1]
            shares = sell_stock_info[2]
            transaction_results = user.portfolio.sell_shares(stock_name, stock_symbol, shares)
            if transaction_results == 0:
                print("You don't own that much stock.  Blah blah blah")
            else:
                user.bank.deposit(transaction_results) 
                print(f'Congratulations! You have successfully sold {shares} shares of {stock_name} stock. Your current account balance is ${user.bank.get_balance()}')

        if validated_b_s_q == 'Q':
            Prompt.quit()
        validated_b_s_q = Prompt.continue_or_quit()

if __name__ == "__main__":
    main()
