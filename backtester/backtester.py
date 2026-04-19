import pandas as pd
POSITION_LIMIT = 80
cash = 0
position = 0
spent = 0
earned = 0
window = 20

df = pd.read_csv('/Users/devesh/Projects/Prep/Prep/backtester/prices_round_1_day_0.csv', sep=';')

pepper = df[df['product'] == 'INTARIAN_PEPPER_ROOT']

# convert to list first so we can use loops for it
prices = pepper['mid_price'].tolist()


# one loop that does everything
for i in range(window, len(prices)):
  rolling_avg = sum(prices[i-window:i]) / window

  #Check how much inventory we have left so we don't exceed position limits
  rem_buy = POSITION_LIMIT - position
  rem_sell = POSITION_LIMIT + position

  if prices[i] < rolling_avg and rem_buy > 0:
    qty = min(rem_buy, 10) # buy in increments of 10
    position += qty
    cash -= qty * prices[i]
    spent += qty * prices[i]

    print(f"BUY at {prices[i]}")


  elif prices[i] > rolling_avg and position > 0:
    qty = min(position, 10) # sell in increments of 10
    position -= qty
    cash += qty * prices[i]
    earned += qty * prices[i]

    print(f"SELL at {prices[i]}")

print(f"Final cash: {cash} | PNL: {cash:,.2f}")
