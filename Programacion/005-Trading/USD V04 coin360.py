import pandas as pd
import requests
import json
import time
import matplotlib.pyplot as plt
import numpy as np

# Obtener los datos de precios del par BTC/USD en velas de 5 minutos durante las últimas 5 horas
symbol = 'BTC'
interval = '5m'
url = f'https://api.coin360.com/v1/coin/markets?coin={symbol}&fiat=USD&period={interval}&length=60'
response = requests.get(url)
data = response.json()[0]['history']

# Convertir los datos de precios en un DataFrame de Pandas
df = pd.DataFrame(data, columns=['time', 'open', 'high', 'low', 'close', 'volume'])
df['time'] = pd.to_datetime(df['time'], unit='s')
df.set_index('time', inplace=True)

# Calcular las líneas de EMA de 20, 50, 100 y 200
df['ema20'] = df['close'].ewm(span=20, adjust=False).mean()
df['ema50'] = df['close'].ewm(span=50, adjust=False).mean()
df['ema100'] = df['close'].ewm(span=100, adjust=False).mean()
df['ema200'] = df['close'].ewm(span=200, adjust=False).mean()

# Visualizar los datos y la dirección del precio
fig, ax = plt.subplots()
ax.plot(df['close'])
ax.plot(df['ema20'])
ax.plot(df['ema50'])
ax.plot(df['ema100'])
ax.plot(df['ema200'])
ax.set_title('Análisis del par BTC/USD')
ax.legend(['Precio', 'EMA20', 'EMA50', 'EMA100', 'EMA200'])
plt.show()
