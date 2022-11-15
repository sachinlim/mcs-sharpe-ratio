import numpy as np
import pandas as pd
import pandas_datareader as pdr
import time

# Starting the timer to see how long it takes to run the simulation
start = time.time()

stockList = ['MSFT', 'AAPL', 'V', 'MA', 'NVDA']
# stockList = ['JNJ', 'UNH', 'PFE', 'LLY', 'ABBV']
# stockList = ['BRK-B', 'JPM', 'BAC', 'WFC', 'SPGI']
# stockList = ['AMT', 'CCI', 'PLD', 'EQIX', 'PSA']
# stockList = ['XOM', 'CVX', 'COP', 'EOG', 'OXY']

# Importing data from Yahoo Finance into a DataFrame
startDate = '2017-06-30'    # start date is one trading day earlier because the first values have NaN
endDate = '2019-06-28'

data = pd.DataFrame()
for stock in stockList:
    data[stock] = pdr.DataReader(stock, 'yahoo', startDate, endDate)['Adj Close'].pct_change()

# Generating tangency portfolios
portfolioWeights, portfolioReturns, portfolioVolatility, portfolioSharpeRatios = [], [], [], []

# Number of simulations
portfolioLimit = 10
tradingDays = 252
riskFreeRate = 0

for portfolios in range(portfolioLimit):
    # generating 5 columns of random numbers between 0-1 as weightings
    weights = np.random.random_sample(5, )
    weights = weights / np.sum(weights)
    weights = np.round(weights, 2)

    portfolioWeights.append(weights)

    # Calculating annualised returns
    annualisedReturns = np.sum(data.mean() * weights) * tradingDays

    portfolioReturns.append(annualisedReturns)

    # Calculating volatility (standard deviation)
    covariance = data.cov()
    variance = np.dot(weights.T, np.dot(covariance, weights))
    volatility = np.sqrt(variance) * np.sqrt(252)

    portfolioVolatility.append(volatility)

    # Calculating the Sharpe ratio
    sharpeRatio = (annualisedReturns - riskFreeRate) / volatility

    portfolioSharpeRatios.append(sharpeRatio)


# Storing all random portfolios from simulation
portfolioSharpeRatios = np.array(portfolioSharpeRatios)

mcSimulation = (portfolioWeights, portfolioSharpeRatios)
mcsData = pd.DataFrame(mcSimulation).T
mcsData.columns = ["Portfolio Weights", "Sharpe Ratio"]

# Pulling the row with the highest Sharpe ratio
maxSharpeRatio = mcsData.iloc[mcsData["Sharpe Ratio"].astype(float).idxmax()]
print(maxSharpeRatio)

# End of simulation time
end = time.time()
time = end - start

print("Runtime: " + str(round(time, 2)) + "seconds")
