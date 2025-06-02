from settings import settings
from MetaTrader5 import TIMEFRAME_H4
from mt5 import initialize, shutdown
from mt5.indicators import get_rsi
from mt5.provider import get_commission
from utils import get_trade_directions
from discord_apis.Discord import Discord

WEBHOOK_URL = settings.WEBHOOK_URL
SYMBOLS = settings.TRACKED_SYMBOLS

TIMEFRAME = TIMEFRAME_H4
RSI_OVERBOUGHT = 60.0
RSI_OVERSOLD = 40.0

discord = Discord()
discord.add_channel(WEBHOOK_URL)


def build_signal_message(rsi: float, direction) -> str:
    if direction.get_type() == 0 and rsi <= RSI_OVERSOLD:
        signal = f"{direction.get_symbol()} - BUY"
    elif direction.get_type() == 1 and rsi >= RSI_OVERBOUGHT:
        signal = f"{direction.get_symbol()} - SELL"
    else:
        return ""

    return f"{signal} [RSI 4H: {rsi:.2f}]\n"


def rsi_4h() -> None:
    try:
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
        else:
            pass

    except Exception as e:
        discord.notify_all(f"⚠️ RSI Bot Error: {e}")
    finally:
        shutdown()


if __name__ == "__main__":
    rsi_4h()
