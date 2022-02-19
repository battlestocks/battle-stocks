from battle_stocks.classes.prompt import Prompt
from battle_stocks.classes.stock import Stock
from battle_stocks.classes.user import User
from battle_stocks.classes.transaction import Transaction
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
            if float(get_current_stock_price(stock_symbol)) * float(shares) > user.bank.balance:
                print('Unfortunately, you currently do not have enough money to purchase your desired amount of shares. Please enter another amount.')
            else:
                # To do: subtract the amount from bank balance
                transact = Transaction(stock_symbol, shares)
                if stock_name in user.holding_stock_names:
                    # find the exsiting stock and update the shares
                    for stock in user.portfolio.stocks:
                        if stock.name == stock_name:
                            stock.total_shares += float(shares)
                            stock.transactions.append(transact)
                else:
                    new_stock = Stock(stock_name, stock_symbol)
                    new_stock.total_shares += float(shares)
                    new_stock.transactions.append(transact)
                    user.holding_stock_names.append(stock_name)
                    # user.portfolio.add_stock(new_stock)
                    user.portfolio.stocks.append(new_stock)
                ################# debugging purpose
                # print(user.portfolio.stocks[0].name, user.portfolio.stocks[0].total_shares)
                # for stock in user.portfolio.stocks:
                #     for transct in stock.transactions:
                #         print(transct.symbol, transct.qty)
                ##################
        if validated_b_s_q == 'S':
            # Prompt.sell_stock_prompt()
            pass
        if validated_b_s_q == 'Q':
            Prompt.quit()
        validated_b_s_q = Prompt.continue_or_print()

if __name__ == "__main__":
    main()
