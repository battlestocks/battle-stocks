from unicodedata import name
import pandas as pd
from types import SimpleNamespace

url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

tables = pd.read_html(url, flavor='html5lib')
df = tables[0]
df = df[['Symbol', 'Security']]
df_list = df.to_dict(orient='records')

class ClassObj:
  def __init__(self, list):
    self.stocks = SimpleNamespace()
    for i in df_list:
      self.stocks
SP_500 = ClassObj(df_list)
