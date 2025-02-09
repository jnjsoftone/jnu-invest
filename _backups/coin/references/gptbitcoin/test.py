import os
from dotenv import load_dotenv
import ccxt
import pprint

load_dotenv()

api_key = os.getenv('UPBIT_ACCESS_KEY')
api_secret = os.getenv('UPBIT_SECRET_KEY')


exchange = ccxt.upbit(config={
    'apiKey': api_key,
    'secret': api_secret,
    'enableRateLimit': True
    }
)

# balance = exchange.fetch_balance()
# pprint.pprint(balance)
# krw_balance = balance['KRW']
# pprint.pprint(krw_balance)

ohlcv = exchange.fetch_ohlcv('BTC/USDT', '1h')
pprint.pprint(ohlcv)