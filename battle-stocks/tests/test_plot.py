import pytest
from battle_stocks.classes.plot import Plot

@pytest.mark.plot
@pytest.fixture
def plot():
  plot = Plot()
  return plot

@pytest.mark.plot
def test_plot_colors(plot):
  assert plot.colors.red == '#9b1414'
  
@pytest.mark.plot
def test_plot_markers(plot):
  assert plot.markers.small == '.'

@pytest.mark.plot
def test_plot_lines(plot):
  assert plot.line_styles.solid == 'solid'

@pytest.mark.plot
def test_plot_size(plot):
  assert plot.size.medium == (5,5)
