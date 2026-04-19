import pandas as pd
cash = 0
position = 0
window = 20

df = pd.read_csv('/Users/devesh/Projects/Prep/Prep/backtester/prices_round_1_day_0.csv', sep=';')

pepper = df[df['product'] == 'INTARIAN_PEPPER_ROOT']

# convert to list first so we can use loops for it
prices = pepper['mid_price'].tolist()

# one loop that does everything
for i in range(window, len(prices)):
  rolling_avg = sum(prices[i-window:i]) / window
  if prices[i] < rolling_avg and position == 0:
    cash -= prices[i]
    position = 1
    print(f"BUY at {prices[i]}")
  elif prices[i] > rolling_avg and position == 1:
    cash += prices[i]
    position = 0
    print(f"SELL at {prices[i]}")
print(f"Final cash: {cash} | PNL: {cash:,.2f}")