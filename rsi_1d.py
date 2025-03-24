import os
import logging

from MetaTrader5 import TIMEFRAME_D1
from mt5 import initialize, shutdown
from mt5.indicators import get_rsi
from discord_apis.Discord import Discord

# Configuration
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
SYMBOL = "EURUSD"
TIMEFRAME = TIMEFRAME_D1
RSI_OVERBOUGHT = 70.0
RSI_OVERSOLD = 30.0

# Setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
discord = Discord()
discord.add_channel(WEBHOOK_URL)


def rsi_1d() -> None:
    """Fetches 1‑day RSI and notifies Discord on overbought/oversold signals."""
    try:
        logging.info("Initializing MT5")
        initialize()

        rsi = get_rsi(SYMBOL, TIMEFRAME)
        logging.info("RSI fetched: %.2f", rsi)

        if rsi >= RSI_OVERBOUGHT or rsi <= RSI_OVERSOLD:
            message = f"{SYMBOL}: RSI 1D signal {rsi:.2f}"
            logging.info("Sending signal: %s", message)
            discord.notify_all(message)
        else:
            logging.info("No signal — RSI within normal range")

    except Exception as e:
        logging.exception("Error calculating RSI")
        discord.notify_all(f"⚠️ RSI 1D Bot Error: {e}")

    finally:
        shutdown()
        logging.info("MT5 connection closed")


if __name__ == "__main__":
    rsi_1d()
