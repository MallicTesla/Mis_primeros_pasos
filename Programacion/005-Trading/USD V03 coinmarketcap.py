import pandas as pd
import requests
import json
import time
import matplotlib.pyplot as plt
import numpy as np

# Configurar la API Key y el URL base
API_KEY = 'your_api_key_here'
BASE_URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/ohlcv'

# Obtener los datos de precios del par BTC/USD en velas de 5 minutos durante las últimas 5 horas
symbol = 'BTC'
interval = '5m'
limit = 60
response = requests.get(BASE_URL, params={'symbol': symbol, 'interval': interval, 'limit': limit},
                        headers={'X-CMC_PRO_API_KEY': API_KEY})
data = response.json()['data']['quotes']

# Convertir los datos de precios en un DataFrame de Pandas
df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
df.set_index('timestamp', inplace=True)

# Calcular las líneas de EMA de 20, 50, 100 y 200
df['ema20'] = df['close'].ewm(span=20, adjust=False).mean()
df['ema50'] = df['close'].ewm(span=50, adjust=False).mean()
df['ema100'] = df['close'].ewm(span=100, adjust=False).mean()
df['ema200'] = df['close'].ewm(span=200, adjust=False).mean()

# Calcular las resistencias de las últimas 2 horas
last_2_hours = df.iloc[-24:]
resistances = []
for i in range(1, len(last_2_hours) - 1):
    if last_2_hours['high'][i] > last_2_hours['high'][i-1] and last_2_hours['high'][i] > last_2_hours['high'][i+1]:
        resistances.append(last_2_hours['high'][i])

# Calcular la dirección del precio en los siguientes 40 segundos y su probabilidad
last_price = df['close'][-1]
price_direction = None
price_prob = None

# Utilizar un modelo de aprendizaje automático para predecir la dirección del precio en los siguientes 40 segundos
# Este es solo un ejemplo y deberá personalizar esta parte según su modelo específico
# También es posible que desee incluir otros indicadores técnicos y fundamentales en su modelo
# También puede considerar el uso de redes neuronales o otros modelos avanzados de aprendizaje automático
# para obtener una mayor precisión en sus predicciones.
...

# Visualizar los datos y la dirección del precio
fig, ax = plt.subplots()
ax.plot(df['close'])
ax.plot(df['ema20'])
ax.plot(df['ema50'])
ax.plot(df['ema100'])
ax.plot(df['ema200'])
ax.plot(resistances, 'ro')
ax.axhline(last_price, linestyle='--')
ax.set_title('Análisis del par BTC/USD')
ax.legend(['Precio', 'EMA20', 'EMA50', 'EMA100', 'EMA200', 'Resistencias', 'Precio Actual'])
plt.show()
