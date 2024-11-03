#!/usr/bin/env /home/cem/.venv/bin/python  

import argparse
import yfinance as yf
import pyfiglet
# import requests


vers = ("Version 0.1 ")  # ENTER VERSION
my_btc = 0.0001 # ENTER YOUR BTC 



ascii_banner = pyfiglet.figlet_format("myBTC") # ascii will generated

#  define options
parser = argparse.ArgumentParser(prog='myBTC', description='----------------------')
parser.add_argument('-v', '--version', action='store_true', help='shows program version')
parser.add_argument('-pp', '--privatprotect', action='store_true', help='hides my invest entry')
opt = parser.parse_args()



# program head
print(ascii_banner) 
print ("by ycode420\n")

if opt.version:
    print(f"{vers}\n")
    exit()
    
# Ticker-Symbol 
btcUS = yf.Ticker("BTC-USD")

# call ups
btc_preisUSD_now = btcUS.fast_info['lastPrice'] # BTC now 
histATH = btcUS.history(period="max") # ATH 
hist1Y = btcUS.history(period="1y") # 1 Year
hist6mo = btcUS.history(period="6mo") # 6 months
hist3mo = btcUS.history(period="3mo")  # 3 month
hist1mo = btcUS.history(period="1mo") # 1 month
hist1d = btcUS.history(period="1d") # 1 day

# calculate high low prices
ath = histATH['High'].max()
y1 = hist1Y['High'].max()
y6mo = hist6mo['High'].max()
y3mo = hist3mo['High'].max()
y1mo = hist1mo['High'].max() 
y1d = hist1d['High'].max()

athL = histATH['Low'].min()
y1L = hist1Y['Low'].min()
y6moL = hist6mo['Low'].min()
y3moL = hist3mo['Low'].min()
y1moL = hist1mo['Low'].min()
y1dL = hist1d['Low'].min()

my_btc2usd = my_btc * btc_preisUSD_now # calculate  my_btc 

# output

print(f"# BTC now: {btc_preisUSD_now} $")
print(f"# BTC ath: {ath} $")

if not opt.privatprotect:   # if option -pp is set, My Invest entry is not displayed
    print(f"# My invest: {my_btc} btc / {round(my_btc2usd,2)} $ ")
    
print("###############################################")
print(f"# BTC 1 Day  high: {round(y1d,2)} $ low: {round(y1dL,2)} $")
print(f"# BTC 1 Mo   high: {round(y1mo,2)} $ low: {round(y1moL,2)} $")
print(f"# BTC 3 Mo   high: {round(y3mo,2)} $ low: {round(y3moL,2)} $")
print(f"# BTC 6 Mo   high: {round(y6mo,2)} $ low: {round(y6moL,2)} $")
print(f"# BTC 1 Y    high: {round(y1,2)} $ low: {round(y1L,2)} $")

