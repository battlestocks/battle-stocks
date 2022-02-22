import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

tables = pd.read_html(url, flavor='html5lib')
df = tables[0]
df = df[['Symbol', 'Security']]
df_list = df.to_dict(orient='records')

symbol = df['Symbol']
company = df['Security']

with open('./battle_stocks/utils/sp_500_dict.py', 'w') as f:
  f.write('SP_500 = {\n')
  for i in range(len(symbol)):
    f.write(f'"{symbol[i]}" : "{company[i]}",\n')
  f.write('}')