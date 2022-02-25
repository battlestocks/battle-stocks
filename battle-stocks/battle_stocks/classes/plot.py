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
    c = Colors()
    color_list = []
    color_names = [a for a in dir(c) if not a.startswith('__')]
    for i in color_names:
      color_list.append(c.__getattribute__(i))
    
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
    color_index = 0
    for stock in portfolio:
      if color_index > len(color_names):
        color_index = 0
      stock.get_price_history()
      x = [date[0] for date in stock.price_history]
      y = [price[1] for price in stock.price_history]
      color_name = color_names[color_index]
      ax.plot( x, y,
        color = color_name, 
        linestyle = line_style, 
        linewidth = 1.0,
        marker = marker,
        label=stock.name
        )
      color_index += 1
      ax.legend()
    plt.show()
