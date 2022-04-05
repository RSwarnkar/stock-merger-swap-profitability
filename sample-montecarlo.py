# Code from: https://www.youtube.com/watch?v=_T0l015ecK4&ab_channel=codebliss
# 

# How to How to fit a histogram with a Gaussian distribution in Origin
#  https://www.youtube.com/watch?v=cfW88FZzsyA&ab_channel=SAYPhysics
# https://www.youtube.com/watch?v=Vgzqvhr6srU&ab_channel=PhysicsMatters

# https://www.youtube.com/watch?v=E2zkJnzr1D4&ab_channel=LearnPythonwithRune


import pandas_datareader.data as web
import pandas as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

start = dt.datetime(2017, 01, 03)
end = dt.datetime(2017, 11, 20)

prices = web.DataReader('AAPL', 'google', start, end)['Close']
returns = prices.pct_change()

last_price = prices[-1]

#Number of Simulations
num_simulations = 1000
num_days = 252

simulation_df = pd.DataFrame()

for x in range(num_simulations):
    count = 0
    daily_vol = returns.std()
    
    price_series = []
    
    price = last_price * (1 + np.random.normal(0, daily_vol))
    price_series.append(price)
    
    for y in range(num_days):
        if count == 251:
            break
        price = price_series[count] * (1 + np.random.normal(0, daily_vol))
        price_series.append(price)
        count += 1
    
    simulation_df[x] = price_series
    
fig = plt.figure()
fig.suptitle('Monte Carlo Simulation: AAPL')
plt.plot(simulation_df)
plt.axhline(y = last_price, color = 'r', linestyle = '-')
plt.xlabel('Day')
plt.ylabel('Price')
plt.show()