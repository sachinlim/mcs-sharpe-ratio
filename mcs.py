import numpy as np
import pandas as pd
import pandas_datareader as pdr
import time


# Number of simulations to be done
def user_input():
    while True:
        try:
            return int(input('Enter number of simulations: '))
        except ValueError:
            print('Please only enter an integer!')


portfolio_limit = user_input()

# Stock list fixed for now
stock_list = ['MSFT', 'AAPL', 'V', 'MA', 'NVDA']
# stockList = ['JNJ', 'UNH', 'PFE', 'LLY', 'ABBV']
# stockList = ['BRK-B', 'JPM', 'BAC', 'WFC', 'SPGI']
# stockList = ['AMT', 'CCI', 'PLD', 'EQIX', 'PSA']
# stockList = ['XOM', 'CVX', 'COP', 'EOG', 'OXY']

# Starting the timer to see how long it takes to run the simulation
start_counter = time.time()

# Importing data from Yahoo Finance into a DataFrame
# start date is one trading day earlier because the first values have NaN
start_date = '2017-06-30'
end_date = '2019-06-28'

data = pd.DataFrame()
for stock in stock_list:
    data[stock] = pdr.DataReader(stock, 'yahoo', start_date, end_date)['Adj Close'].pct_change()

# Generating tangency portfolios
portfolio_weights, portfolio_returns, portfolio_volatility, portfolio_sharpe_ratios = [], [], [], []
trading_days = 252
risk_free_rate = 0

for portfolios in range(portfolio_limit):
    # generating 5 columns of random numbers between 0-1 as weightings
    weights = np.random.random_sample(5, )
    weights = weights / np.sum(weights)
    weights = np.round(weights, 2)

    portfolio_weights.append(weights)

    # Calculating annualised returns
    annualisedReturns = np.sum(data.mean() * weights) * trading_days

    portfolio_returns.append(annualisedReturns)

    # Calculating volatility (standard deviation)
    covariance = data.cov()
    variance = np.dot(weights.T, np.dot(covariance, weights))
    volatility = np.sqrt(variance) * np.sqrt(252)

    portfolio_volatility.append(volatility)

    # Calculating the Sharpe ratio
    sharpeRatio = (annualisedReturns - risk_free_rate) / volatility

    portfolio_sharpe_ratios.append(sharpeRatio)

# Storing all random portfolios from simulation
portfolioSharpeRatios = np.array(portfolio_sharpe_ratios)

mcSimulation = (portfolio_weights, portfolioSharpeRatios)
mcsData = pd.DataFrame(mcSimulation).T
mcsData.columns = ["Portfolio Weights", "Sharpe Ratio"]

# Pulling the row with the highest Sharpe ratio
max_sharpe_ratio = mcsData.iloc[mcsData["Sharpe Ratio"].astype(float).idxmax()]
print(max_sharpe_ratio)

# End of simulation time
end_counter = time.time()
time = end_counter - start_counter

print("Runtime: " + str(round(time, 2)) + "seconds")
#