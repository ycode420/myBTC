#!/usr/bin/env /home/cem/.venv/bin/python

import yfinance as yf
import pyfiglet

ascii_banner = pyfiglet.figlet_format("myBTC")

my_btc = 0.0001 # mein bestand, wird manuell eingegeben 


# Ticker-Symbol für Bitcoin
btcUS = yf.Ticker("BTC-USD")

# Anfragen
btc_preisUSD_now = btcUS.fast_info['lastPrice'] # BTC now wird ermittelt
histATH = btcUS.history(period="max") # ATH wird ermittelt
hist1Y = btcUS.history(period="1y") # ermittelt die Jahres daten 
hist6mo = btcUS.history(period="6mo") # ermittelt die 3 Monats daten 
hist3mo = btcUS.history(period="3mo") # ermittelt die 3 Monats daten 
hist1mo = btcUS.history(period="1mo") # ermittelt die 1 Monats daten
hist1d = btcUS.history(period="1d") # ermittelt die 1 Monats daten

# Daten ermitteln
ath = histATH['High'].max()
y1 = hist1Y['High'].max()
y6mo = hist6mo['High'].min()
y3mo = hist3mo['High'].max()
y1mo = hist1mo['High'].max()
y1d = hist1d['High'].max()

athL = histATH['Low'].min()
y1L = hist1Y['Low'].min()
y6moL = hist6mo['Low'].min()
y3moL = hist3mo['Low'].min()
y1moL = hist1mo['Low'].min()
y1dL = hist1d['Low'].min()

my_btc2usd = my_btc * btc_preisUSD_now 

# Ausgeben

print(ascii_banner)

print ("by code420\n")
print(f"# BTC now: {btc_preisUSD_now} $")
print(f"# BTC ath: {ath} $")
print(f"# My invest: {my_btc} btc / {round(my_btc2usd,2)} $ ")
print("###############################################")
print(f"# BTC 1 Day  high: {round(y1d,2)} $ low: {round(y1dL,2)} $")
print(f"# BTC 1 Mo   high: {round(y1mo,2)} $ low: {round(y1moL,2)} $")
print(f"# BTC 3 Mo   high: {round(y3mo,2)} $ low: {round(y3moL,2)} $")
print(f"# BTC 6 Mo   high: {round(y6mo,2)} $ low: {round(y6moL,2)} $")
print(f"# BTC 1 Y    high: {round(y1,2)} $ low: {round(y1L,2)} $")

