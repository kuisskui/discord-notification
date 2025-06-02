from settings import settings
from MetaTrader5 import TIMEFRAME_D1
from mt5 import initialize, shutdown
from mt5.indicators import get_rsi
from discord_apis.Discord import Discord

WEBHOOK_URL = settings.WEBHOOK_URL
SYMBOLS = settings.TRACKED_SYMBOLS

TIMEFRAME = TIMEFRAME_D1
RSI_OVERBOUGHT = 70.0
RSI_OVERSOLD = 30.0

discord = Discord()
discord.add_channel(WEBHOOK_URL)


def build_signal_message(symbol, rsi) -> str:
    if rsi >= RSI_OVERBOUGHT or rsi <= RSI_OVERSOLD:
        return f"{symbol} - ALERT [RSI 1D {rsi:.2f}]\n"

    return ""


def rsi_1d() -> None:
    try:
        initialize()
        rsis = {}

        for symbol in SYMBOLS:
            rsis[symbol] = get_rsi(symbol, TIMEFRAME)

        message = ""

        for key, value in rsis.items():
            message += build_signal_message(key, value)

        if message:
            discord.notify_all(message)
        else:
            pass
    except Exception as e:
        discord.notify_all(f"⚠️ RSI 1D Bot Error: {e}")
    finally:
        shutdown()


if __name__ == "__main__":
    rsi_1d()
