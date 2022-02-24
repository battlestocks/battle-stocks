import pytest
from battle_stocks.utils.scraping import get_historical_stock_price
from battle_stocks.utils.constants import STOCKS

@pytest.mark.scraping
@pytest.fixture
def data():
  data = get_historical_stock_price(STOCKS.MICROSOFT)
  return data


@pytest.mark.scraping
def test__scraping_hist(data):
  assert len(data) > 1
