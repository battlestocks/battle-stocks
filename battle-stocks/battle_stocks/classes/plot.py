import matplotlib.pyplot as plt
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
  def plot_single_stock(name, transaction, size=size.medium, line_color=colors.green, face_color=colors.grey, edge_color=colors.black, marker=markers.small, line_style=line_styles.dashdot):
    x = [date[0] for date in transaction.price_history]
    y = [price[1] for price in transaction.price_history]
    x_ticks = []
    y_ticks = [int(price) for price in y]
    for i in range(len(x)):
      if i % 5 == 0:
        x_ticks.append(x[i])

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
    ax.set_xticks(x_ticks)
    ax.set_yticks(y_ticks)
    tick_size = 6
    rotation_x = 45
    plt.xticks(rotation=rotation_x, size=tick_size)
    plt.yticks(size=tick_size)
    plt.show()

  @staticmethod
  def plot_portfolio(portfolio, size=size.large, line_color=colors.green, face_color=colors.grey, edge_color=colors.black, marker=markers.small, line_style=line_styles.dashdot):
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
      x = [date[0] for date in stock.price_history]
      y = [price[1] for price in stock.price_history]

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
