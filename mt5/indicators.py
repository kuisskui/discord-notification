import pandas as pd
from ta.momentum import RSIIndicator
import MetaTrader5 as mt5


def get_rsi(symbol: str, timeframe: int = mt5.TIMEFRAME_H4, period: int = 14, bars: int = 100) -> float:
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, bars)

    df = pd.DataFrame(rates)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    df.set_index('time', inplace=True)

    df['RSI'] = RSIIndicator(close=df['close'], window=period).rsi()
    latest_rsi = df['RSI'].iloc[-1]

    return float(latest_rsi)
