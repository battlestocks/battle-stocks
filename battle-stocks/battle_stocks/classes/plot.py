import matplotlib.pyplot as plt
from battle_stocks.classes.transaction import Transaction
from battle_stocks.utils.constants import SYMBOL


class Colors:
  red = '#9b1414'
  blue = '#65a4eb'
  green = '#03a31e'
  pinky = '#ffaaff'
  grey = '#dbdbdb'
  black = '#131212'
  white = '#ffffff'

class Markers:
  small = '.'
  large = 'o'
  triange_up = 6
  triangle_down = 7
class LineStyles:
  solid = 'solid'
  dotted = 'dotted'
  dashdot = 'dashdot'
  none = None

class Size:
  small = (3,3)
  medium = (5,5)
  large = (8,8)
  huge = (15,15)


class Plot:
  colors = Colors()
  markers = Markers()
  line_styles = LineStyles()
  size = Size()

  @staticmethod
  def plot_single_stock(name, transaction, size=(6,6), line_color=colors.green, face_color=colors.grey, edge_color=colors.black, marker=markers.small, line_style=line_styles.dashdot):
    x = list(transaction.price_history.keys())
    x = [date.strftime('%m-%d-%Y') for date in x ]
    y = list(transaction.price_history.values())
    
    # Figure settings
    fig = plt.figure(
      figsize=size, 
      facecolor=face_color, 
      edgecolor=edge_color
      )
    ax = plt.axes()

    # Line Styles
    ax.plot( x, y,
      color = line_color, 
      linestyle = line_style, 
      linewidth = 1.0,
      marker = marker
      )

    # Tiles / Ticks
    ax.set_title(f'Stock price for {name}')
    ax.set_xlabel('Date')
    ax.set_ylabel('Stock Price')
    ax.set_xticks(x)
    ax.set_yticks(y)
    plt.show()


  @staticmethod
  def plot_portfolio(portfolio, size=(15,8), line_color=colors.green, face_color=colors.grey, edge_color=colors.black, marker=markers.small, line_style=line_styles.dashdot):
    # Figure settings
    fig = plt.figure(
      figsize=size, 
      facecolor=face_color, 
      edgecolor=edge_color
      )
    # Labeling
    ax = plt.axes()
    ax.set_title(f'Stock Performance')
    ax.set_xlabel('Dates')
    ax.set_ylabel('Stock Price')
    for stock in portfolio:
      # Set X values: dates
      x = list(stock.price_history.keys())
      x = [date.strftime('%m-%d-%Y') for date in x ]

      # Set Y values: prices
      y = list(stock.price_history.values())

      ax.plot( x, y,
        color = line_color, 
        linestyle = line_style, 
        linewidth = 1.0,
        marker = marker
        )
    plt.show()
    

  ## WIP Stretch Goal
  @staticmethod
  def plot_portfolio_performance(portfolio, size=(15,8), line_color=colors.green, face_color=colors.grey, edge_color=colors.black, line_style=line_styles.dashdot, marker=markers.small):
    # Figure settings
    fig = plt.figure(
      figsize=size, 
      facecolor=face_color, 
      edgecolor=edge_color
      )

    ax = plt.axes()
    ax.set_title(f'Stock Performance')
    ax.set_xlabel('Dates')
    ax.set_ylabel('Stock Price')
    
    total_values = []
    for stock in portfolio:
      # dates
      x = list(stock.price_history.keys())
      x = [date.strftime('%m-%d-%Y') for date in x ]

      # prices
      while len(total_values) < len(x):
        total_values.append(stock.current_total_value())

      ax.plot( x, total_values,
        color = line_color, 
        linestyle = line_style, 
        linewidth = 1.0,
        marker = marker
        )
    plt.show()
