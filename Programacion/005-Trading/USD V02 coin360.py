import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import requests

# Función para obtener los datos de precios utilizando la API de Coin360
def get_data(symbol, timeframe, limit):
    u =    "https://api.coin360.com/coin/latest?coin=BTC&convert=USD"
    url = f'https://api.coin360.com/coin/latest?coin={symbol}&convert={timeframe}/?limit={limit}'
    response = requests.get(url)
    print (type(response))
    print (response)
    data = response.json()
    print(type(data))
    print (data)
    return data

# Obtener los datos de precios del par EUR/USD en velas de 5 segundos durante los últimos 5 minutos
data = get_data('btc-usd', '5s', 300)

# Convertir los datos de precios en un DataFrame de Pandas
df = pd.DataFrame(data['ohlcv'], columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])

# Convertir la columna timestamp a un objeto datetime y establecerla como el índice del DataFrame
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
df.set_index('timestamp', inplace=True)

# Calcular las líneas de EMA de 20, 50, 100 y 200
df['ema20'] = df['close'].ewm(span=20).mean()
df['ema50'] = df['close'].ewm(span=50).mean()
df['ema100'] = df['close'].ewm(span=100).mean()
df['ema200'] = df['close'].ewm(span=200).mean()

# Calcular las resistencias de las últimas 2 horas
last_2_hours = df.iloc[-24 * 60 / 5:]
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
ax.set_title('Análisis del par EUR/USD')
ax.legend(['Precio', 'EMA20', 'EMA50', 'EMA100', 'EMA200', 'Resistencias', 'Precio Actual'])
plt.show()
