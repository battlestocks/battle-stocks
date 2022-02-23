from bs4 import BeautifulSoup
import requests
from battle_stocks.utils.constants import SYMBOL


def get_current_stock_price(symbol):
    URL = f'https://finance.yahoo.com/quote/{symbol}?p={symbol}'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find('fin-streamer', class_='Fw(b) Fz(36px) Mb(-4px) D(ib)')
    return results.text

# print(get_current_stock_price(SYMBOL['FACEBOOK']))

def get_historical_stock_price(symbol):
    historical_data = []
    URL = f'https://finance.yahoo.com/quote/{symbol}/history?p={symbol}'
    page = requests.get(URL, headers={'User-Agent': 'Custom'})
    soup = BeautifulSoup(page.content, 'html.parser')
    thead = soup.find('thead')
    thead_ths = thead.find_all('th')
    head_row = []
    for th in thead_ths:
        head_row.append(th.text)
    historical_data.append(head_row)
    tbody = soup.find('tbody')
    # looks like find_all only get 100 items
    trs = tbody.find_all('tr')
    for tr in trs:
        row = []
        for td in tr:
            row.append(td.text)
        historical_data.append(row)
    return historical_data

# get_historical_stock_price('AAPL')