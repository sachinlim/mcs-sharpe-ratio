<img align="right" src="https://cdn-icons-png.flaticon.com/512/9144/9144377.png" width="125">

# MCS - Sharpe Ratio

## Prerequisites

The script requires a few installations for extracting and storing of data from the S&P 500. Information is collected from Yahoo Fiannce using [pandas-datareader](https://pydata.github.io/pandas-datareader/).

Installing using `pip`

```
pip install pandas, numpy, pandas-datareader
```

On MacOS, `pip3` might need to be used
```
pip3 install pandas, numpy, pandas-datareader
```

## Running the script

The number of simulations to be conduected will be asked by the compiler. This will then start the timer and runs the simulations to find the portfolio weightings with the most optimal Sharpe ratio for the time period. 

<p align="center">
  <img src="https://user-images.githubusercontent.com/80691974/208108303-96310acc-fedf-46db-850c-f8a7dd841b06.JPG">
</p>

The output will look like the screenshot above, and will provide the weightings in the order of stocks listed in the [mcs.py](https://github.com/sachinlim/mcs-sharpe-ratio/blob/main/mcs.py#L19) file. 


<p align="center">
  <img src="https://user-images.githubusercontent.com/80691974/208106788-51dff70a-32fc-407e-a4c1-5f9518097fc2.JPG">
</p>

Figure 1 shows the results for 4 runs.

### Run Times

One thing to note with the two screenshots above is that the first one is slightly faster to complete. This is due to it running on Python 3.11, while the second screenshot has simulations running with Python 3.10. This improvement was highlighted in the [official documentation](https://docs.python.org/3/whatsnew/3.11.html#summary-release-highlights) as well.

## Project Aims

Many studies have been conducted over the past 60 years ([Warin, 2021](https://arxiv.org/pdf/2101.02044.pdf)) to be able to predict the stock market prices using different approaches in order to achieve an acceptable rate of return. The aim of this project was to study the effect of over-relying on the Sharpe ratio and how it affects the potential returns for an investor. 

## What is the Sharpe ratio?

William F. Sharpe built upon the idea of performance evaluation through risk-reward analysis and applied the methodology onto the MV approach developed by Markowitz ([Bailey and Lopez de Prado, 2012](https://deliverypdf.ssrn.com/delivery.php?ID=878026005027092092121073110093097010103027035008001066117065020121081067100096126101059057107022010023114101111065091094118108122051044060017007080125114100115066062023080067016125107024067024023090123122106103103072100122095079092112119112126029110&EXT=pdf&INDEX=TRUE)). Since the introduction of the Sharpe ratio in 1966, other analysis models have been introduced which can be used to evaluate performance in a similar manor to the Sharpe ratio. Models such as the Sortino ratio and the Omega ratio have shown some promise, which seem to be a better indicator of performance ([Farinelli et al., 2008](https://d1wqtxts1xzle7.cloudfront.net/47086157/j.jbankfin.2007.12.02620160707-18517-14a6h8r-libre.pdf?1467916611=&response-content-disposition=inline%3B+filename%3DBeyond_Sharpe_ratio_Optimal_asset_alloca.pdf&Expires=1671199897&Signature=WgZMegMhXXcSvXwodUkiiiax2FonyS~33K-mOQDHbDVosd2jhY8HWAkvThJZz1KIwk885tjNrPGDEf0P7hZ3Rv6P7byRO2yL8d4bwcWhsitVz58Z5RKRV2I84fpT7mqKnyE92N-Y-zqwitNSkUq7NaThv8Atp~bE74fZbSDV-c6O4CDGjYAFGqIF9Y37VtOZfYbejXregJgs0hS5-PJOjVjYtCGEy35A-hiu~W5yHhbwrr5~YVsiMVw~yQ1agwGR~An824gXzv7FKqq5Su4-V1ZuOMzkrQtUJfUqMTwRtWuwqAiklvkuWCA5Ln1imOMe2c6KCVSNP7NMI65~IZZVDA__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA)). The Sharpe ratio is defined as:

<p align="center">
  <img src="https://user-images.githubusercontent.com/80691974/208106847-739a405d-fd80-4005-8c5d-843b2dd1c549.JPG">
</p>

A negative ratio would indicate that the portfolio is seeing mostly losses while a positive ratio would confirm that there are positive gains. The ratios between 0 and 1 may not be deemed good by an investor, as many would try to go above a ratio of 1 if possible ([Investopedia](https://www.investopedia.com/terms/s/sharperatio.asp)).

One aspect of the Sharpe ratio is that it considers both uptrend and downtrend of prices as a risk via the standard deviation. When the price of a stock goes up, it should be seen as a positive, but the Sharpe ratio cannot assume this ([Rollinger and Hoffman, 2013](http://ea.kitgain.com/content/uploadfile/202102/9e631613532179.pdf)) and sees price changes in both direction as a risk. However, the Sharpe ratio remains the most common and popular analysis model being used ([Kircher and Rösch, 2021](https://www.sciencedirect.com/science/article/pii/S0378426621002375)) to evaluate performance.
