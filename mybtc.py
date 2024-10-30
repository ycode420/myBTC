#!/usr/bin/env /home/cem/.venv/bin/python

import yfinance as yf
import pyfiglet
ascii_banner = pyfiglet.figlet_format("my BTC")  #  erstellt Banner 

my_btc = 0.000001 # mein bestand wird manuell eingegeben 


# Ticker-Symbol für Bitcoin
btcUS = yf.Ticker("BTC-USD")

# Anfragen
btc_preisUSD_now = btcUS.fast_info['lastPrice']
hist = btcUS.history(period="max")

# Daten ermitteln
ath = hist['High'].max()
my_btc2usd = my_btc * btc_preisUSD_now 

# Preis ausgeben
print(ascii_banner)
print(f"# BTC now: {btc_preisUSD_now} $")
print(f"# BTC ath: {ath} $")
print(f"# My invest: {my_btc} btc / {round(my_btc2usd,2)} $ ")

