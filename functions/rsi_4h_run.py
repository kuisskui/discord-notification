from mt5.indicators import get_rsi
from MetaTrader5 import TIMEFRAME_H4

SYMBOL = "EURUSD"
TIMEFRAME = TIMEFRAME_H4


def rsi_4h_run():
    rsi = get_rsi(SYMBOL, TIMEFRAME)
