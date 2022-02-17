from bs4 import BeautifulSoup
import requests
from battle_stocks.utils.data import symbol


def get_current_stock_price(symbol):
    URL = f'https://finance.yahoo.com/quote/{symbol}?p={symbol}'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find('fin-streamer', class_='Fw(b) Fz(36px) Mb(-4px) D(ib)')
    return results.text

# print(get_current_stock_price(symbol['APPLE']))