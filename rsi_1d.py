import os
import logging

from MetaTrader5 import TIMEFRAME_D1
from mt5 import initialize, shutdown
from mt5.indicators import get_rsi
from discord_apis.Discord import Discord

# Configuration
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
SYMBOLS = ["AUDUSD", "DXY", "EURUSD", "GBPUSD", "NZDUSD", "USDCAD", "USDCHF", "USDJPY"]
TIMEFRAME = TIMEFRAME_D1
RSI_OVERBOUGHT = 70.0
RSI_OVERSOLD = 30.0

# Setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
discord = Discord()
discord.add_channel(WEBHOOK_URL)


def build_signal_message(symbol, rsi) -> str:
    """Constructs the notification message based on RSI and trade direction."""
    if rsi >= RSI_OVERBOUGHT or rsi <= RSI_OVERSOLD:
        return f"{symbol} - ALERT [RSI 1D {rsi:.2f}]\n"

    return ""


def rsi_1d() -> None:
    """Fetches 1‑day RSI and notifies Discord on overbought/oversold signals."""
    try:
        logging.info("Initializing MT5")
        initialize()
        rsis = {}

        for symbol in SYMBOLS:
            rsis[symbol] = get_rsi(symbol, TIMEFRAME)

        message = ""

        for key, value in rsis.items():
            message += build_signal_message(key, value)

        if message:
            discord.notify_all(message)
            logging.info("Send notification:\n%s", message)
        else:
            logging.info("No event.")

    except Exception as e:
        logging.exception("Error calculating RSI", e, exc_info=True)
        discord.notify_all(f"⚠️ RSI 1D Bot Error: {e}")

    finally:
        shutdown()
        logging.info("MT5 connection closed")


if __name__ == "__main__":
    rsi_1d()
