import os
import logging

from MetaTrader5 import TIMEFRAME_H4
from mt5 import initialize, shutdown
from mt5.indicators import get_rsi
from mt5.provider import get_commission
from utils import get_trade_directions
from discord_apis.Discord import Discord

WEBHOOK_URL = os.getenv("WEBHOOK_URL")
SYMBOLS = ["AUDUSD", "DXY", "EURUSD", "GBPUSD", "NZDUSD", "USDCAD", "USDCHF", "USDJPY"]

TIMEFRAME = TIMEFRAME_H4
RSI_OVERSOLD = 40.0
RSI_OVERBOUGHT = 60.0

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
discord = Discord()
discord.add_channel(WEBHOOK_URL)


def build_signal_message(rsi: float, direction) -> str:
    """Constructs the notification message based on RSI and trade direction."""
    if direction.get_type() == 0 and rsi <= RSI_OVERSOLD:
        signal = f"{direction.get_symbol()} - BUY"
    elif direction.get_type() == 1 and rsi >= RSI_OVERBOUGHT:
        signal = f"{direction.get_symbol()} - SELL"
    else:
        return ""

    return f"{signal} [RSI 4H: {rsi:.2f}]\n"


def rsi_4h() -> None:
    """Fetches 4‑hour RSI, determines trade signal, and notifies Discord if opportunity."""
    try:
        logging.info("Initializing MT5 connection")
        initialize()
        rsis = {}

        for symbol in SYMBOLS:
            rsis[symbol] = get_rsi(symbol, TIMEFRAME)

        commissions = get_commission(SYMBOLS)
        directions = get_trade_directions(commissions)

        messages = ""

        for i in range(len(SYMBOLS)):
            messages += build_signal_message(rsis[SYMBOLS[i]], directions[i])

        if messages:
            discord.notify_all(messages)
            logging.info("Send notification:\n%s", messages)
        else:
            logging.info("No event.")

    except Exception as e:
        logging.error("Error in RSI workflow: %s", e, exc_info=True)
        discord.notify_all(f"⚠️ RSI Bot Error: {e}")
    finally:
        shutdown()
        logging.info("MT5 connection closed")


if __name__ == "__main__":
    rsi_4h()
